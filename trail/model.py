from __future__ import print_function

from sqlalchemy import Column, Integer, String

from trail import utils
from trail.db import Base, engine
from trail import db


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


class LiveBoard(object):
    def __init__(self, records):
        self.records = records

    @property
    def records(self):
        if not self._records:
            self._records = db.find_all(BoardRecord)
        return self._records

    @records.setter
    def records(self, records):
        db.add_all(records)
        self._records = records

    @classmethod
    def from_raw(cls, raw_board):
        records = []

        for d in raw_board.get('departures').get('departure'):
            br = BoardRecord()

            br.dest = d.get('station')
            br.delayed = int(d.get('delay')) / 60
            br.scheduled = int(d.get('time'))

            records.append(br)
        return cls(records)

    def show(self):
        [print(record) for record in self.records]


