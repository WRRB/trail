from datetime import datetime
import pytz


def print_to_console(board):
    dep = board.get('departures').get('departure')
    fmt = '{}   {} {}'
    for d in dep:
        direction = d.get('station')
        late = int(d.get('delay'))/60
        delay_indicator = '+{}'.format(late) if late else None
        padding = '  '
        time = format_time(int(d.get('time')))
        print fmt.format(delay_indicator or padding, time, direction.encode('utf-8'))


def format_time(timestamp):
    time = datetime.utcfromtimestamp(timestamp)
    time = pytz.utc.localize(time)
    time = time.astimezone(pytz.timezone('Europe/Brussels'))
    return time.strftime('%H:%M')
