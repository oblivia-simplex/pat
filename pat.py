#! /usr/bin/env python3

import sys

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
digit = '0123456789'

def make_pat(length, find=None):
  count   = 0
  out     = ''
  for u in upper:
    for l in lower:
      for n in digit:
        chunk = u+l+n
        out += chunk
        if find is not None:
          if find in out[-(2*len(find)):]:
            return out.index(find)
        count += 3
        if count >= length:
          if find is None:
            return out[:length]
          else:
            return 'NOT FOUND'
  return out+make_pat(length-count, find=find)

def usage():
  print('Usage: {:s} (<length>|<string to find>)'.
                  format(sys.argv[0]))


if __name__ == '__main__':
  try:
    length = int(sys.argv[1])
    print(make_pat(length))
  except (ValueError):
    print(make_pat(length=20280, find=sys.argv[1]))
  except (IndexError):
    usage()

