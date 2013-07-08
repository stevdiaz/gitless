#!/usr/bin/env python

# Gitless - a version control system built on top of Git.
# Copyright (c) 2013  Santiago Perez De Rosso.
# Licensed under GNU GPL, version 2.

"""gl-untrack - Stop tracking changes to files.

Implements the gl-untrack command, part of the Gitless suite. The gl-untrack
command allows the user to stop tracking changes to the files passed as
parameters."""


import argparse

import cmd
import lib
import pprint


def main():
  parser = argparse.ArgumentParser(
      description='Stop tracking changes to files')
  parser.add_argument(
      'files', nargs='+', help='the file(s) to untrack')
  args = parser.parse_args()
  for fp in args.files:
    ret = lib.untrack_file(fp)
    if ret is lib.FILE_NOT_FOUND:
      pprint.err('Can\'t untrack an inexistent file: %s' % fp)
    elif ret is lib.FILE_ALREADY_UNTRACKED:
      pprint.err('File %s is already untracked' % fp)
    elif ret is lib.FILE_IS_IGNORED:
      pprint.err('File %s is ignored. Nothing to untrack' % fp)
      pprint.err_exp('edit the .gitignore file to stop ignoring file %s' % fp)
    elif ret is lib.SUCCESS:
      pprint.msg('File %s is now a untracked file' % fp)
    elif ret is lib.FILE_IN_CONFLICT:
      pprint.err('Can\'t untrack a file in conflict')
    else:
      raise Exception('Unexpected return code')


if __name__ == '__main__':
  cmd.run(main)
