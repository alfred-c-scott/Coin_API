from coin_gecko import coin_list

my_symbol_list = ['eth', 'btc', 'link', 'doge', 'sol', 'arb']
my_id_list = []

coin_list = coin_list()

for coin in coin_list:
    for my_coin in my_symbol_list:
        if coin['symbol'] == my_coin:
            my_id_list.append(coin['id'])

for coin_id in my_id_list:
    print(coin_id)
