from argparse import ArgumentParser

from trail import irail
from trail.model import LiveBoard


def status(args):
    station = args.station
    raw_board = irail.live_board(station)
    board = LiveBoard.from_raw(raw_board)
    board.show()
#Dag Wim, ik ben Jan

def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')
    sub.required = True

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)
    status_cmd.add_argument('station', help='Name of station you want to see the status from')
    status_cmd.set_defaults(func=status)

    return ap
