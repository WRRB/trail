from datetime import datetime

import pytz


def format_time(timestamp):
    time = datetime.utcfromtimestamp(timestamp)
    time = pytz.utc.localize(time)
    time = time.astimezone(pytz.timezone('Europe/Brussels'))
    return time.strftime('%H:%M')
