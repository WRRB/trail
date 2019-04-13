@echo off & python -x "%~f0" %* & goto :eof
import logging

from trail import TrailException
from trail.cli.parser import get_parser

if __name__ == '__main__':
    try:
        parser = get_parser()
        args = parser.parse_args()
        args.func(args)
    except TrailException as e:
        logging.error(e)