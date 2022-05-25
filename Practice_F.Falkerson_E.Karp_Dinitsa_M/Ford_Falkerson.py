import math


def dfs(graph, start, visited):
    visited.add(start)

    for next in graph.network[start]:
        if next not in visited:
            if next.capacity == 0 or next.end in visited:
                continue
            graph.previous[next.end] = next.start
            dfs(graph, next.end, visited)

    return visited


def get_max_flow(graph, path):
    max_flow = math.inf
    sign = 1
    for i in range(len(path) - 1):
        edge = graph.get_edge(path[i], path[i + 1])
        max_flow = min(max_flow, edge.capacity)
    return max_flow


def ford_falkerson(graph):
    graph.get_source()
    graph.get_sink()
    max_network_flow = 0

    while graph.sink.name in dfs(graph, graph.source.name, set()):
        path = graph.get_path()
        max_flow = get_max_flow(graph, path)
        max_network_flow += max_flow

        for i in range(len(path) - 1):
            edge = graph.get_edge(path[i], path[i + 1])
            return_edge = graph.get_edge(path[i + 1], path[i])

            sign = -1 if edge.is_return_flow else 1
            edge.flow += max_flow * sign
            return_edge.flow -= max_flow * sign

            edge.capacity -= max_flow * sign
            return_edge.capacity += max_flow * sign

        graph.clear_previous()

    return max_network_flow
