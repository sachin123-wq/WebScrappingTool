import json
import os
from pathlib import Path
from models.products import Product

class DatabaseHandler:
    def __init__(self, storage_path: str = "scraped_data.json"):
        self.storage_path = Path(storage_path)
        if not self.storage_path.exists():
            self.storage_path.write_text("[]")  # Initialize with an empty list if file doesn't exist

    def load_data(self):
        try:
            # Ensure the file exists and is not empty
            if os.path.exists(self.storage_path) and os.path.getsize(self.storage_path) > 0:
                with open(self.storage_path, 'r') as f:
                    return json.load(f)  # Load the data as a list
            else:
                print(f"Warning: {self.storage_path} is empty or doesn't exist.")
                return []  # Return an empty list if file is empty or doesn't exist
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []  # Return empty list if JSON is malformed
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def save_data(self, products):
        # Ensure the data is saved as a list
        with self.storage_path.open("w") as f:
            json.dump(products, f, indent=4)

    def update_product(self, product: Product):
        data = self.load_data()  # Load current data from file
        print(product)
        for item in data:
            if item["product_title"] == product.product_title:
                if item["product_price"] != product.product_price:
                    item["product_price"] = product.product_price
                    item["path_to_image"] = product.path_to_image
                return False  # Return False if the product is updated
        # If product does not exist, append the new product
        dict_prod = vars(product)
        # print(dict_prod)
        data.append(dict_prod)
        self.save_data(data)  # Save the updated data back to the file
        return True  # Return True to indicate the product was added
