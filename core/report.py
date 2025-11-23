# core/report.py
import json
from utils.logger import log
import time

class Report:
    def __init__(self):
        self.findings = []

    def add(self, entry):
        """
        entry: dict with keys like url, type, payload, details
        """
        self.findings.append(entry)

    def save_txt(self, filename=None):
        if not filename:
            filename = f"report_{int(time.time())}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for e in self.findings:
                f.write(json.dumps(e, ensure_ascii=False, indent=2))
                f.write("\n\n")
        log(f"[REPORT] Saved TXT report -> {filename}")

    def save_json(self, filename=None):
        if not filename:
            filename = f"report_{int(time.time())}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.findings, f, ensure_ascii=False, indent=2)
        log(f"[REPORT] Saved JSON report -> {filename}")

    def export(self):
        self.save_json()
        self.save_txt()
