from argparse import ArgumentParser

from datetime import datetime

from trail import irail_gw, alert


def status(args):
    now = datetime.now()
    params = {'to': 'Halle',
              'from': 'Leuven',
              'fast': 'true',
              'timesel': 'departure',
              'date': now.strftime('%d%m%y'),
              'format': 'json'}
    conn = irail_gw.get('connections', params)
    for train in conn.get('connection'):
        alert.delay(train)


def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)
    status_cmd.set_defaults(func=status)

    return ap
