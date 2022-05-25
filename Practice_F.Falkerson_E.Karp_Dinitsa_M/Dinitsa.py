import collections
import math


def bfs(graph):
    queue = collections.deque([graph.source.name])
    d = [math.inf for _ in range(graph.V)]  # заполняем массив d значениями, равными ∞
    d[graph.source.name] = 0

    while len(queue) != 0:
        vertex = queue.popleft()
        for next in graph.network[vertex]:
            if next.flow < next.capacity and d[next.end] == math.inf:
                # next.capacity == 0 and d[next.end] == math.inf:
                d[next.end] = d[next.start] + 1
                queue.append(next.end)

    return d[graph.sink.name] != math.inf, d


# поиск блокирующего потока
# vertex — номер вершины
# min_cap — минимальная пропускная способность дополняющей сети на пройденном dfs пути
def dfs(graph, vertex, min_cap, p, d):
    delta = 0
    if vertex == graph.sink.name or min_cap == 0:
        return p, min_cap
    for v in range(p[vertex], graph.V):
        edge = graph.get_edge(vertex, v)
        if edge is not None and edge.is_return_flow:
            continue
        return_edge = graph.get_edge(v, vertex)
        if d[v] == d[vertex] + 1:  # это условие эквивалентно поиску во вспомогательной слоистой сети
            p, delta = dfs(graph, v, min(min_cap, edge.capacity - edge.flow) if edge != None else 0, p, d)
        if delta != 0:
            edge.flow += delta  # насыщаем рёбра по пути dfs
            return_edge.flow -= delta
            return p, delta
    p[vertex] += 1
    return p, 0  # O(n * m)


def dinitsa(graph):
    graph.get_source()
    graph.get_sink()
    max_network_flow = 0

    res_bfs, d = bfs(graph)
    while res_bfs:  # пересчитываем d[i], заодно проверяем достижима ли t из s
        p = [0 for _ in range(graph.V)]
        p, flow = dfs(graph, graph.source.name, math.inf, p, d)
        while flow != 0:
            max_network_flow += flow
            p, flow = dfs(graph, graph.source.name, math.inf, p, d)
        res_bfs, d = bfs(graph)

    return max_network_flow
