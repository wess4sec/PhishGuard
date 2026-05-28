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

PhishGuard is a phishing detection engine I built for SOC-style analysis and blue team work. It's rule-based, modular, and covers the most common phishing tricks I kept seeing in the wild — sketchy URLs, Unicode spoofing, brand impersonation, and email header abuse.

The idea is pretty simple: you feed it a URL or email headers, it tears them apart, scores the risk, and tells you what's suspicious and why. No ML black boxes, just transparent detection logic you can actually read and extend.

---

## 🎯 Why I built this

I wanted to understand how phishing triage actually works at the analyst level, not just conceptually. So I built the detection pipeline myself — parsing, signal extraction, scoring, classification — the whole thing. It's also a good base if you want to bolt on threat intel feeds later.

---

## ⚙️ What it detects

### 🔗 URLs
- Pulls apart the domain, subdomain, TLD, and path
- Catches nested domain tricks like `google.com.evil.ru`
- Flags IP-based URLs and URL encoding abuse
- Spots redirect chains

### 🌐 Unicode / Homograph attacks
Domains that look legit but aren't:
- Punycode (`xn--`) domains
- Mixed-script domains (Latin + Cyrillic, etc.)
- Example: `gοogle.com` — that `ο` is Greek, not Latin

### 🏷️ Brand impersonation
Checks against: Google, Microsoft, PayPal, GitHub, Amazon, LinkedIn

Uses keyword matching + fuzzy similarity so it catches typosquats too, not just exact matches.

### ⚖️ Risk Scoring

| Signal | Score |
|---|---:|
| Brand impersonation | +30 |
| Unicode spoofing | +40 |
| Nested domain abuse | +25 |
| Suspicious TLD | +20 |
| Excess subdomains | +15 |
| Redirect indicators | +25 |

**Risk levels:**
- 🟢 LOW (0–29)
- 🟡 MEDIUM (30–59)
- 🟠 HIGH (60–79)
- 🔴 CRITICAL (80–100)

### 📧 Email headers
Looks for the usual signs of spoofing:
- SPF / DKIM / DMARC failures
- From/Reply-To mismatch
- Weird relay paths

---

## 🧱 Structure

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

## 🚀 Setup

```bash
git clone https://github.com/wess4sec/PhishGuard.git
cd PhishGuard

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

---

## ▶️ Run it

```bash
python main.py
```

---

## 🧪 Sample output

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

## 🧠 How it works

```
Input → Parsing → Detection Engines → Risk Scoring → JSON Output
```

Nothing fancy. Each analyzer runs independently and contributes signals to a shared score. Easy to add new detectors without breaking anything.

---

## 🔐 Where this fits

Good for:
- SOC Tier 1 phishing triage
- Building and testing detection rules
- IOC enrichment
- Learning how phishing infrastructure actually works

---

## 📈 What's next

- [ ] FastAPI endpoint (`/analyze`)
- [ ] Simple SOC dashboard
- [ ] VirusTotal + URLHaus integration
- [ ] SIEM log output
- [ ] Docker support
- [ ] Real-time monitoring

---

## 👤 Author

**Oussama Zehri (OZX / 0xOZX)**  
Pentester, SOC analyst, detection engineering enthusiast.

---

## 📜 License

MIT — use it, break it, learn from it.
