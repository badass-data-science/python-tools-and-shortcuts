# math

General mathematical utilities.

## `calculate_list_entropy`

Calculates the Shannon entropy of a list of strings based on the frequency of each unique item.

```python
calculate_list_entropy(str_list: list, base: float = 2.0) -> np.float64 | None
```

| Parameter | Description |
|---|---|
| `str_list` | List of strings to analyse |
| `base` | Logarithm base for the entropy calculation. Default `2.0` reports entropy in bits. |

Returns `None` if `str_list` is not a list or is empty. Otherwise returns the entropy as `np.float64`. A list of all identical items has entropy `0`; a perfectly uniform distribution has maximum entropy.

### Example

```python
from python_tools_and_shortcuts.math.entropy_calculations import calculate_list_entropy

tags = ['noun', 'verb', 'noun', 'adjective', 'noun', 'verb']
print(calculate_list_entropy(tags))  # ~1.459 bits
```

---

## `regression_first_order`

Fits a simple ordinary least squares (OLS) regression of `y` on `x`.

```python
regression_first_order(x, y) -> tuple[pd.DataFrame, float]
```

| Parameter | Description |
|---|---|
| `x` | Predictor values (list or array-like) |
| `y` | Response values (list or array-like) |

Returns a tuple of:
- `df` — the input data with an added `y_predicted` column of fitted values
- `R_adj` — the adjusted R² of the model

### Example

```python
from python_tools_and_shortcuts.math.regressions import regression_first_order

x = [1, 2, 3, 4, 5]
y = [2.1, 3.9, 6.2, 7.8, 10.1]
df, r_adj = regression_first_order(x, y)
print(f"Adjusted R²: {r_adj:.4f}")
print(df)
```

### Dependencies

- `numpy`
- `scipy`
- `pandas`
- `statsmodels`
