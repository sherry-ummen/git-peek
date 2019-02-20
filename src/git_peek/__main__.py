#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import subprocess
from colorama import Fore, Back, Style
from git_peek.parse_arguments import *
from subprocess import call, STDOUT


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
    if not _is_git_repo():
      print('Not a git repo. Program will exit!')
      return

    args = parse_args(args)
    if args.fetch_all:
      os.system('git fetch --all')

    if args.new_branches:
      c = subprocess.check_output(
            "git fetch --all --dry-run", stderr=subprocess.STDOUT).decode('UTF-8').splitlines()
      branches_new = list(map(lambda x: x[28:],list(filter(lambda x: x.startswith(' * [new branch]'), c))))
      if not any(branches_new):
        print('No new branches found!')
        return
      print(Fore.GREEN, *branches_new,sep='\n')
      print(Style.RESET_ALL)
      return

    setup_logging(args.loglevel)
    _logger.debug("Starting operation.. " + args.author)
    os.system(git_log_command_builder(args))
    _logger.info("Script ends here")

def run():
    main(sys.argv[1:])

def _is_git_repo() -> bool:
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
      return False
    else:
      return True

if __name__ == "__main__":
    run()
