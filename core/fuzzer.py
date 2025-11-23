# core/fuzzer.py
import os
from utils.http_client import http_get, http_post
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from utils.logger import log

class Fuzzer:
    def __init__(self, payload_dir="data"):
        self.payloads = {
            "sqli": self._load_payloads(os.path.join(payload_dir, "payloads_sql.txt")),
            "xss": self._load_payloads(os.path.join(payload_dir, "payloads_xss.txt")),
            "lfi": self._load_payloads(os.path.join(payload_dir, "payloads_lfi.txt"))
        }

    def _load_payloads(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip() and not line.startswith("#")]
        except FileNotFoundError:
            return []

    def fuzz_get_params(self, url):
        """
        For each GET parameter, inject payloads and return list of (tested_url, body, status)
        """
        results = []
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if not qs:
            return results

        for pname in qs.keys():
            for cat, payloads in self.payloads.items():
                for p in payloads:
                    test_qs = {k: (v if k!=pname else [v[0]+p]) for k,v in qs.items()}
                    new_query = urlencode({k: v[0] for k,v in test_qs.items()})
                    test_parts = list(parsed)
                    test_parts[4] = new_query
                    tested_url = urlunparse(test_parts)
                    body, status, headers = http_get(tested_url)
                    results.append({
                        "url": tested_url,
                        "category": cat,
                        "payload": p,
                        "body": body,
                        "status": status
                    })
        return results

    def fuzz_post_form(self, action_url, form_fields):
        """
        form_fields: dict name->value
        """
        results = []
        for cat, payloads in self.payloads.items():
            for p in payloads:
                data = {k:(v+p if isinstance(v,str) else v) for k,v in form_fields.items()}
                body, status, headers = http_post(action_url, data=data)
                results.append({
                    "url": action_url,
                    "category": cat,
                    "payload": p,
                    "body": body,
                    "status": status
                })
        return results

    def deep_fuzz(self, url):
        log(f"[FUZZ] Deep fuzzing {url}")
        res_get = self.fuzz_get_params(url)
        return res_get
