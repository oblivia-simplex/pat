#! /usr/bin/env python3

import sys

def main(length):
  upper   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  lower   = upper.lower()
  digit   = '0123456789'
  count   = 0
  out     = ''
  for u in upper:
    for l in lower:
      for n in digit:
        out += u+l+n
        count += 3
        if count >= length:
          return out[:length]

def usage():
  print('Usage: {:s} <length>'.format(sys.argv[0]))


if __name__ == '__main__':
  try:
    length = int(sys.argv[1])
    print(main(length))
  except (ValueError, IndexError):
    usage()

