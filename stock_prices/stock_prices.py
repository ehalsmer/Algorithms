#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # initialize max_profit with first possible value: buy at 0, sell at 1
  max_profit = prices[1]-prices[0]
  # Use a loop within a loop to find best price j to sell, after buying at price i
  for i in range(1, len(prices)):
    for j in range(i + 1, len(prices)):
      # print('i, j: ', i, j)
      if prices[j] - prices[i] > max_profit:
        max_profit = prices[j] - prices[i]
  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))