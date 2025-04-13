import requests
from bs4 import BeautifulSoup
import time


def scrape_website(url, material):
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/115.0 Safari/537.36'
        )
    }
    results = []

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code != 200:
            print(f"Failed to fetch page, status code: {r.status_code}")
            return results

        soup = BeautifulSoup(r.text, 'html.parser')

        # Find product links
        product_links = soup.find_all(
            'a', {'class': 'a-link-normal s-no-outline'}
        )
        product_urls = [
            'https://www.amazon.in' + link['href']
            for link in product_links
        ]

        # limit to first 15 products to avoid getting blocked
        for product_url in product_urls[:15]:
            time.sleep(3)  # polite delay

            product_page = requests.get(
                product_url, headers=headers, timeout=10
            )
            if product_page.status_code != 200:
                continue

            product_soup = BeautifulSoup(product_page.text, 'html.parser')

            # Find the specifications table
            details = product_soup.find(
                'table', {'id': 'productDetails_techSpec_section_1'}
            )
            if not details:
                details = product_soup.find(
                    'div', {'id': 'detailBullets_feature_div'}
                )
            material_found = None

            if details:
                text = details.get_text(separator=' ').lower()
                if material.lower() in text:
                    material_found = True

            if material_found:
                # Get product title
                title = product_soup.find('span', {'id': 'productTitle'})
                title_text = title.get_text().strip() if title else 'No Title'

                results.append({
                    'company': 'Amazon',
                    'product': title_text[:100],
                    'email': 'N/A'  # No email on Amazon
                })

    except Exception as e:
        print(f"Error scraping website: {e}")

    return results
