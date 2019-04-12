from argparse import ArgumentParser

from trail import show, irail


def status(args):
    station = args.station.encode('utf-8')
    board = irail.live_board(station)
    show.print_to_console(board)


def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)
    status_cmd.add_argument('station', help='Name of station you want to see the status from')
    status_cmd.set_defaults(func=status)

    return ap
