def parse_in(filename="maze.in.txt", content=None):
    if content is None:
        with open(filename) as f:
            content = f.readlines()

    line_ = content[0].strip('\n ')
    vertex = int(line_.split(' ')[0])
    adj = [[None for _ in range(vertex)] for _ in range(vertex)]
    for line in content[1:]:
        line = line.strip('\n ')
        v, u, w = line.split(" ")
        v = int(v)
        u = int(u)
        w = int(w)
        if adj[v - 1][u - 1] is None or adj[v - 1][u - 1] < w:
            adj[v - 1][u - 1] = w
    return adj


def answer_func(adj):
    N = len(adj)

    arr = []
    v_in = {}
    v_in_sorted = {}
    max_dist = {}
    for v in range(N):
        v_in[v] = set((u for u in range(N) if adj[u][v] is not None))

    start = 0
    end = N

    while True:
        v = next((x for x in v_in if not v_in[x]), None)
        if v is None:
            return ":)"

        if v >= start:
            arr.append(v)
            max_dist[v] = 0
            v_in_sorted[v] = set((u for u in arr if adj[u][v] is not None))
            dist = [adj[u][v] + max_dist[u] for u in v_in_sorted[v]]
            if dist:
                max_dist[v] = max(dist)
        if v == end - 1:
            break

        v_out_to = [i for i, weight in enumerate(adj[v]) if weight is not None]
        for j in v_out_to:
            v_in[j].remove(v)

        v_in.pop(v)
        if not v_in:
            break

    if start in arr and end - 1 in arr:
        answer = max_dist[end - 1]
    else:
        return ":("
    return answer


adj = parse_in()
answer = answer_func(adj)

str_ = str(answer)
with open("maze.out.txt", 'w') as f:
    f.write(str_)
