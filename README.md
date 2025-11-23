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
    |
    ├── utils/
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
    ├── main.py
    ├── main_menu.py
    ├── requirements.txt

------------------------------------------------------------------------

## 🛠️ Instalasi

### 1. Clone Repository

``` bash
git clone https://github.com/username/project-ai-python.git
cd project-ai-python
```

### 2. Buat Virtual Environment

``` bash
python -m venv venv
venv/Scripts/activate       # Windows
source venv/bin/activate    # Linux/macOS
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

## ▶️ Cara Menjalankan

``` bash
python main.py
```

atau bila menggunakan menu:

``` bash
python main_menu.py
```

## ⚙️ Konfigurasi

Jika proyek menggunakan file konfigurasi:

    config/
    │── settings.json
    │── model_config.yaml

Sesuaikan API key, path dataset, serta parameter model sesuai kebutuhan.

## 📦 Dependencies Utama

-   Python 3.10+
-   TensorFlow / PyTorch
-   NumPy
-   Pandas
-   Scikit-learn
-   OpenAI / LangChain
-   Rich

## 🧪 Testing

``` bash
- Mauskan Url Target
- Pilih Menu Agent 1-5
- Proses 
- Report dalam bentuk JSON & Txt
```

## 🤝 Kontribusi

1.  Fork repository\
2.  Buat branch baru\
3.  Commit & push\
4.  Buat Pull Request

## 📧 Kontak

**Email:** mediamulti049@gmail.com\

------------------------------------------------------------------------

## 📝 Lisensi

Proyek ini bebas digunakan untuk pembelajaran & riset penetration
testing.
