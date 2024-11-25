import redis
from models.products import Product

class Cache:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def is_price_cached(self, product: Product) -> bool:
        cached_price = self.redis_client.get(f"product:{product.product_title}")
        return cached_price and float(cached_price) == product.product_price

    def cache_product_price(self, product: Product):
        self.redis_client.set(f"product:{product.product_title}", product.product_price)
