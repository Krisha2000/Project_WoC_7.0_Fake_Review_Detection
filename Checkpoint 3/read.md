# Web Scraping Reviews Script

This Python script allows  to scrape product reviews from a given URL and save the details in a CSV file. The script collects reviewer names, ratings, review text, and the review date from the page, storing them in a structured format for further analysis.

## **Task Overview**

- **Task 1: Setting Up Environment**  
  Install the required libraries:
  - `requests` for making HTTP requests to fetch the HTML content of the product page.
  - `beautifulsoup4` for parsing the HTML and extracting the reviews.
  - `pandas` for storing and saving the scraped reviews in a CSV file.
  - `re` for regular expression matching to extract ratings from the reviews.

- **Task 2: Develop the Web Scraping Script**  
  This script will:
  - Take a product URL as input.
  - Scrape reviews including the review text, rating, reviewer name, and review date.
  - Handle cases where certain elements may not be found (e.g., no review text or rating).
  
- **Task 3: Saving the Results**  
  Once reviews are scraped, they will be stored in a CSV file named `Reviews.csv`.

- **Task 4: Automation & Reusability**  
  The script allows you to input any product URL and scrape the reviews dynamically, making it reusable for any product on the website.

## **Requirements**

To run the script, you need to have the following Python libraries installed:

```bash
pip install requests beautifulsoup4 pandas

