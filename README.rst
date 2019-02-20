========
git-peek
========

Installation
============
pip install git+https://github.com/sherry-ummen/git-peek.git

Description
===========
Python script to peek what various commits someone did


Usage
===========
usage: git-peek [-h] [--version] [-v] [-vv] [-a AUTHOR] [-x] [-n LINE_LIMIT] [-f] [-nb]

Git Peek

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         set loglevel to INFO
  -vv, --very-verbose   set loglevel to DEBUG
  -a AUTHOR, --author AUTHOR
                        commit author
  -x, --across          show commit across all branches
  -n LINE_LIMIT, --nl LINE_LIMIT
                        limit the number of log lines
  -f, --fetch           fetch all before showing the log entries
  -nb, --new-branches   show new branches which are not fetched yet
