#! /usr/bin/env python3

from __future__ import print_function
import sys

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
digit = '0123456789'

def pat(length, find=None):
  count   = 0
  out     = ''
  for u in upper:
    for l in lower:
      for n in digit:
        chunk = u+l+n
        out += chunk
        if find is not None and find in out[-(2*len(find)):]:
          return out.index(find)
        count += 3
        if count >= length:
          if find is None:
            return out[:length]
          else:
            return 'NOT FOUND'
  try:
    return out+pat(length-count, find=find)
  except RecursionError:
    return out+'...'

def usage():
  print('Usage: {:s} (<length>|<string to find>)'.
                  format(sys.argv[0]))


if __name__ == '__main__':
  try:
    end = '\n'
    if len(sys.argv) == 3:
      if sys.argv[1] == '-n':
        end = ''
        sys.argv[1] = sys.argv[2]
      elif sys.argv[2] == '-n':
        end = ''
    length = int(sys.argv[1])
    print(pat(length), end=end)
  except (ValueError):
    print(pat(length=20280, find=sys.argv[1]))
  except (IndexError):
    usage()

