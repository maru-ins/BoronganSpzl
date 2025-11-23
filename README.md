# AutoPentest Agent -- Python

## 🧠 Overview

AutoPentest adalah project Python yang dirancang untuk melakukan otomasi
proses penetration testing secara modular.\
Aplikasi ini dapat melakukan crawling, scanning, fuzzing, serta
menghasilkan laporan dalam format JSON secara otomatis.

Tujuan dari project ini adalah membantu proses pentesting manual agar
lebih efisien, terstruktur, dan cepat.

------------------------------------------------------------------------

## 🚀 Fitur Utama

-   Crawling otomatis untuk menemukan endpoint tersembunyi.
-   Basic vulnerability scanning (IFL, SQL Injection, XSS, dsb).
-   Fuzzing payload otomatis berdasarkan file pada folder `data/`.
-   Generator laporan otomatis (JSON).
-   CLI menu interaktif.
-   Modular architecture --- mudah dikembangkan.
-   Logging, parser, HTTP client, analyzer terpisah dan rapi.

------------------------------------------------------------------------

## 📂 Struktur Folder

    AutoPentest/
    │
    ├── core/
    │   ├── agent.py
    │   ├── analyzer.py
    │   ├── crawler.py
    │   ├── scanner.py
    │   ├── fuzzer.py
    │   ├── utils/
    │       ├── http_client.py
    │       ├── logger.py
    │       ├── parser.py
    │       ├── reporter.py
    │
    ├── data/
    │   ├── payloads/
    │   ├── wordlists/
    │
    ├── reports/
    │   ├── hasil_scan.json
    │
    ├── main_menu.py
    ├── requirements.txt

------------------------------------------------------------------------

## 🔧 Cara Menjalankan

### 1. Clone Repository

    git clone https://github.com/username/AutoPentest.git
    cd AutoPentest

### 2. Buat Virtual Environment

    python -m venv venv
    venv/Scripts/activate  # Windows
    source venv/bin/activate  # Linux

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Jalankan Program

    python main_menu.py

------------------------------------------------------------------------

## 📝 Lisensi

Proyek ini bebas digunakan untuk pembelajaran & riset penetration
testing.
