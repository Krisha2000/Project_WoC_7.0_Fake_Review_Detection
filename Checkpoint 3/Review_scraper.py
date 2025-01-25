# Task 1: Setting Up environment

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

# Task 2: Develop the Web Scraping Script

def scrape_reviews(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept-Language": "en-US, en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        
        reviews = []
        for review_block in soup.select('.review'):
            
            review_text = review_block.select_one('.review-text').get_text(strip=True) if review_block.select_one('.review-text') else 'N/A'
            
            
            rating_text = review_block.select_one('.review-rating').get_text(strip=True) if review_block.select_one('.review-rating') else 'N/A'
            rating = re.search(r'\d+\.?\d*', rating_text).group() if rating_text != 'N/A' else 'N/A'
            
            
            reviewer_name = review_block.select_one('.review-author').get_text(strip=True) if review_block.select_one('.review-author') else 'Anonymous'
            
           
            review_date = review_block.select_one('.review-date').get_text(strip=True) if review_block.select_one('.review-date') else 'N/A'
            
            reviews.append({
                "Reviewer Name": reviewer_name,
                "Rating": rating,
                "Review Text": review_text,
                "Review Date": review_date
            })
        
        
        if reviews:
            df = pd.DataFrame(reviews)
            output_file = "Reviews.csv"
            df.to_csv(output_file, index=False)
            print(f"Reviews saved to {output_file}")
        else:
            print("No reviews found on the page.")

    except Exception as e:
        print(f"An error occurred: {e}")


product_url = input("Enter the product URL: ")
scrape_reviews(product_url)


# Task 3: Saviing the Results
# The script automatically saves the scraped reviews into a file named Reviews.csv.


# Task 4: Automation & Reusability
# The script accepts any product URL as input, making it dynamic and reusable for multiple products.
