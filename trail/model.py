from sqlalchemy import Column, Integer, String

from trail import utils
from trail.db import Base, engine


class BoardRecord(Base):
    __tablename__ = 'live_board'

    id = Column(Integer, primary_key=True)
    delayed = Column(Integer)
    scheduled = Column(Integer)
    dest = Column(String)

    def __repr__(self):
        padding = '  '
        delay_indicator = '+{}'.format(self.delayed) if self.delayed else None
        return '{}   {} {}'.format(delay_indicator or padding, utils.format_time(self.scheduled), self.dest)


Base.metadata.create_all(engine)


def create_board_records(board):
    records = []

    for d in board.get('departures').get('departure'):
        br = BoardRecord()

        br.dest = d.get('station')
        br.delayed = int(d.get('delay')) / 60
        br.scheduled = int(d.get('time'))

        records.append(br)
    return records
