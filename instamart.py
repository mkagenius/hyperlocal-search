from model import Product
import json

instamart_list = [{
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/369345aedec4b90b15699e2d3537c50c",
    "mrp": 750,
    "name": "Red Bull Energy Drink",
    "selling_price": 637,
    "variant": "6 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/09e6ad8a2dbce62aea4df2321b4c93b6",
    "mrp": 500,
    "name": "Red Bull Energy Drink",
    "selling_price": 435,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/9d040d1960b9b782ffd48a8f364a3b23",
    "mrp": 125,
    "name": "Red Bull Energy Drink",
    "selling_price": 112,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/a0d043a3cc64d556c22052a41b82a7bb",
    "mrp": 60,
    "name": "Hustle Energy Drink",
    "selling_price": 60,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/aecfd3ad12cbef96573fff4729753ba9",
    "mrp": 750,
    "name": "Red Bull The Yellow Edition Energy Drink",
    "selling_price": 705,
    "variant": "6 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/5512844387bdb56ae3925f85361e7149",
    "mrp": 500,
    "name": "Red Bull The Yellow Edition Energy Drink",
    "selling_price": 380,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/lzw54mi0rlikuux6iy3z",
    "mrp": 125,
    "name": "Red Bull The Yellow Edition Energy Drink",
    "selling_price": 99,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/ad1bd8617880477e5c4f383a9bd60fa8",
    "mrp": 750,
    "name": "Red Bull Sugar Free Energy Drink",
    "selling_price": 637,
    "variant": "6 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/8532bb6e5235eb28b02d8095cecccad5",
    "mrp": 500,
    "name": "Red Bull Sugar Free Energy Drink",
    "selling_price": 435,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/rm0mu7ig8gq0cesfmjie",
    "mrp": 125,
    "name": "Red Bull Sugar Free Energy Drink",
    "selling_price": 112,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/3d3ae9c08451f653c0c7165e8f0a1e10",
    "mrp": 660,
    "name": "Red Bull Energy Drink",
    "selling_price": 614,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/77fffda7ba05c449caa1276c35652cb9",
    "mrp": 330,
    "name": "Red Bull Energy Drink",
    "selling_price": 294,
    "variant": "2 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/wz11qw4zqtdrilk7v2rp",
    "mrp": 165,
    "name": "Red Bull Energy Drink",
    "selling_price": 148,
    "variant": "350 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/994919d31388e9be3bb67485a24ec2a7",
    "mrp": 1920,
    "name": "Red Bull Energy Drink Multipack 250ml",
    "selling_price": 1594,
    "variant": "16 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/3d0122a6c24e42a61e848b2c7e2c7560",
    "mrp": 960,
    "name": "Red Bull Energy Drink Multipack 250ml",
    "selling_price": 883,
    "variant": "8 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/392920a81af71929fbab7a8f2088b70b",
    "mrp": 480,
    "name": "Red Bull Energy Drink Multipack 250ml",
    "selling_price": 446,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/8e5db792f4d78cf22710f0975a842167",
    "mrp": 490,
    "name": "Red Bull Energy Drink Can Pack of 2",
    "selling_price": 465,
    "variant": "2 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/psmty7vitvflijm5ifuw",
    "mrp": 245,
    "name": "Red Bull Energy Drink Can Pack of 2",
    "selling_price": 235,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/d3f2d3ed94500735815c286f599daa05",
    "mrp": 175,
    "name": "Red Bull Plus",
    "selling_price": 175,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/6869679f8e2c82551168b72091cf756b",
    "mrp": 960,
    "name": "Red Bull Energy Drink Multipack",
    "selling_price": 845,
    "variant": "2 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/c3342763a7275f2cc9366a03865ac1ee",
    "mrp": 175,
    "name": "Red Bull Energy Drink & Snickers Peanut Chocolate Bar ",
    "selling_price": 175,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/a105dcd973b0603c4028bfd08854820c",
    "mrp": 1500,
    "name": "Red Bull Energy Drink",
    "selling_price": 1185,
    "variant": "12 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/2bc5f2eabde5c42986e365ce3c9a1691",
    "mrp": 1500,
    "name": "Red Bull Energy Drink & Red Bull Sugarfree Energy Drink Combo",
    "selling_price": 1290,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/102e722d2d92a2bcf2326133ff1c111f",
    "mrp": 145,
    "name": "Red Bull Energy Drink & Bingo Mad Angles Tomato Madness Combo",
    "selling_price": 145,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/9b8e13aac54ccec9d99cdb6b23ebd863",
    "mrp": 145,
    "name": "Red Bull Energy Drink & Bingo Mad Angles Achari Masti Combo",
    "selling_price": 145,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/1e2ab707d7fd8dbe95ea5e9ce76b8798",
    "mrp": 145,
    "name": "Red Bull Energy Drink & Bingo Potato Chips Original Style Red Chilli Sprinkled Combo",
    "selling_price": 145,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/cb3842fb96d983aef2e1ada646899c59",
    "mrp": 215,
    "name": "Yoga Bar Multigrain Energy Bars Chocolate Chunk Nut & Red Bull Energy Drink",
    "selling_price": 211,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/e0eb04fef779887b3ef34b73d5c01aa9",
    "mrp": 240,
    "name": "Red Bull Energy Drink & Pringles Sour Cream & Onion Flavour Potato Crips Combo",
    "selling_price": 216,
    "variant": "1 combo"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/d11a7bf9d4c677b2d560f93d02cca21e",
    "mrp": 500,
    "name": "Red Bull Energy Drink Watermelon The Red Edition",
    "selling_price": 450,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/cqnp5ubt30tgx7zaynzl",
    "mrp": 125,
    "name": "Red Bull Energy Drink Watermelon The Red Edition",
    "selling_price": 99,
    "variant": "250 ml"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/e3d73cc2191fbc30fca1e4cd32393568",
    "mrp": 2800,
    "name": "Red Bull Energy Drink",
    "selling_price": 2324,
    "variant": "4 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/0c3c6581953f9947fc1fb6fef6309ec6",
    "mrp": 1400,
    "name": "Red Bull Energy Drink",
    "selling_price": 1190,
    "variant": "2 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/874ee98957c0ceed19757a1a72bc5b2e",
    "mrp": 700,
    "name": "Red Bull Energy Drink",
    "selling_price": 623,
    "variant": "6 pieces"
},
    {
    "deeplink": "",
    "image": "https://instamart-media-assets.swiggy.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,h_96,w_96/r4thxy6p0ba6hncsw94k",
    "mrp": 1180,
    "name": "Red Bull Energy Drinks Combo",
    "selling_price": 1015,
    "variant": "1 combo"
}]


def fetch_instamart(query="redbull", location="koramangala"):
    products = []
    for p_json in instamart_list:
        p = Product.fromJson(json.dumps(p_json))
        products.append(p)
    return products
