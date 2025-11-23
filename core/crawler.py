# core/crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from utils.parser import extract_domain
from utils.logger import log

class Crawler:
    def __init__(self, base_url, max_pages=200):
        self.base_url = base_url.rstrip("/")
        self.domain = extract_domain(base_url)
        self.visited = set()
        self.found_urls = set()
        self.max_pages = max_pages

    def _is_internal(self, url):
        try:
            return self.domain in url
        except:
            return False

    def crawl(self):
        to_visit = [self.base_url]
        while to_visit and len(self.visited) < self.max_pages:
            url = to_visit.pop(0)
            if url in self.visited:
                continue

            try:
                r = requests.get(url, timeout=6, headers={"User-Agent": "AutoPentestAgent/1.0"}, verify=False)
                html = r.text
            except Exception:
                self.visited.add(url)
                continue

            self.visited.add(url)
            self.found_urls.add(url)
            log(f"Found: {url}")

            soup = BeautifulSoup(html, "lxml")
            # find a[href], form actions, script src, link href
            for tag in soup.find_all(['a','form','link','script']):
                attr = 'href' if tag.name in ('a','link') else 'action' if tag.name=='form' else 'src'
                ref = tag.get(attr)
                if not ref:
                    continue
                new_url = urljoin(self.base_url, ref)
                if self._is_internal(new_url) and new_url not in self.visited:
                    to_visit.append(new_url)
        return sorted(self.found_urls)
