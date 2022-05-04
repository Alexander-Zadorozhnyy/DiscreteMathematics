import collections
import math


def bfs(graph, start, min_cap):
    visited, queue = set(), collections.deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for next in graph.network[vertex]:
            if next.capacity < min_cap or next.end in visited:
                continue
            graph.previous[next.end] = next.start
            visited.add(next.end)
            queue.append(next.end)
    return visited


def max_flow_by_scaling(graph):
    graph.get_source()
    graph.get_sink()
    max_network_flow = max_cap = 0
    for v in range(graph.V):
        for edge in graph.network[v]:
            max_cap = max(max_cap, edge.capacity)
    scale = 2 ** math.floor(math.log(max_cap, 2))  # текущий минимальный размер потока, который пытаемся пустить

    while scale >= 1:
        # while в Gf существует увеличивающий путь p с пропускной способностью не меньше, чем scale
        while graph.sink.name in bfs(graph, graph.source.name, scale):
            path = graph.get_path()

            # минимальная пропускная способность в увеличивающем пути
            min_cap = min([graph.get_edge(path[i], path[i + 1]).capacity for i in range(len(path) - 1)])
            max_network_flow += min_cap  # увеличить поток по рёбрам path на min_cap

            # обновить Gf
            for i in range(len(path) - 1):
                edge = graph.get_edge(path[i], path[i + 1])
                return_edge = graph.get_edge(path[i + 1], path[i])

                sign = -1 if edge.is_return_flow else 1

                edge.capacity -= min_cap * sign
                return_edge.capacity += min_cap * sign

        scale /= 2
    return max_network_flow
