from model import Product
import json

zepto_list = [{
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/5f2ba4d7-98ff-4fdb-ba4d-4fa86e7ad1df.jpeg",
    "mrp": 125,
    "name": "Monster Energy Drink Ultra Can",
    "selling_price": 110,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/9f15ac0a-c3ec-4042-bd45-0f05047eb6b8.jpeg",
    "mrp": 125,
    "name": "Monster Energy Drink Can",
    "selling_price": 110,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/d7872792-f97c-4fe3-bf98-074cf623484d.jpeg",
    "mrp": 125,
    "name": "Red Bull Energy Drink Can",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/dbe3edc8-4b2a-4d8d-9020-2accb3c74574.jpeg",
    "mrp": 125,
    "name": "Red Bull Energy Drink Sugar Free",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/ee40f94d-9a37-467f-b12d-d099580f6ab4.jpeg",
    "mrp": 480,
    "name": "Red Bull Energy Drink Multican",
    "selling_price": 447,
    "variant": "4 X 250ML"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/e8d065ee-7932-4622-8d15-7b8154e84821.jpeg",
    "mrp": 700,
    "name": "Red Bull Energy Drink Multican",
    "selling_price": 623,
    "variant": "6 x 250ML"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/439b7463-0e7f-4875-9e35-8f1d164b4175.jpeg",
    "mrp": 165,
    "name": "Red Bull Energy Drink Can",
    "selling_price": 165,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/48583623-f5f5-4d92-844c-86ae6471256f.jpeg",
    "mrp": 125,
    "name": "Red Bull Energy Drink Yellow Edition Can",
    "selling_price": 125,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/inventory/product/2253b322-82a1-4ba5-b2ac-8c47903750f4-3825.jpg",
    "mrp": 250,
    "name": "Monster Energy Drink 350 ml Combo",
    "selling_price": 210,
    "variant": "350 ml X 2"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/inventory/product/d04ee745-2eae-465f-b5df-f99c8ce923f2-3826.jpg",
    "mrp": 500,
    "name": "Monster Energy Drink 350 ml Combo",
    "selling_price": 400,
    "variant": "350 ml X 4"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/a2f52222-0f68-4ccd-b47e-8ccda432bf1a1746.jpg",
    "mrp": 565,
    "name": "Red Bull Energy Drink(1l) & Dr. Cubes Ice Cubes(1kg) Combo",
    "selling_price": 527,
    "variant": "2 combo"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/3c510741-84af-418b-b59b-87856c0bf4d0.jpeg",
    "mrp": 629,
    "name": "Red Bull Energy Drink(1l) & Plastic Playing Cards Black Box Premium(1pc) Combo",
    "selling_price": 566,
    "variant": "2 combo"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/94ac75f7-9fab-45b8-a767-81ad14840598.jpeg",
    "mrp": 60,
    "name": "Hell Energy Drink - Classic Can",
    "selling_price": 60,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/9f15ac0a-c3ec-4042-bd45-0f05047eb6b8.jpeg",
    "mrp": 125,
    "name": "Monster Energy Drink Can",
    "selling_price": 110,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/b0d8175f-c1c2-4795-a28d-d27f51326073.jpeg",
    "mrp": 20,
    "name": "Sting Energy Drink Pet",
    "selling_price": 20,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://ik.imagekit.io/jupdt2k6txi/production/cms/product_variant/a621d248-968c-41bb-9d3c-df700045a902.jpeg",
    "mrp": 125,
    "name": "Red Bull Energy Drink The Winter Pomegranate Can",
    "selling_price": 125,
    "variant": "250 ml"
}]


def fetch_zepto(query="redbull", location="koramangala"):
    products = []
    for p_json in zepto_list:
        p = Product.fromJson(json.dumps(p_json))
        products.append(p)
    return products
