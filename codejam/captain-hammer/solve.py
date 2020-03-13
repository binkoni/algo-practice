#!/usr/bin/python
# https://code.google.com/codejam/contest/2845486/dashboard
import math

G = -9.8
N = int(input().strip())
for i in range(N):
  V, D = input().strip().split()
  V, D = int(V), int(D)
  A = math.asin((D / (V ** 2)) * G) / 2
  print('Case #%d: %f' % (i + 1, abs(180 * A / math.pi)))
