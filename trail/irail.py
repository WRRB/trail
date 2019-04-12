from datetime import datetime

from trail import irail_gw


def live_board(station):
    now = datetime.now()
    params = {'station': station,
              'fast': 'true',
              'arrdep': 'departure',
              'date': now.strftime('%d%m%y'),
              'time': now.strftime('%H%M'),
              'format': 'json'}
    return irail_gw.get('liveboard', params)