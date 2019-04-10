@echo off & python -x "%~f0" %* & goto :eof
from trail.cli.parser import get_parser
import logging
import traceback
if __name__ == '__main__':
    try:
        parser = get_parser()
        args = parser.parse_args()
        args.func(args)
    except Exception as e:
        logging.info('there was an exception {} \n {}'.format(e, traceback.print_exc()))