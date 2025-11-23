# core/scanner.py
import requests
from utils.logger import log
from utils.analyzer import analyze_response
from core.fuzzer import Fuzzer

class Scanner:
    def __init__(self, max_workers=5, delay=0.5):
        self.max_workers = max_workers
        self.delay = delay
        self.fuzzer = Fuzzer()

    def scan_url_basic(self, url):
        """
        BASIC SCANNER:
        - Cek status code
        - Cek response size
        - Cek indikasi SQLi / XSS dari response
        - Mengirim hasil ke analyzer
        """

        log(f"[SCAN] {url}")

        try:
            resp = requests.get(url, timeout=10)
        except Exception as e:
            log(f"[ERR] gagal akses {url} : {e}")
            return []

        results = []

        # Basic fingerprinting
        info = f"Status: {resp.status_code}, Size: {len(resp.text)}"
        results.append(info)

        # Analisa content (misalnya cari error SQL, script tag, dll)
        analysis = analyze_response(resp)
        if analysis:
            results.append(analysis)

        return results
