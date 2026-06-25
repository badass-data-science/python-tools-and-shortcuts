# files

File system utilities.

## `download_file`

Downloads a file from a URL to a local directory using streaming, so large files are not loaded entirely into memory.

```python
download_file(url: str, folder: str) -> str
```

| Parameter | Description |
|---|---|
| `url` | Full URL of the file to download |
| `folder` | Local directory to save the file into (created if it does not exist) |

Returns the full local path of the downloaded file. The filename is taken from the last segment of the URL. Raises `requests.HTTPError` if the server returns an error status.

### Example

```python
from python_tools_and_shortcuts.files.downloading import download_file

path = download_file(
    url='https://example.com/data/report.csv',
    folder='./downloads',
)
print(f"Saved to: {path}")
```

### Dependencies

- `requests`
