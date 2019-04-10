from argparse import ArgumentParser

from trail.irail_gw import get_connections


def status(args):
    connections = get_connections(start='Leuven', end='Halle', date='110419')
    for train in connections.get('connection'):
        print train
        print ''

def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)

    status_cmd.set_defaults(func=status)

    ht = 'Usage: configure'
    configure = sub.add_parser('configure', help=ht)
    configure.add_argument('--id', dest='identifier', help='first few chars of location_id or '
                                                           'event_owner_id, checks for uniqueness first')
    configure.set_defaults(func=configure)
    return ap