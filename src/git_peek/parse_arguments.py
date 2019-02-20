import os
import sys
import argparse
from git_peek import __version__
import logging


def parse_args(args):
    git_user = os.popen("git config user.name").read().strip()
    parser = argparse.ArgumentParser(
        description="Git Peek", allow_abbrev=False)
    parser.add_argument('--version', action='version',
                        version='git-peek {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v', '--verbose', dest="loglevel", help="set loglevel to INFO", action='store_const', const=logging.INFO)
    parser.add_argument(
        '-vv', '--very-verbose', dest="loglevel", help="set loglevel to DEBUG", action='store_const', const=logging.DEBUG)
    parser.add_argument('-a', '--author', dest="author",
                        help="commit author", type=str, default=git_user)
    parser.add_argument('-x', '--across', dest='across',
                        help="show commit across all branches", action='store_true', default=False)
    parser.add_argument('-n', '--nl', dest='line_limit',
                        help='limit the number of log lines', default=100)
    parser.add_argument('-f', '--fetch', dest='fetch_all',
                        help='fetch all before showing the log entries', action='store_true', default=False)
    parser.add_argument('-nb', '--new-branches', dest='new_branches',
                        help='show new branches which are not fetched yet', action='store_true', default=False)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
