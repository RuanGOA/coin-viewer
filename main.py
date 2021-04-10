'''main
'''
import os
from time import sleep
import json
import requests as req
from utils import (
    generate_string_search,
    print_quots,
    generate_json_cache
)
from const import BASE_URL_API

STRING_SEARCH = generate_string_search()

URL_API = f'{BASE_URL_API}{STRING_SEARCH}'

if __name__ == '__main__':
    quots_cache = {}
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        request_quot = req.get(URL_API)
        quots = json.loads(request_quot.text)

        print_quots(quots, quots_cache)

        quots_cache = generate_json_cache(quots)

        sleep(30)
