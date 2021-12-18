import heapq
reader = open("sumdist.in", 'r')
writer = open('sumdist.out', 'w')

v, m = map(int, reader.readline().split())

adj = [0] * v
for i in range(v):
    adj[i] = [None] * v

for _ in range(m):
    v, u = reader.readline().split()
    v = int(v)
    u = int(u)
    adj[v - 1][u - 1] = 1
    adj[u - 1][v - 1] = 1


N = len(adj)
#dist = [[9999999 for _ in range(N)] for _ in range(N)]

dist = [0] * N
for i in range(N):
    dist[i] = [None] * N

for node in range(N):
    x = node
    path = dist[node]
    others = {node: None for node in range(N)}
    node_h = []
    curr_dist = 0
    others[x] = curr_dist
    while True:
        path[x] = curr_dist
        for y in others:
            distance = adj[x][y]
            if distance is None:
                continue
            new_d = curr_dist + distance
            if others[y] is None or others[y] > new_d:
                heapq.heappush(node_h, (new_d, y))
                others[y] = new_d
        del others[x]
        if not others:
            break

        curr_dist, x = heapq.heappop(node_h)
        if path[x] is not None:
            continue
res = 0
k = len(dist)
for i in range(k):
    for j in range(k):
        if j >= i:
            res += dist[i][j]
writer.write(str(res))
