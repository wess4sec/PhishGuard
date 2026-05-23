# 🛡️ PhishGuard — Phishing Detection Engine 

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Security](https://img.shields.io/badge/Security-Phishing%20Detection-red.svg)
![SOC](https://img.shields.io/badge/SOC-Blue%20Team-blueviolet.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)
![Build](https://img.shields.io/badge/Build-Experimental-orange.svg)
![Architecture](https://img.shields.io/badge/Architecture-Modular-informational.svg)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)

---

## 📌 Overview

**PhishGuard** is a modular phishing detection engine designed for SOC-style analysis and blue-team detection engineering.

It identifies phishing infrastructure using rule-based security analysis across multiple attack vectors:

- URLs (structure, obfuscation, redirects)
- Unicode / homograph attacks
- Brand impersonation attempts
- Email header spoofing indicators
- Risk-based scoring system

This project simulates how real SOC analysts triage phishing threats in production environments.

---

## 🎯 Objectives

- Build a detection engineering pipeline in Python
- Simulate SOC phishing analysis workflows
- Detect malicious indicators using rule-based logic
- Generate structured risk scores and classifications
- Provide extensible architecture for threat intelligence integration

---

## ⚙️ Core Features

### 🔗 URL Analysis Engine
- Extract domain, subdomain, TLD, and path
- Detect nested domains (e.g. `google.com.evil.ru`)
- Identify obfuscated or suspicious URL structures
- Detect IP-based URLs
- Flag URL encoding abuse

---

### 🌐 Unicode / Homograph Detection
Detects:
- Punycode (`xn--`)
- Unicode spoofing
- Mixed-script domains (Latin + Cyrillic/Greek)

Example:
```
gοogle.com → Unicode spoofing attempt
```

---

### 🏷️ Brand Impersonation Detection
Targets:
- Google
- Microsoft
- PayPal
- GitHub
- Amazon
- LinkedIn

Methods:
- Keyword matching
- Fuzzy similarity scoring (Levenshtein-style)

---

### ⚖️ Risk Scoring Engine

| Signal                  | Score |
|------------------------|------:|
| Brand impersonation    | +30   |
| Unicode spoofing       | +40   |
| Nested domain abuse    | +25   |
| Suspicious TLD         | +20   |
| Excess subdomains      | +15   |
| Redirect indicators    | +25   |

### Classification
- 🟢 LOW (0–29)
- 🟡 MEDIUM (30–59)
- 🟠 HIGH (60–79)
- 🔴 CRITICAL (80–100)

---

### 📧 Email Header Analysis
Detects:
- SPF failures
- DKIM failures
- DMARC failures
- Sender mismatch
- Reply-To spoofing
- Suspicious relay paths

---

## 🧱 Project Structure

```
PhishGuard/
│
├── analyzer/
│   ├── url_analyzer.py
│   ├── unicode_detector.py
│   ├── brand_detector.py
│   ├── risk_scoring.py
│   ├── header_analyzer.py
│   └── reputation_checker.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone repo
```bash
git clone https://github.com/wess4sec/PhishGuard.git
cd PhishGuard
```

### Create environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 🧪 Example Output

```json
{
  "input": "google.com.evil.ru",
  "risk": {
    "score": 85,
    "level": "CRITICAL",
    "reasons": [
      "nested_domain",
      "brand_impersonation",
      "unicode_spoofing"
    ]
  }
}
```

---

## 🧠 Architecture

```
Input → Parsing → Detection Engines → Risk Scoring → JSON Output
```

---

## 🔐 Security Use Case

- SOC Tier 1 phishing triage
- Threat detection engineering pipeline
- IOC enrichment workflows
- Security automation for analysts

---

## 📈 Roadmap

- [ ] FastAPI REST API (/analyze)
- [ ] SOC dashboard UI
- [ ] Threat intel integrations (VirusTotal, URLHaus)
- [ ] SIEM logging support
- [ ] Docker deployment
- [ ] Real-time monitoring engine

---

## 👤 Author

**Oussama Zehri (OZX / 0xOZX)**  
penetration tester | SOC Analyst | Detection Engineering

---

## 📜 License

MIT License — free to use for learning and security research.
