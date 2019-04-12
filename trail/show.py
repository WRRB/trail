from datetime import datetime
import pytz


def print_to_console(board):
    dep = board.get('departures').get('departure')
    fmt = '+{}    {}\t{}'
    for d in dep:
        direction = d.get('station')
        late = int(d.get('delay'))
        time = datetime.utcfromtimestamp(int(d.get('time')))
        time = pytz.utc.localize(time)
        time = time.astimezone(pytz.timezone('Europe/Brussels'))
        print fmt.format(late/60,time.strftime( '%H:%M'), direction.encode('utf-8'), )

