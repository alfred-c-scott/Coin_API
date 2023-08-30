# Coin_API/coin_gecko.py
import requests

BASE_URL = 'https://api.coingecko.com/api/v3/'

def ping():
    req_url = 'ping'
    r = requests.get(BASE_URL+req_url)
    r_json = r.json()
    print(r_json)

def coin_list():
    req_url = 'coins/list'
    r = requests.get(BASE_URL+req_url)
    r_json = r.json()
    return r_json

def simple_price(coin):
    coin_id = coin
    req_url = 'simple/price?ids='+coin_id+'&vs_currencies=usd'
    r = requests.get(BASE_URL+req_url)
    r_json = r.json()
    return r_json

def simple_token_price(coin_id):
    pass

def coin_markets(coin):
    coin_id = coin
    req_url = 'coins/markets?vs_currency=usd&ids='+coin_id+'&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en'
    r = requests.get(BASE_URL + req_url)
    r_json = r.json()
    print(r_json)
