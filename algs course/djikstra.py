def main():
    reader = open('dijkstra.in','r')
    writer = open('dijkstra.out', 'w')
    n, s, f = map(int, reader.readline().split())
    arr = [list(map(int, reader.readline().split())) for _ in range(n)]

    d = [float('inf') for _ in range(n)]
    used = [False for _ in range(n)]

    d[s - 1] = 0
    for _ in range(n):
        min_ = float('inf')
        ind = -1
        for j in range(n):
            if not used[j] and min_ > d[j]:
                min_ = d[j]
                ind = j
        if ind == -1:
            break
        used[ind] = True
        for v in range(n):
            if ind != v and arr[ind][v] != -1:
                d[v] = min(d[v], d[ind] + arr[ind][v])

    if d[f - 1] != float('inf'):
        writer.write(str(d[f - 1]))

    else:
        writer.write(str(-1))


main()
