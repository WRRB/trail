from argparse import ArgumentParser

from trail import show, irail, db, model


def status(args):
    station = args.station
    board = irail.live_board(station)
    records = model.create_board_records(board)
    db.add_all(records)
    show.print_to_console()


def get_parser():
    ap = ArgumentParser()
    sub = ap.add_subparsers(help='sub-command help')
    sub.required = True

    ht = 'Usage: status'
    status_cmd = sub.add_parser('status', help=ht)
    status_cmd.add_argument('station', help='Name of station you want to see the status from')
    status_cmd.set_defaults(func=status)

    return ap
