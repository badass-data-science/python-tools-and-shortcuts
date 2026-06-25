# geography/united_states

Utilities for working with US Federal Information Processing Standard (FIPS) codes. FIPS codes uniquely identify US states, territories, and counties and are standardized across the US government by NIST.

Data is sourced from the US Census Bureau's 2020 national county reference file.

## Classes

### `Fips` (base class)

Holds the source URL and download timestamp. Not used directly — use `FipsCounty` or `FipsState`.

### `FipsCounty`

Downloads and stores county-level FIPS codes.

```python
FipsCounty(url_fips_codes: str = <census_bureau_default>)
```

#### Methods

| Method | Description |
|---|---|
| `download_FIPS_codes()` | Downloads the Census Bureau reference file and stores results in `self.df`, sorted by state and county FIPS code |

`self.df` columns include `STATE`, `STATEFP`, `COUNTYFP`, `COUNTYNS`, and county name.

### `FipsState`

Downloads and stores state-level FIPS codes, deduplicated from the same county reference file.

```python
FipsState(url_fips_codes: str = <census_bureau_default>)
```

#### Methods

| Method | Description |
|---|---|
| `download_FIPS_codes()` | Downloads the reference file and stores `STATE` and `STATEFP` columns in `self.df`, sorted by state abbreviation |

### Example

```python
from python_tools_and_shortcuts.geography.united_states.Fips import FipsCounty, FipsState

counties = FipsCounty()
counties.download_FIPS_codes()
print(counties.df.head())

states = FipsState()
states.download_FIPS_codes()
print(states.df)
```

### Dependencies

- `pandas`
