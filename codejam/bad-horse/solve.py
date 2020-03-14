#!/usr/bin/python
# https://code.google.com/codejam/contest/2933486/dashboard
# bipartite graph
def bfs(graph, visited, queue, xset, yset):
  while queue:
    e = queue.pop(0)
    if e not in visited:
      if e not in xset and e not in yset:
        xset.add(e)
      if e in xset:
        if len(set(graph[e]).intersection(xset)) >= 1:
          return False
        else:
          yset.update(graph[e])
      elif e in yset:
        if len(set(graph[e]).intersection(yset)) >= 1:
          return False
        else:
          xset.update(graph[e])
      visited.add(e)
      queue.extend(graph[e])
  return True

ncases = int(input())
for i in range(ncases):
  graph = {}
  visited = set()
  queue = []
  xset = set()
  yset = set()
  npairs = int(input())
  for j in range(npairs):
    a, b = input().strip().split()
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  ret = True
  for e in graph:
    queue.append(e)
    ret = bfs(graph, visited, queue, xset, yset)
    if ret == False:
      break
  print(f'Case #{i + 1}: ' + ('Yes' if ret else 'No'))
