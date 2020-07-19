#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  results = [[]]
  def rps(n):
    n -= 1
    for arr in results:
      results.remove(arr)
      results.extend([arr + ['rock'], arr + ['paper'], arr + ['scissors']])
      return
      # print(results)
  while n > 0:
    rps(n)
    n -= 1
    print(n)
  return results
  # return 

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')