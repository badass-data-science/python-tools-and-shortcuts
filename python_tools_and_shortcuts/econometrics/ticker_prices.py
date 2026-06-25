import yfinance as yf

def get_most_recent_ticker_close_value(symbol, period : str = '7d') -> float:
    df_history = yf.Ticker(symbol).history(period=period)

    # QA
    if df_history.empty or "Close" not in df_history.columns:
        raise RuntimeError(f"No {symbol!r} close data returned for period = {period!r}.")
    
    series_closes = df_history["Close"].dropna()

    # QA
    if series_closes.empty:
        raise RuntimeError(f"{symbol!r} close data was returned but contained no valid values.")
    
    value = float(series_closes.iloc[-1])
    return value
