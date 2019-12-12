#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def small_eating_cookies(n):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  else:
    return small_eating_cookies(n-3) + small_eating_cookies(n-2) + small_eating_cookies(n-1)


# Tribonacci numbers, see https://oeis.org/A000073
def eating_cookies(n):
  cache = {0:1, 1:1, 2:2, 3:4}
  def inner(n):
    nonlocal cache
    if n not in cache:
      cache[n] = inner(n-3) + inner(n-2) + inner(n-1)
    return cache[n]
  return inner(n)

# print('15: ',eating_cookies(15))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')