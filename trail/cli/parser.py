from argparse import ArgumentParser

from datetime import datetime

from trail.irail_gw import connections


def status(args):
    now = datetime.now()
    params = {'to': 'Halle',
              'from': 'Leuven',
              'fast': 'true',
              'timesel': 'departure',
              'date': now.strftime('%d%m%y'),
              'format': 'json'}
    conn = connections(params)
    for train in conn.get('connection'):
        print train
        print ''


def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)
    status_cmd.set_defaults(func=status)

    return ap
