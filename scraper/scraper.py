from bs4 import BeautifulSoup # HTML and XML parsing library for extracting data from web pages
from models.products import Product # Custom-defined Pydantic model to represent a product's details
from models.settings import ScrapeSettings # Custom-defined Pydantic model for scraper settings like max_pages and proxy

import requests # HTTP library for sending web requests
from pathlib import Path # File system library for managing and manipulating file paths
from tenacity import retry, stop_after_attempt, wait_fixed # Library for implementing retry logic with customizable conditions

class Scraper:
    def __init__(self, settings: ScrapeSettings):
        self.settings = settings
        self.base_url = "https://dentalstall.com/shop/"
        self.headers = {"User-Agent": "Mozilla/5.0"}
    
    # Fetch_page method
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def fetch_page(self, page_number: int) -> BeautifulSoup:
        url = f"{self.base_url}?page={page_number}"  # Constructs the URL for a specific page
        proxies = {"http": self.settings.proxy, "https": self.settings.proxy} if self.settings.proxy else None
        response = requests.get(url, headers=self.headers, proxies=proxies)  # Makes an HTTP GET request
        print(response)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return BeautifulSoup(response.text, "html.parser")  # Parses the page's HTML content
    
    def scrape(self):
        products = []  # List to store all the scraped product details
        page = 1  # Start scraping from the first page
        print("Scrapping in progress....")
        while True:
            if self.settings.max_pages and page > self.settings.max_pages:
                break  # Stop scraping if the maximum page limit is reached

            soup = self.fetch_page(page)  # Fetch and parse the page's content
            
            product_cards = soup.select(".product-inner")  # Locate all product cards on the page
            print(len(product_cards))
            if not product_cards:
                break  # Stop if no product cards are found (e.g., end of catalogue)

            for card in product_cards:
                # Extract product details
                title = card.select_one(".woo-loop-product__title").get_text(strip=True)
                # print(title)
                price = float(card.select_one(".woocommerce-Price-amount").select_one("bdi").get_text(strip=True).replace("₹", ""))
                # print(price)
                image_url = card.select_one(".mf-product-thumbnail").select_one("img")["src"]
                # print(image_url)
                image_path = self.download_image(image_url, title)  # Download and save the product's image
                # print(image_path)
                # Create a Product object and add it to the list
                products.append(Product(product_title=title, product_price=price, path_to_image=image_path))
            page += 1  # Move to the next page
        return products  # Return all scraped products
    
    def download_image(self, url: str, title: str) -> str:
        response = requests.get(url, stream=True)  # Sends a GET request to the image URL
        image_path = Path(f"images/{title}.jpg")  # Constructs a local path for the image
        image_path.parent.mkdir(exist_ok=True, parents=True)  # Creates the images directory if it doesn't exist
        with image_path.open("wb") as f:
            f.write(response.content)  # Writes the image content to the file
        return str(image_path)  # Returns the image's local path
        