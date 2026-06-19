import os
import requests

def download_file(url, folder):
    os.makedirs(folder, exist_ok=True) # Ensure directory exists
    filename = url.split("/")[-1]
    path = os.path.join(folder, filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return path
