# Get bitcoin price in USD

import json
import requests


def get_price():
    """Get bitcoin price in USD."""
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    data = json.loads(response.text)
    price = data['bpi']['USD']['rate']
    return price


print(get_price())
