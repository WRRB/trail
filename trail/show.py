from __future__ import print_function

from trail import db
from trail.model import BoardRecord


def print_to_console():
    [print(record) for record in db.session.query(BoardRecord).all()]
