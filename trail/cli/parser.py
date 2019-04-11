from argparse import ArgumentParser

from trail.irail_gw import connections


def status(args):
    conn = connections(start='Leuven', end='Halle', date='110419')
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
