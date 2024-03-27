import json
from model import Product

dmart_list = [{
    "deeplink": "",
    "image": "https://cdn.dmart.in/images/products/APR130000041xx21APR23_5_P.jpg",
    "mrp": "480.00",
    "name": "Red Bull Energy Drink Pack : 4x250 ml",
    "selling_price": "430.00",
    "variant": "4x250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.dmart.in/images/products/APR130001518xx21APR23_5_P.jpg",
    "mrp": "700.00",
    "name": "Red Bull Energy Drink Pack : 6x250 ml",
    "selling_price": "599.00",
    "variant": "6x250 ml"
}]


def fetch_dmart(query="redbull"):
    products = []
    for p_json in dmart_list:
        p = Product.fromJson(json.dumps(p_json))
        products.append(p)
    return products
