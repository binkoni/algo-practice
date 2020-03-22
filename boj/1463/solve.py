def recursion(N):
  N = float(N)
  #print(f'N is {N}')
  if N < 1 or not N.is_integer(): 
    return float('inf')
  elif N == 1:
    return 0
  elif N / 3 == 1:
    return 1
  elif N / 2 == 1:
    return 1
  elif N - 1 == 1:
    return 1
  else:
    return min(solve(N / 3), solve(N / 2), solve(N - 1)) + 1

def dp(N):
  memory = [0] * (N + 1)
  memory[1] = 0
  for i in range(2, N + 1):
    memory[i] = memory[i - 1] + 1
    if i % 2 == 0:
      memory[i] = min(memory[i], memory[int(i / 2)] + 1)
    if i % 3 == 0:
      memory[i] = min(memory[i], memory[int(i / 3)] + 1)
  return memory[N]

solve = dp

N = int(input().strip())
print(solve(N))
