#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging
from git_peek.parse_arguments import *


__author__ = "Sherry Ummen"
__copyright__ = "Sherry Ummen"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
