import requests


def base():
    return 'https://api.irail.be'


def headers():
    return {'Accept': 'application/json'}


def connections(start, end, date):
    url = 'connections/?to={}&from={}&fast=true&timesel=departure&date={}&format=json'.format(start, end, date)
    response = requests.get(url='{}/{}'.format(base(), url), headers=headers())
    if response.status_code == 200:
        return response.json()
    else:
        print response.status_code
