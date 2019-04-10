import requests

BASE = 'https://api.irail.be'
HEADERS = {'Accept': 'application/json'}


def get_connection(start, end, date):
    url = 'connections/?to={}&from={}&fast=true&timesel=departure&date={}&format=json'.format(start, end, date)
    response = requests.get(url='{}/{}'.format(BASE, url), headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print response.status_code



