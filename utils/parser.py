# utils/parser.py
from urllib.parse import urlparse, parse_qs, urljoin

def extract_domain(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"

def get_params_from_url(url):
    parsed = urlparse(url)
    return {k: v for k, v in parse_qs(parsed.query).items()}

def join_url(base, href):
    return urljoin(base, href)
