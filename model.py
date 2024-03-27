import json


class Product:
    def __init__(self, name="-", image="", deeplink="", mrp=None, selling_price=None, variant=""):
        self.name = name
        self.image = image
        self.deeplink = deeplink
        self.mrp = mrp
        self.selling_price = selling_price
        self.variant = variant

    def __str__(self):
        # Create a dictionary representing the product's data
        product_dict = {
            "name": self.name,
            "image": self.image,
            "deeplink": self.deeplink,
            "mrp": self.mrp,
            "selling_price": self.selling_price,
            "variant": self.variant
        }
        # Convert the dictionary to a JSON string
        # Ensure ASCII is False to properly display characters, and sort_keys=True for consistent ordering
        return json.dumps(product_dict, ensure_ascii=False, indent=2, sort_keys=True)

    @classmethod
    def fromJson(cls, json_str):
        # Parse the JSON string into a Python dictionary
        product_data = json.loads(json_str)
        # Create a new Product instance using the dictionary
        return cls(**product_data)
