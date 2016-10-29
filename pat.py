#! /usr/bin/env python3

from __future__ import print_function
import sys

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
digit = '0123456789'

def pat(length):
  count   = 0
  out     = ''
  for u in upper:
    for l in lower:
      for n in digit:
        out += u+l+n
        count += 3
        if count >= length:
          return out[:length]
  try:
    return out+pat(length-count, find=find)
  except RecursionError:
    return out+'...'

def usage():
  print('Usage: {:s} (<length>|<string to find>)'.
                  format(sys.argv[0]))

def find(p):
  # assume that p is Uld
  # we'll adjust later
  adj = 0
  u, l, d = '', '', ''
  D = [c for c in p if c in digit]
  L = [c for c in p if c in lower]
  U = [c for c in p if c in upper]
  if not (D and L and U):
    return 'NOT ENOUGH INFORMATION TO PINPOINT OFFSET'
  else:
    u, l, d = U[0], L[0], D[0]
  if p.index(d) < p.index(u):
    adj = -1
    d = digit[(digit.index(d) + 1) % 10]
  if p.index(l) < p.index(u):
    adj = -2
  place = ((upper.index(u) * 26*10) + 
           (lower.index(l) * 10)    +
           (digit.index(d)))        * 3
  return place + adj

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
    print(find(sys.argv[1]))
  except (IndexError):
    usage()

