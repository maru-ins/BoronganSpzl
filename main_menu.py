from core.agent import AutoPentestAgent
from utils.logger import log
import time

def main_menu():
    print("==========================")
    print("=== AUTO PENTEST AGENT ===")
    print("===       By.Pnjl      ===")
    print("==========================")
    print("\n1. Crawl target")
    print("2. Scan target (basic scan)")
    print("3. Full AutoPentest (crawl + scan + fuzz)")
    print("4. Export report manual")
    print("5. Keluar")

    choice = input("Pilih menu Cok (1-5) : ")
    return choice


def run():
    target = input("Masukkan target URL (contoh: http://127.0.0.1:8080): ")

    # Buat agent
    agent = AutoPentestAgent(
        target=target,
        max_workers=6,
        delay=0.3
    )

    while True:
        menu = main_menu()

        if menu == "1":
            log("[MENU] Crawling dimulai...")
            urls = agent.crawler.crawl()
            print(f"[+] Total halaman ditemukan: {len(urls)}")

        elif menu == "2":
            log("[MENU] Basic scanning dimulai...")
            urls = agent.crawler.crawl()
            for url in urls:
                agent.scanner.scan_url_basic(url)
            print("[+] Basic scan selesai")

        elif menu == "3":
            log("[MENU] Full AutoPentest dimulai...")
            agent.run()
            print("[+] Full AutoPentest selesai")

        elif menu == "4":
            log("[MENU] Export report manual...")
            agent.report.export()
            print("[+] Report diexport")

        elif menu == "5":
            print("Keluar...")
            time.sleep(1)
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    run()