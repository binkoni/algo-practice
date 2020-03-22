#!/usr/bin/python
'''
def solve(budget, ncosts, costs, memory={}):
  key = str(budget) + ':' + str(ncosts)
  ret = None
  #print(f'{budget}, {ncosts}, {costs}, {memory}')
  if key in memory:
    return memory[key]
  if budget <= 0 or ncosts <= 0:
    ret = 0
  elif costs[ncosts - 1] <= budget:
    ret = max(solve(budget, ncosts - 1, costs, memory), solve(budget - costs[ncosts - 1], ncosts - 1, costs, memory) + 1)
  else:
    ret = solve(budget, ncosts - 1, costs, memory)
  memory[key] = ret
  return ret
'''


def solve(budget, ncosts, costs):
  count = 0
  costs = sorted(costs)
  for i in range(ncosts):
    if budget >= costs[i]:
      budget -= costs[i]
      count += 1
  return count

T = int(input().strip())
for t in range(T):
  l = list(map(int, input().strip().split()))
  N, B = l[0], l[1]
  costs = list(map(int, input().strip().split()))
  print('Case #%d: %d' % (t + 1, solve(B, N, costs)))
