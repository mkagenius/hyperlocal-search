# import requests
from model import Product
import json

blinkit_list = [{

    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/403174a.jpg?ts=1688470763",
    "mrp": 125,
    "name": "Monster Energy Drink",
    "selling_price": 93,
    "variant": "350 ml"
},

    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_416160.jpg?ts=1710346837",
    "mrp": 500,
    "name": "Monster Energy Drink (Can) - Pack of 4",
    "selling_price": 367,
    "variant": "4x350 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/assets/products/sliding_images/jpeg/2217f2ec-4dc7-47ec-b67c-65fe1b848db4.jpg?ts=1707312716",
    "mrp": 125,
    "name": "Red Bull Energy Drink (250 ml)",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/267800a.jpg?ts=1688443508",
    "mrp": 125,
    "name": "Red Bull Energy Drink (Yellow Edition Tropical)",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_416159.jpg?ts=1710346836",
    "mrp": 250,
    "name": "Red Bull Energy Drink (2 x 250 ml) - Pack of 2",
    "selling_price": 240,
    "variant": "2x250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/432768a.jpg?ts=1688444558",
    "mrp": 125,
    "name": "Monster Zero Sugar Ultra Energy Drink",
    "selling_price": 93,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_528337.jpg?ts=1710344054",
    "mrp": 500,
    "name": "Monster Zero Sugar Ultra Energy Drink - Pack of 4",
    "selling_price": 367,
    "variant": "4 x 350 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/assets/products/sliding_images/jpeg/05757bda-c037-4d7f-a0e8-24432ce32a29.jpg?ts=1708592508",
    "mrp": 480,
    "name": "Red Bull Energy Drink (4 x 250 ml)",
    "selling_price": 430,
    "variant": "4x250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_487823.jpg?ts=1710347468",
    "mrp": 960,
    "name": "Red Bull Energy Drink (4 x 250 ml) - Pack of 2",
    "selling_price": 845,
    "variant": "2 x (4 x 250 ml)"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/534157a.jpg",
    "mrp": 125,
    "name": "Red Bull The Winter Edition Energy Drink (Pomegranate)",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_536241.jpg?ts=1710350817",
    "mrp": 500,
    "name": "Red Bull The Winter Edition Energy Drink (Pomegranate) - Pack of 4",
    "selling_price": 450,
    "variant": "4 x 250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_536242.jpg?ts=1710350817",
    "mrp": 500,
    "name": "Red Bull The Red Edition Energy Drink - Pack of 4",
    "selling_price": 450,
    "variant": "4 x 250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/479532a.jpg?ts=1686564691",
    "mrp": 125,
    "name": "Red Bull The Red Edition Energy Drink",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/sliding_image/496467a.jpg?ts=1709898205",
    "mrp": 295,
    "name": "Fast&Up Reload Energy Drink Electrolyte (Lime & Lemon Flavour)",
    "selling_price": 259,
    "variant": "20 tablets"
},
    {
    "deeplink": "",
    "image": "https://cdn.grofers.com/app/images/products/full_screen/pro_538176.jpg?ts=1710350825",
    "mrp": 375,
    "name": "Red Bull Energy Drink (Yellow Edition Tropical) + Red Bull The Red Edition Energy Drink + Red Bull The Winter Edition Energy Drink (Pomegranate) Combo",
    "selling_price": 330,
    "variant": None
}
]


def fetch_blinkit(query="redbull", location="koramangala"):
    products = []
    for p_json in blinkit_list:
        p = Product.fromJson(json.dumps(p_json))
        products.append(p)
    return products
