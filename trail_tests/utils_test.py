from trail.utils import format_time


def test_format_time():
    assert format_time(1555099080) == '21:58'

