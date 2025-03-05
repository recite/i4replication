import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

# Base URL
base_url = "https://ideas.repec.org/p/zbw/i4rdps/{}.html"

# Open a CSV file to save the abstracts
with open('abstracts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['url', 'abstract'])

    # Iterate over the range of URLs
    for i in tqdm(range(1, 192), desc="Scraping abstracts"):
        url = base_url.format(i)
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            abstract_section = soup.find('div', id='abstract-body')

            if abstract_section:
                abstract = abstract_section.get_text(strip=True)
            else:
                abstract = "Abstract not found"

            # Write URL and abstract to CSV
            writer.writerow([url, abstract])
        else:
            print(f"Failed to retrieve {url}")
