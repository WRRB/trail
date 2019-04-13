import os
import sys

ROOT = os.path.dirname(__file__)


class TrailException(Exception):
    pass


reload(sys)
sys.setdefaultencoding('utf-8')