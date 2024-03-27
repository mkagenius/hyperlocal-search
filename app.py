from flask import Flask, render_template, request
from zepto import fetch_zepto
from blinkit import fetch_blinkit
from instamart import fetch_instamart
from dmart import fetch_dmart
from concurrent.futures import ThreadPoolExecutor


app = Flask(__name__)


def fetch_products_in_parallel(query, location):
    with ThreadPoolExecutor() as executor:
        future_zepto = executor.submit(fetch_zepto, query, location)
        future_blinkit = executor.submit(fetch_blinkit, query, location)
        future_instamart = executor.submit(fetch_instamart, query, location)
        future_dmart = executor.submit(fetch_dmart, query)
        zepto_products = future_zepto.result() or []
        try:
            blinkit_products = future_blinkit.result() or []
        except Exception as e:
            blinkit_products = []
            print(e)
        instamart_products = future_instamart.result() or []
        dmart_products = future_dmart.result() or []
        
    return zepto_products, blinkit_products, instamart_products, dmart_products


@app.route('/')
def index():
    query = request.args.get('query', '')
    location = request.args.get('location', '')
    # Replace spaces with hyphens
    query = query.replace(' ', '-')
    if query:
        zepto_products, blinkit_products, instamart_products, dmart_products = fetch_products_in_parallel(query, location)
    else:
        zepto_products = blinkit_products = instamart_products = dmart_products = []
    return render_template('index.html', zepto_products=zepto_products, blinkit_products=blinkit_products, instamart_products=instamart_products, dmart_products=dmart_products)


if __name__ == "__main__":
    app.run(debug=True)
