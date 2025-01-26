# Checkpoint-3

## Overview

This Python script scrapes reviews from a given product URL, extracting reviewer name, rating, review text, and date. The data is saved as a CSV file for analysis.

---

## Process

1. **Environment Setup**: Import libraries for HTTP requests (requests), HTML parsing (BeautifulSoup), and data handling (pandas).
2. **Send Request**: Use requests to fetch HTML content, mimicking a browser.
3. **Parse HTML**: Use BeautifulSoup to locate review details (text, rating, name, date).
4. **Save Data**: Store reviews in a DataFrame and save as Reviews.csv.
5. **Reusable Script**: Accepts any product URL as input.

---

## Libraries Used

- **requests**: For HTTP requests (pip install requests).
- **BeautifulSoup**: For HTML parsing (pip install beautifulsoup4).
- **pandas**: For handling data (pip install pandas).

---



## Notes

- Includes error handling for invalid URLs or network issues.
- Works for static HTML structures; dynamic pages may need Selenium.
- Ensure compliance with website terms of service when scraping.
- **This CSV file is the result of scraping reviews from the product link**: [MELOGAGA Bluetooth Wireless Cordless Rechargeable Mouse](https://www.amazon.com/MELOGAGA-Bluetooth-Wireless-Cordless-Rechargeable/dp/B0DK7SPK6T/ref=sr_1_5?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.gfAyBOD1LGYUxsD6p4bPCxpYVW8cP5sZ12qMIUi5XcERzhBLQyTsh-ruobn6jM2jEalRrpLsABaNZYjjK-hIbmzWXprYRpGhson-GaUZxgYup4rrezVICBYHChhPSyMwVXiTl0AHT77rIt_8P4SnzyzuNRCC62-59wQ_COpqp3lx62dKLFgWvFKkXFHmUfkAOuITng6pzQIhzfOd0uJuUOssoCJ1r-K-SUUPzw_IJ_A.ye3NxRxK5HkBa1lCFdeojsO6WwQHAOYMTl0V-KvFm9k&dib_tag=se&keywords=gaming%2Bmouse&pd_rd_r=5ae0299e-79d9-4b94-8f7d-59ba69463838&pd_rd_w=eETzR&pd_rd_wg=GkH85&qid=1737777955&sr=8-5&th=1).

---

