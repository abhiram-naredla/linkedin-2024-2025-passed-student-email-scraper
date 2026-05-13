<<<<<<< HEAD
# LinkedIn Student Scraper (Graduation 2024-2025)

A professional-grade Python automation tool using **Selenium** to find and extract student profile data for specific graduation years.

## 🚀 Features
- **Automated Login**: Securely logs into LinkedIn using environment variables.
- **Advanced Filtering**: Targets graduating students (2024-2025) via search queries.
- **Detailed Extraction**: Captures Name, URL, College, Graduation Year, and Contact Info (if public).
- **Anti-Blocking Measures**: Uses randomized delays, custom user-agents, and non-headless bypasses.
- **Data persistence**: Automatically saves results to CSV in the `data/` directory.
- **Robust Logging**: Detailed logs found in `logs/app.log`.

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- **Python 3.8+** installed.
- **Google Chrome** browser installed.

### 2. Installation
Clone this repository or download the files, then run:
```bash
pip install -r requirements.txt
```

### 3. Configuration
1. Rename `.env.example` to `.env`.
2. Fill in your LinkedIn credentials:
   ```env
   LINKEDIN_EMAIL="your_email@gmail.com"
   LINKEDIN_PASSWORD="your_password"
   ```
3. Adjust scraping limits and years in `.env` if needed.

---

## 🏃 Launching the Scraper

To start the automated process:
```bash
python main.py
```

### Output Location
- Scraped data: `data/output.csv` (and timestamped versions).
- Activity logs: `logs/app.log`.

---

## 🛡️ LinkedIn Blocking & Common Errors

LinkedIn has aggressive bot detection. To ensure your account stays safe:

### 💡 Tips to Avoid Blocking:
1. **Reduce Speed**: The script uses random delays. Increase `MAX_PROFILES` gradually. Do not scrape 1000s of profiles in one go.
2. **Use Real Browser Info**: Running with `HEADLESS=false` in `.env` is safer as it behaves more like a real user.
3. **Account Age**: Use an established LinkedIn account. Fresh accounts are flagged much faster.
4. **Solve CAPTCHAs**: If the script stops at a "security checkpoint," the browser will remain open. Solve the CAPTCHA manually in that window, and the script might be able to continue (though login usually fails if CAPTCHA is triggered initially).

### ❌ Common Errors:
- **`TimeoutException`**: Usually means the page took too long to load or Chrome crashed. Check your internet connection.
- **`NoSuchElementException`**: LinkedIn updated their UI/HTML structure. Contact me for an update to the selectors.
- **`Login Failed`**: Double check your credentials and ensure you don't have 2FA (Two-Factor Authentication) enabled, as it blocks automation.

---

## 📂 Project Structure
```text
project/
├── main.py              # Entry point
├── linkedin_login.py    # Driver setup & Login logic
├── scraper.py           # Searching & Profile extraction
├── requirements.txt     # Python dependencies
├── README.md            # You are here
├── .env.example         # Environment template
├── data/                # CSV outputs
└── logs/                # Runtime logs
```

---
**Disclaimer**: This tool is for educational purposes only. Scraping LinkedIn might violate their Terms of Service. Use at your own risk.
=======
# linkedin-2024-2025-passed-student-email-scraper
edit your linkedin email and password in env file to login.
# Student Scraper

A Python project to scrape LinkedIn student profiles.

## Features
- Selenium automation
- CSV export
- Login support

## Run
```bash
python main.py
>>>>>>> 2693c965706cf25ed92525a8ec325ed6a39f27bc
