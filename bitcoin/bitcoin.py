import sys
import requests
import json

try:
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    x = data.json()
    q = x.get("bpi")
    m = q.get("USD")
    r = m.get("rate").replace(",", "")
    r = float(r)
    g = float(r) * float(sys.argv[1])
    print(f"${g:,.4f}")
except (ValueError, IndexError):
    sys.exit("not suitable")
