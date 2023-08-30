# !/

from coin_gecko import ping, coin_list, simple_price, coin_markets
import time

# ping()

# coin_list = coin_list()

my_symbol_list = ['eth', 'btc', 'link', 'doge', 'sol', 'arb']
# my_id_list = []
coin_dict = {
}

# for coin in coin_list:
#     for my_coin in my_symbol_list:
#         if coin['symbol'] == my_coin:
#             my_id_list.append(coin['id'])

# for coin_id in my_id_list:
#     print(simple_price(coin_id))

my_id_list = ['bitcoin', 'chainlink', 'dogecoin', 'ethereum', 'arbitrum', 'solana']
while True:
    for coin_id in my_id_list:
        coin_markets(coin_id)
        time.sleep(30)
