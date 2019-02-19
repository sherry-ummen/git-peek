import os
import sys
import argparse
from git_peek import __version__
import logging


def parse_args(args):
    git_user = os.popen("git config user.name").read().strip()
    parser = argparse.ArgumentParser(
        description="Git Peek")
    parser.add_argument('--version', action='version',
                        version='git-peek {ver}'.format(ver=__version__))
    parser.add_argument(
        '-v', '--verbose', dest="loglevel", help="set loglevel to INFO", action='store_const', const=logging.INFO)
    parser.add_argument(
        '-vv', '--very-verbose', dest="loglevel", help="set loglevel to DEBUG", action='store_const', const=logging.DEBUG)
    parser.add_argument('-a', '--author', dest="author", help="commit author", type=str, default=git_user)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")
