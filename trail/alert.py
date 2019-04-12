from datetime import datetime


def delay(board):
    dep = board.get('departures').get('departure')
    for d in dep:
        direction = d.get('station')
        late = int(d.get('delay'))
        time = d.get('time')
        if late:
            print 'train to {} has been delayed {} minutes'.format(direction.encode('utf-8'), late)
        else:
            print 'train to {} will arrive at {}'.format(direction.encode('utf-8'), datetime.utcfromtimestamp(int(time)))
