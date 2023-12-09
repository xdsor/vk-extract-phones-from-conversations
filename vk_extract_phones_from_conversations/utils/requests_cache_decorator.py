import json
import os

import requests

CACHE_DIR = os.getcwd() + "/cache"


def get(url, headers=None):
    method_from_url = url.split("/")[-1]
    cache_file = f"{CACHE_DIR}/{method_from_url[0:100]}.json"
    if os.path.isfile(cache_file):
        with open(cache_file, "r") as f:
            return json.load(f)
    else:
        response = requests.get(url, headers=headers)
        with open(cache_file, 'w') as f:
            json.dump(response.json(), f, indent=4, ensure_ascii=False)
        return response.json()

