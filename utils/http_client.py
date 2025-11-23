# utils/http_client.py
import requests
from requests.exceptions import RequestException

DEFAULT_HEADERS = {
    "User-Agent": "AutoPentestAgent/1.0 (+https://example.local)"
}

def http_get(url, params=None, timeout=8):
    try:
        r = requests.get(url, params=params, headers=DEFAULT_HEADERS, timeout=timeout, verify=False)
        return r.text, r.status_code, r.headers
    except RequestException:
        return None, None, None

def http_post(url, data=None, timeout=8):
    try:
        r = requests.post(url, data=data, headers=DEFAULT_HEADERS, timeout=timeout, verify=False)
        return r.text, r.status_code, r.headers
    except RequestException:
        return None, None, None
