# core/agent.py
from core.crawler import Crawler
from core.scanner import Scanner
from core.report import Report
from utils.logger import log
from utils.parser import extract_domain

class AutoPentestAgent:
    def __init__(self, target, max_workers=5, delay=1):
        self.target = target
        self.max_workers = max_workers
        self.delay = delay
        self.domain = extract_domain(target)
        self.crawler = Crawler(target, max_pages=150)
        self.scanner = Scanner()
        self.report = Report()

    def run(self):
        log("[+] AutoPentestAgent starting")
        urls = self.crawler.crawl()
        log(f"[+] {len(urls)} pages discovered")

        for url in urls:
            findings = self.scanner.scan_url_basic(url)
            # findings may be list of strings or dicts depending on analyzer/fuzzer results
            if findings:
                for f in findings:
                    entry = {
                        "target": self.target,
                        "url": url,
                        "finding": f
                    }
                    self.report.add(entry)

                    # Decision logic: if scan finds "Possible SQL Injection", trigger deep fuzz
                    if isinstance(f, list):
                        # rule-based detection from analyzer (list of strings)
                        for note in f:
                            if "sql" in note.lower():
                                log(f"[DECISION] SQL signal on {url} -> deep fuzzing")
                                fuzz_results = self.scanner.fuzzer.deep_fuzz(url)
                                for fr in fuzz_results:
                                    entry2 = {
                                        "target": self.target,
                                        "url": fr.get("url"),
                                        "finding": {
                                            "category": fr.get("category"),
                                            "payload": fr.get("payload"),
                                            "analysis_excerpt": (fr.get("body") or "")[:300]
                                        }
                                    }
                                    self.report.add(entry2)
                    else:
                        # if f is a dict (fuzzer finding)
                        if isinstance(f, dict) and "category" in f:
                            log(f"[!] Vulnerability candidate: {f.get('category')} on {f.get('tested_url', url)}")
        # export report
        self.report.export()
        log("[+] AutoPentestAgent finished")
