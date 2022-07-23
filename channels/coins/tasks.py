import requests
from django.forms.models import model_to_dict
from .models import Coin
from celery import shared_task

@shared_task
def get_coins_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    coins = []
    for coin in data:
        obj, created = Coin.objects.get_or_create(simbol=coin['symbol'])

        obj.name = coin['name']
        obj.symbol = coin['symbol']

        if obj.price > coin['current_price']:
            state = 'fall'
        elif obj.price == coin['current_price']:
            state = 'same'
        elif obj.price < coin['current_price']:
            state = 'raise'
        obj.price = coin['current_price']
        obj.rank = coin['rank']
        obj.url = coin['image']

        obj.save()

        new_data = model_to_dict(obj)
        #new_data['state'] = state
        new_data.update({'stste': state})

        coins.append(new_data)