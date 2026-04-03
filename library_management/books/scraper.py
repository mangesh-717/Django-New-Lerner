import requests
from bs4 import te
from urllib.parse import urljoin
from .models import Book
import re
import logging

logger = logging.getLogger('books')

BASE_URL = "http://books.toscrape.com/"

def scrape_books(category):
    # Step 1: Get all categories from homepage
    homepage = requests.get(BASE_URL)
    soup = BeautifulSoup(homepage.text, "html.parser")

    category_links = soup.select("div.side_categories ul li ul li a")

    category_url = None

    for link in category_links:
        name = link.text.strip()
        if name.lower() == category.name.lower():
            category_url = urljoin(BASE_URL, link["href"])
            break

    if not category_url:
        return  # category not found on site

    # Step 2: Scrape category pages (with pagination)
    while category_url:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")
        
        logger.info(f"Found {len(books)} books")

        for book in books:
            try:
                title = book.h3.a["title"]
    
                raw_price = book.find("p", class_="price_color").text.strip()
                price = float(re.sub(r"[^\d.]", "", raw_price))
    
                image_relative = book.find("img")["src"]
                image_url = urljoin(BASE_URL, image_relative)
    
                detail_relative = book.h3.a["href"]
                detail_url = urljoin(category_url, detail_relative)
    
                detail_response = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_response.text, "html.parser")
    
                description_tag = detail_soup.find("meta", attrs={"name": "description"})
                description = description_tag["content"].strip() if description_tag else "No description"
    
                # UPSERT (Update if exists, else create)
                Book.objects.update_or_create(
                    title=title,
                    category=category,
                    defaults={
                        "price": price,
                        "description": description,
                        "image_url": image_url,
                    }
                )

                logger.info(f"Saved book: {title}")

            except Exception as e:
                logger.error(f"Error processing book: {e}")
                continue
    
        # Pagination
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page = next_button.a["href"]
            category_url = urljoin(category_url, next_page)
        else:
            category_url = None