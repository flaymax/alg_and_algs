def get_dist(adj):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if adj[j][i] != -1 and adj[i][k] != -1:
                    if adj[j][k] > adj[j][i] + adj[i][k] or adj[j][k] == -1:
                        adj[j][k] = adj[j][i] + adj[i][k]
    return adj


with open('diameter.in.txt', 'r') as fin:
    n = int(fin.readline())

    adj = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        adj[i] = list(map(int, fin.readline().split()))

    # dist = [[-1 for i in range(n)] for j in range(n)]
radius = 999999
diameter = -999999


with open('diameter.out.txt', 'w') as fout:
    dist = get_dist(adj)
    for j in range(n):
        curr_rad = 0

        for k in range(n):
            if diameter < dist[j][k]:
                diameter = dist[j][k]
            if curr_rad < dist[j][k]:
                curr_rad = dist[j][k]

        radius = min(radius, curr_rad)
    res = str(diameter) + "\n" + str(radius)
    fout.write(res)