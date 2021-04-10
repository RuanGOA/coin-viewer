'''Utils
'''
from const import (
    TARGET_COIN,
    COINS_TO_SEARCH,
    COLUMN_NAMES
)

def generate_string_search():
    '''Uses constants defined in const.py to return a string made up of
    smaller strings in the format "coin_search-target_search".
    '''
    coins_formated_list = []
    for coin in COINS_TO_SEARCH:
        formated_coin = f'{coin}-{TARGET_COIN}'
        coins_formated_list.append(formated_coin)

    return ','.join(coins_formated_list)


def print_quots(response, quots_cache):
    '''Receives the result of a request and displays the values of that
    result formatted on the screen.
    '''
    items_request = response.items()

    print('-'*66)
    print_formated_quot(COLUMN_NAMES)
    print('-'*66)
    for item in items_request:
        format_quot(item[0], item[1], quots_cache.get(item[0]))
    print('-'*66)


def format_quot(name, infos, last_avg):
    '''Auxiliary function of print_quots. Formats the request data for
    each line.
    '''
    high = round(float(infos.get('high')), 3)
    low = round(float(infos.get('low')), 3)
    avg = round((high+low)/2, 3)
    state_avg = '~'
    if last_avg:
        if last_avg < avg:
            state_avg = '+'
        elif last_avg > avg:
            state_avg = '-'
        else:
            state_avg = '='

    formated_quot = [
        name,
        f'{str(high)} {TARGET_COIN}',
        f'{str(low)} {TARGET_COIN}',
        f'{str(avg)} {TARGET_COIN}',
        state_avg
    ]

    print_formated_quot(formated_quot)


def print_formated_quot(lis):
    '''From the formatted response values, displays the formatted
    result on the screen.
    '''
    print(
        '| %-5s | %-12s | %-12s | %-12s | %-9s |' % \
        (lis[0], lis[1], lis[2], lis[3], lis[4])
    )


def generate_json_cache(quots):
    '''Generates a json that has the names of coins_search as keys, and
    as the value the average of the lowest value and the highest value
    of the previous search.
    '''
    result = {}
    for name, infos in quots.items():
        high = round(float(infos.get('high')), 3)
        low = round(float(infos.get('low')), 3)
        avg = round((high+low)/2, 3)
        result[name] = avg

    return result
