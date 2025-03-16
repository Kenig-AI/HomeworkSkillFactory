import json

import requests
from confing import keys

class ConveionException(Exception):
    pass

class Price:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if base == quote:
            raise ConveionException(f'Не возмоно перевести одинаковые валюты {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConveionException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticket = keys[quote]
        except KeyError:
            raise ConveionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConveionException(f'Не удалось обработать колличество {amount}')

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={base_ticker + quote_ticket}&key=b85b9638d47554e3f5989564b3a37c0e')
        total_base = float(json.loads(r.content)["data"][base_ticker + quote_ticket]) * float(amount)


        return total_base