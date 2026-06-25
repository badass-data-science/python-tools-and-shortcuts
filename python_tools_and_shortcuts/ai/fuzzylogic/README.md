# ai/fuzzylogic

Fuzzy logic utilities built on top of [`scikit-fuzzy`](https://pythonhosted.org/scikit-fuzzy/).

## `FuzzyInterpolator`

Constructs a set of named fuzzy membership functions over a shared domain and interpolates a crisp value's degree of membership in each set.

### Membership function shapes

The shape of each set's membership function is inferred from the length of its range list:

| Range list length | Shape | When used |
|---|---|---|
| `[min, max]` | Z-shaped (decreasing) | First set in the ordered list |
| `[min, max]` | S-shaped (increasing) | Last set in the ordered list |
| `[min, mid, max]` | Triangular | All interior sets |

### Constructor

```python
FuzzyInterpolator(
    list_increasingly_ordered_set_names: list,
    dict_ranges: dict,
    step: float = 0.001,
)
```

| Parameter | Description |
|---|---|
| `list_increasingly_ordered_set_names` | Ordered list of set names, from lowest to highest |
| `dict_ranges` | Dict mapping each set name to its `[min, max]` or `[min, mid, max]` breakpoints |
| `step` | Domain resolution (default `0.001`) |

### Methods

#### `interpolate_membership(value_to_interpolate) -> dict`

Returns a dict mapping each set name to the crisp value's degree of membership (0.0–1.0). Values outside the domain are clamped to the domain boundary.

#### `plot_membership_functions(title, xlabel)`

Displays a matplotlib plot of all membership functions.

### Example

```python
from python_tools_and_shortcuts.ai.fuzzylogic.FuzzyInterpolator import FuzzyInterpolator

set_names = ['low', 'medium', 'high']
ranges = {
    'low':    [0, 30],
    'medium': [0, 30, 60],
    'high':   [30, 60],
}

fi = FuzzyInterpolator(set_names, ranges)
print(fi.interpolate_membership(20))
# {'low': 0.333..., 'medium': 0.666..., 'high': 0.0}
```

### Dependencies

- `numpy`
- `scikit-fuzzy`
- `matplotlib`
