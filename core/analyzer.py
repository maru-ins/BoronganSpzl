# core/analyzer.py
import re
from utils.logger import log

class Analyzer:
    def __init__(self):
        # regex patterns for errors / indicators
        self.sql_error_patterns = [
            r"you have an error in your sql syntax",
            r"warning: mysql",
            r"mysql_fetch",
            r"syntax error.*sql",
            r"ora-\d+",
            r"unclosed quotation mark after the character string"
        ]
        self.xss_indicators = [
            "<script>alert(",
            "javascript:alert(",
            "onerror=",
            "onload="
        ]
        self.lfi_indicators = [
            "root:x:0:0:", "/etc/passwd", "boot.ini"
        ]

    def analyze(self, body, source_url=None):
        findings = []
        if not body:
            return findings

        text = body.lower()

        # SQL errors
        for p in self.sql_error_patterns:
            if re.search(p, text):
                findings.append("Possible SQL Injection (database error pattern found)")
                log(f"[ANALYZER] SQL pattern matched on {source_url}")
                break

        # XSS reflection
        for x in self.xss_indicators:
            if x in text:
                findings.append("Possible XSS (payload reflection detected)")
                log(f"[ANALYZER] XSS indicator matched on {source_url}")
                break

        # LFI
        for l in self.lfi_indicators:
            if l in text:
                findings.append("Possible Local File Inclusion / sensitive file exposure")
                log(f"[ANALYZER] LFI indicator matched on {source_url}")
                break

        # Directory listing
        if "index of /" in text:
            findings.append("Directory listing detected")

        if not findings:
            findings.append("No common vuln patterns detected")

        return findings
