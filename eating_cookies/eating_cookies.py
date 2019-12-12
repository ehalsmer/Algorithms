#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# Tribonacci numbers, see https://oeis.org/A000073
def eating_cookies(n, cache=None):
  memo = {0:1, 1:1, 2:2}
  if n in memo:
    print('found in memo')
    return memo[n]
  else:
    computed = eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    memo[n] = computed
    print('computed')
    return memo[n]

print(eating_cookies(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')