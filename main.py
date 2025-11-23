# main.py
import argparse
from core.agent import AutoPentestAgent
from utils.logger import log
import warnings
warnings.filterwarnings("ignore")

def parse_args():
    p = argparse.ArgumentParser(description="AutoPentestAgent (lab only)")
    p.add_argument("target", help="Target base URL (http://127.0.0.1:8080)")
    p.add_argument("--workers", type=int, default=6, help="Max concurrent worker threads")
    p.add_argument("--delay", type=float, default=0.3, help="Delay between requests (seconds)")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()

    agent = AutoPentestAgent(
        target=args.target,
        max_workers=args.workers,
        delay=args.delay
    )

    agent.run()
    log("Selesai. Periksa file report_*.json / report_*.txt")
