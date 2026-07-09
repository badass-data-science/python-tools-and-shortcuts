from __future__ import annotations

from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from python_tools_and_shortcuts.databases.influxdb.InfluxDbTool import InfluxDbTool

# A fixed, known instant -- 2026-07-08 05:09:24 UTC -- and its correct unix-epoch
# seconds value, computed independently of the code under test.
_KNOWN_INSTANT = "2026-07-08 05:09:24+00:00"
_KNOWN_EPOCH_S = 1783487364


def test_time_column_to_unix_epoch_s_handles_microsecond_precision():
    """This is the exact bug: a non-pivoted Flux query result has been observed to
    parse to datetime64[us], and the old code (`.astype('int64') // 10**9`,
    assuming nanoseconds) silently produced a value 1000x too small for this case
    -- no error, just a wrong number landing around 1970 instead of 2026."""
    series = pd.Series([_KNOWN_INSTANT]).astype("datetime64[us, UTC]")
    result = InfluxDbTool._time_column_to_unix_epoch_s(series)
    assert int(result.iloc[0]) == _KNOWN_EPOCH_S


def test_time_column_to_unix_epoch_s_handles_nanosecond_precision():
    """The previously-working case (every existing production caller's pivoted
    Flux queries happen to parse to this precision) -- must stay correct."""
    series = pd.Series([_KNOWN_INSTANT]).astype("datetime64[ns, UTC]")
    result = InfluxDbTool._time_column_to_unix_epoch_s(series)
    assert int(result.iloc[0]) == _KNOWN_EPOCH_S


def test_time_column_to_unix_epoch_s_handles_second_precision():
    series = pd.Series([_KNOWN_INSTANT]).astype("datetime64[s, UTC]")
    result = InfluxDbTool._time_column_to_unix_epoch_s(series)
    assert int(result.iloc[0]) == _KNOWN_EPOCH_S


def test_time_column_to_unix_epoch_s_handles_plain_strings():
    """pd.to_datetime parses this itself -- covers a raw, not-yet-datetime column
    exactly as it would arrive from query_data_frame before any casting."""
    series = pd.Series([_KNOWN_INSTANT])
    result = InfluxDbTool._time_column_to_unix_epoch_s(series)
    assert int(result.iloc[0]) == _KNOWN_EPOCH_S


def test_run_flux_query_produces_correct_epoch_seconds_not_1000x_too_small():
    """End-to-end through run_flux_query_on_forex_database_and_get_dataframe with
    a mocked client returning a microsecond-precision _time column (the real
    failure mode) -- the regression test for the actual bug, not just the helper
    in isolation."""
    fake_df = pd.DataFrame({
        "_time": pd.Series([_KNOWN_INSTANT]).astype("datetime64[us, UTC]"),
        "_value": [-0.0248],
        "_field": ["long_rate"],
        "_measurement": ["swap-rate"],
        "instrument": ["EUR/USD"],
    })

    with patch("python_tools_and_shortcuts.databases.influxdb.InfluxDbTool.InfluxDBClient") as mock_client_cls:
        mock_query_api = MagicMock()
        mock_query_api.query_data_frame.return_value = fake_df
        mock_client_cls.return_value.query_api.return_value = mock_query_api

        tool = InfluxDbTool("http://fake", "fake-token", "fake-org")
        result = tool.run_flux_query_on_forex_database_and_get_dataframe("fake flux query")

    assert int(result["unix_epoch_s"].iloc[0]) == _KNOWN_EPOCH_S
    assert "_time" not in result.columns


def test_run_flux_query_drops_result_and_table_columns():
    fake_df = pd.DataFrame({
        "result": ["_result"],
        "table": [0],
        "_time": pd.Series([_KNOWN_INSTANT]).astype("datetime64[ns, UTC]"),
        "_value": [1.0],
    })

    with patch("python_tools_and_shortcuts.databases.influxdb.InfluxDbTool.InfluxDBClient") as mock_client_cls:
        mock_query_api = MagicMock()
        mock_query_api.query_data_frame.return_value = fake_df
        mock_client_cls.return_value.query_api.return_value = mock_query_api

        tool = InfluxDbTool("http://fake", "fake-token", "fake-org")
        result = tool.run_flux_query_on_forex_database_and_get_dataframe("fake flux query")

    assert "result" not in result.columns
    assert "table" not in result.columns
