# 🛡️ Directory Traversal Demo (For Education Only)

This project demonstrates how insecure file path handling in web applications can lead to directory traversal vulnerabilities.

## ⚠️ WARNING
This is an intentionally vulnerable demo. Do **not** use this in production environments.

## 💡 What It Shows
- How attackers can use `../` sequences to access sensitive files
- Why input sanitization and safe path handling are critical

## 🛠 How to Run
```bash
pip install flask
python app.py

## 💣 Vulnerable Version
Here's what a directory traversal attack looks like:

![Directory Traversal Example](C:\..\..\..\images)

## 🔐 Secure Version
Here's what a directory traversal attack looks like being blocked:

![Secure Example](images/secure-example.png)