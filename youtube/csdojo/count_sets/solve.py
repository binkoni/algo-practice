#!/usr/bin/python
# https://www.youtube.com/watch?v=nqlNzOcnCfs
total = int(input().strip())
array = list(map(int, input().strip().split()))
def recurse(total, array, idx):
  if total == 0:
    return 1
  elif total < 0:
    return 0
  elif idx < 0:
    return 0
  elif total < array[idx]:
    return recurse(total, array, idx - 1)
  else:
    return recurse(total - array[idx], array, idx - 1) + recurse(total, array, idx - 1)

def recursive(total, array):
  return recurse(total, array, len(array) - 1)

print(solve(total, array))


# [2, 4, 6, 10], total 16
# count(total 0) == 1

# count(total 16) == count(total 16, with 10) + count(total 16, without 10)
# == count(total 6, [2, 4, 6]) + total(16, [2, 4, 6])
# == count(total 0, [2, 4]) + total(6, [2, 4]) + count(total 16, [2, 4])
# ...
# == 1 + 1 + 0
# == 2

# [2], total 2
# count(total 2, [2]) == count(total 2, with 2) + count(total 2, without 2)
# count(total 2, with 2) == count(total 0, []) == 1
# count(total 2, without 2) == count(total 2, []) == 0
# count == 1
