import collections
import math


def bfs(graph, start):
    visited, queue = set(), collections.deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        for next in graph.network[vertex]:
            if next.capacity == 0 or next.end in visited:
                continue
            graph.previous[next.end] = next.start
            visited.add(next.end)
            queue.append(next.end)
    return visited


def get_max_flow(graph, path):
    max_flow = math.inf
    sign = 1
    for i in range(len(path) - 1):
        edge = graph.get_edge(path[i], path[i + 1])
        max_flow = min(max_flow, edge.capacity)
    return max_flow


def edmonds_carp(graph):
    graph.get_source()
    graph.get_sink()
    max_network_flow = 0

    while graph.sink.name in bfs(graph, graph.source.name):
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
