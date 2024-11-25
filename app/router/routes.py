from fastapi import APIRouter, Depends
from app.dependencies import authenticate
from scraper.scraper import Scraper
from scraper.database_handler import DatabaseHandler
from scraper.notifier import ConsoleNotifier
from scraper.cache import Cache
from models.settings import ScrapeSettings

router = APIRouter()

@router.post("/scrape")
def scrape(settings: ScrapeSettings, _: str = Depends(authenticate)):
    scraper = Scraper(settings)
    db_handler = DatabaseHandler()
    notifier = ConsoleNotifier()
    cache = Cache()

    products = scraper.scrape()
    # print(products)
    added_count = 0

    for product in products:
        # Cache check
        if cache.is_price_cached(product):
            continue

        # Update DB and Cache
        # print(product)
        if db_handler.update_product(product):
            added_count += 1
        cache.cache_product_price(product)

    notifier.notify(f"Scraping complete. {added_count} products added/updated.")
    return {"message": f"Scraping complete. {added_count} products added/updated."}
