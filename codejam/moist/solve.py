#!/usr/bin/python
# https://code.google.com/codejam/contest/2933486/dashboard
# application of insertion sort
N = int(input().strip())
for i in range(N):
  M = int(input().strip())
  deck = []
  count = 0
  for j in range(M):
    deck.append(input().strip())
  p = 0
  for k in range(len(deck)):
    if k > 0 and deck[k] < deck[p]:
      count += 1
    else:
      p = k
  print(f'Case #{i + 1}: {count}')
