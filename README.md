# python-tools-and-shortcuts

A reusable Python library containing classes and functions shared across projects. Covers AI/fuzzy logic, LLM clients, Neo4j databases, econometrics, file utilities, US geography, math, and NLP.

## Installation

```bash
pip install git+https://github.com/badass-data-science/python-tools-and-shortcuts.git
```

Or with `uv` as a path dependency in your `pyproject.toml`:

```toml
[tool.uv.sources]
python-tools-and-shortcuts = { git = "https://github.com/badass-data-science/python-tools-and-shortcuts.git" }
```

## Modules

| Module | Contents |
|---|---|
| [`ai/fuzzylogic/`](python_tools_and_shortcuts/ai/fuzzylogic/) | `FuzzyInterpolator` — fuzzy set membership interpolation |
| [`ai/llm/`](python_tools_and_shortcuts/ai/llm/) | `OllamaInator` — Ollama LLM client |
| [`databases/influxdb/`](python_tools_and_shortcuts/databases/influxdb/) | `InfluxDbTool` — Flux query execution, bulk insert, bucket management |
| [`databases/neo4j/`](python_tools_and_shortcuts/databases/neo4j/) | `Neo4jInterface`, `Neo4jGraphDataScienceInterface` |
| [`econometrics/`](python_tools_and_shortcuts/econometrics/) | `get_most_recent_ticker_close_value` — Yahoo Finance ticker data |
| [`files/`](python_tools_and_shortcuts/files/) | `download_file` — streaming file downloader |
| [`geography/united_states/`](python_tools_and_shortcuts/geography/united_states/) | `FipsCounty`, `FipsState` — US FIPS code data |
| [`math/`](python_tools_and_shortcuts/math/) | `calculate_list_entropy`, `regression_first_order` |
| [`nlp/`](python_tools_and_shortcuts/nlp/) | `calculate_part_of_speech_tags` — NLTK POS tagging |

## Requirements

Python 3.10+. See [`pyproject.toml`](pyproject.toml) for the full dependency list.

## Tests

```bash
uv sync --extra dev
uv run pytest -v
```

Currently covers `InfluxDbTool`'s Flux-query-to-dataframe timestamp conversion
(`tests/databases/influxdb/`) — the rest of this library doesn't have test
coverage yet.
