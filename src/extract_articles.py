import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Load input file
input_file = "../data/input.xlsx"
df = pd.read_excel(input_file)

# Create output directory
output_dir = "../output/articles"
os.makedirs(output_dir, exist_ok=True)

def extract_text(url, url_id):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title
        title = soup.find("h1").text.strip()

        # Extract article text
        paragraphs = soup.find_all("p")
        article_text = "\n".join(p.text.strip() for p in paragraphs)

        # Save as text file
        with open(f"{output_dir}/{url_id}.txt", "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{article_text}")

        print(f"Extracted: {url_id}.txt")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Loop through URLs
for _, row in df.iterrows():
    extract_text(row["URL"], row["URL_ID"])
    time.sleep(2)  # Prevents rate limiting
