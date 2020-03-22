def dp(N):
  counts = [0] * (N + 1)
  counts[0] = 1
  for i in range(1, N + 1):
    if N >= 1:
      counts[i] += counts[i - 1]
    if N >= 2:
      counts[i] += counts[i - 2]
    if N >= 3:
      counts[i] += counts[i - 3]
  return counts[N]

T = int(input().strip())
for i in range(T):
  N = int(input().strip())
  print(dp(N))

'''
count(4) = count(4, with last 1 selected) + count(4, with last 2 selected) + count(4, with last 3 selected)
count(4) = count(3) + count(2) + count(1)
count(4) = (count(2) + count(1) + count(0)) + count(2) + count(1)
count(4) = ((count(1) + count(0)) + count(1) + count(0)) + count(2) + count(1)
...
'''
