# utils/analyzer.py

def analyze_response(resp):
    """
    Basic content analyzer:
    - mendeteksi error SQL
    - mendeteksi potensi XSS
    - mendeteksi kebocoran informasi
    """

    text = resp.text.lower()
    findings = []

    # --- SQL ERROR DETECTION ---
    sql_errors = [
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark",
        "sqlstate",
        "unknown column",
        "mysql_fetch",
        "syntax error",
        "pg_query",
        "oracle error"
    ]

    for err in sql_errors:
        if err in text:
            findings.append(f"Possible SQL Injection Error Detected: '{err}'")

    # --- XSS INDICATION ---
    if "<script>" in text:
        findings.append("Possible reflected XSS: <script> found in response")

    # --- Sensitive info ---
    sensitive_keywords = [
        "password",
        "api_key",
        "secret_key",
        "token",
        "private key",
        "credentials",
        "authorization",
        "jwt"
    ]

    for key in sensitive_keywords:
        if key in text:
            findings.append(f"Potential sensitive data exposed: {key}")

    # --- SERVER INFO ---
    server_header = resp.headers.get("Server")
    if server_header:
        findings.append(f"Server Header: {server_header}")

    return findings if len(findings) > 0 else None
