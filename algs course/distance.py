def main():
    with open('distance.in', 'r') as reader:
        n, m = map(int, reader.readline().split())
        s, f = map(int, reader.readline().split())
        arr = [[] for i in range(n)]
        d = [float('inf') for i in range(n)]
        d[s - 1] = 0
        used = [-1] * n
        prev = [-1] * n
        for i in range(m):
            b, e, v = map(int, reader.readline().split())
            arr[b - 1] += [(e - 1, v)]
            arr[e - 1] += [(b - 1, v)]

    for i in range(n):
        min_ = float('inf')
        iod = -1

        for j in range(n):
            if min_ > d[j] and used[j] == -1:
                min_ = d[j]
                iod = j
        if iod == -1:
            break
        used[iod] = 1
        d[iod] = min_

        for v in arr[iod]:
            if d[v[0]] > d[iod] + v[1]:
                d[v[0]] = d[iod] + v[1]
                prev[v[0]] = iod

    writer = open("distance.out", "w")
    if d[f - 1] != float('inf'):
        writer.write(str(d[f - 1]))
        i = f - 1
        res = []
        k = 0
        while prev[i] != -1:
            res += [i + 1]
            i = prev[i]
            k += 1
        res += [s]
        res = [str(i) for i in res]

        writer.write('\n' + ' '.join(res[::-1]))
    else:
        writer.write('-1')


main()
