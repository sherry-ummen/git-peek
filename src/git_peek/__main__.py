#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
from git_peek.parse_arguments import *


__author__ = "Sherry Ummen"
__copyright__ = "Sherry Ummen"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def git_log_command_builder(args) -> str:
  cmd = "git log"
  if args.author != None:
    cmd += f" --author \"{args.author}\""
  if args.across:
    cmd += " --all"

  cmd += f" -n {args.line_limit} --pretty=format:\"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset\" --abbrev-commit"
  print(cmd)
  return cmd

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    if args.fetch_all:
      os.system('git fetch --all')
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations..." + args.author)
    os.system(git_log_command_builder(args))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
