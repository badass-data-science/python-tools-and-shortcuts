# econometrics

Utilities for retrieving financial market data.

## `get_most_recent_ticker_close_value`

Fetches the most recent closing price for a given ticker symbol from Yahoo Finance.

```python
get_most_recent_ticker_close_value(symbol: str, period: str = '7d') -> float
```

| Parameter | Description |
|---|---|
| `symbol` | Yahoo Finance ticker symbol (e.g. `'AAPL'`, `'^VIX'`) |
| `period` | Lookback period passed to `yfinance` (default `'7d'`). Valid values: `'1d'`, `'5d'`, `'1mo'`, `'3mo'`, etc. |

Returns the most recent non-null closing value as a `float`. Raises `RuntimeError` if no data is returned or all close values are null.

### Example

```python
from python_tools_and_shortcuts.econometrics.ticker_prices import get_most_recent_ticker_close_value

vix = get_most_recent_ticker_close_value('^VIX')
print(f"Most recent VIX close: {vix}")

aapl = get_most_recent_ticker_close_value('AAPL', period='1mo')
print(f"Most recent AAPL close: {aapl}")
```

### Dependencies

- `yfinance`
