# core/worker.py
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.logger import log
import time

class WorkerPool:
    def __init__(self, max_workers=8, delay_between_requests=0.5):
        self.max_workers = max_workers
        self.delay = delay_between_requests

    def map(self, func, iterable):
        """
        func: callable(url) -> result
        iterable: list of urls
        returns list of (url, result)
        """
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as exc:
            future_to_url = {exc.submit(self._wrap_call, func, url): url for url in iterable}
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    res = future.result()
                    results.append((url, res))
                except Exception as e:
                    log(f"[WORKER] Exception for {url}: {e}")
        return results

    def _wrap_call(self, func, url):
        # small politeness delay to avoid hammering target
        time.sleep(self.delay)
        return func(url)
