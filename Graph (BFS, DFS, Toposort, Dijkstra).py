from collections import deque
import heapq
from math import inf


def bfs(s, AL):
    order = []
    to_visit, visited = deque([s]), {s}
    while to_visit:
        u = to_visit.popleft()
        order.append(u)
        for v in AL[u]:
            if v not in visited:
                to_visit.append(v)
                visited.add(v)
    return order


def dfs(s, AL):
    order = []
    to_visit, visited = [s], {s}
    while to_visit:
        u = to_visit.pop()
        order.append(u)
        for v in AL[u]:
            if v not in visited:
                to_visit.append(v)
                visited.add(v)
    return order


def dfs_re(s, AL):
    order = []
    visited = set()

    def dfs_re_helper(u, AL, visited):
        order.append(u)
        visited.add(u)
        for v in AL[u]:
            if v not in visited:
                dfs_re_helper(v, AL, visited)

    dfs_re_helper(s, AL, visited)
    return order


def dfs_re_toposort(s, AL):
    toposort = []
    visited = set()

    def dfs_re_helper(u, AL, visited):
        visited.add(u)
        for v in AL[u]:
            if v not in visited:
                dfs_re_helper(v, AL, visited)
        toposort.append(u)

    dfs_re_helper(s, AL, visited)
    toposort.reverse()
    return toposort


def bfs_toposort(AL):
    # first, create a dict to tracking incoming edges for each node
    incoming_edges = {v: 0 for v in AL}
    for u in AL:
        for v in AL[u]:
            incoming_edges[v] += 1
    # then, add nodes with no incoming edge to the queue
    queue = deque()
    toposort = []
    for v in incoming_edges:
        if incoming_edges[v] == 0:
            queue.append(v)

    while queue:
        u = queue.popleft()
        toposort.append(u)
        if u in AL:
            for v in AL[u]:
                incoming_edges[v] -= 1
                if incoming_edges[v] == 0:
                    queue.append(v)
    return toposort


def dijkstra(s, V, Weighed_AL):  # O((V+E)logV)
    # in the tuple t, v = t[0], dist = t[1]
    dist = [0 if u == 0 else inf for u in range(V)]
    to_visited = []
    heapq.heappush(to_visited, (0, s))

    while to_visited:
        d, u = heapq.heappop(to_visited)
        if d > dist[u]:
            continue
        for v, w in Weighed_AL[u]:
            if dist[u] + w >= dist[v]:
                continue
            dist[v] = dist[u] + w
            heapq.heappush(to_visited, (dist[v], v))
    for u in range(V):
        print('SSSP ({}, {}) = {}'.format(s, u, dist[u]), end=' ')

# DP算法处理DAG时，时间复杂度为O(V+E),优于dijkstra算法


AL = {0: [1, 2],
      1: [2, 3],
      2: [3, 5],
      3: [4],
      4: [],
      5: [],
      6: [],
      7: [6],
      8: [7, 9],
      9: []}

Weighed_AL = {2: [(0, 1), (1, 1)],
              0: [(2, 1), (1, 1)],
              1: [(0, 1), (2, 1)]}

print(bfs(0, AL))
print(dfs(0, AL))
print(dfs_re(0, AL))
print(dfs_re_toposort(0, AL))
print(bfs_toposort(AL))
print(dijkstra(0, 3, Weighed_AL))


