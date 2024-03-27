from instamart import fetch_instamart
from blinkit import fetch_blinkit
from zepto import fetch_zepto
from dmart import fetch_dmart

res = fetch_blinkit("redbull")

for p in res:
    print(f"{p},")


print("==================")

res = fetch_instamart("redbull")

for p in res:
    print(f"{p},")

print("==================")

res = fetch_zepto("redbull")

for p in res:
    print(f"{p},")


print("==================")

res = fetch_dmart("redbull")

for p in res:
    print(f"{p},")

