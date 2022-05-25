import collections


class Vertex:
    def __init__(self, name, source=False, sink=False):
        self.name = name
        self.source = source
        self.sink = sink


class Edge:
    def __init__(self, start, end, capacity, is_return_flow=False):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.flow = 0
        self.is_return_flow = is_return_flow


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.vertices = set()
        self.network = dict()
        self.previous = dict()
        self.source = None
        self.sink = None

    def get_source(self):
        for vertex in self.vertices:
            if vertex.source:
                self.source = vertex
        return None

    def get_sink(self):
        for vertex in self.vertices:
            if vertex.sink:
                self.sink = vertex
        return None

    def get_path(self):
        vertex = self.sink.name
        res = [vertex]

        while vertex != self.source.name:
            prev = self.previous[vertex]
            res.append(prev)
            vertex = prev

        return res[::-1]

    def clear_previous(self):
        self.previous = dict()

    def add_vertex(self, name, source=False, sink=False):
        try:
            if source and sink:
                raise Exception("Vertex can't be a source and sink at the same time!")
            if source and self.get_source() is not None:
                raise Exception("Source already exist!")
            if sink and self.get_sink() is not None:
                raise Exception("Sink already exist!")
        except Exception as ex:
            print(f"Caught exception ---> {ex}")

        newVertex = Vertex(name, source, sink)
        self.vertices.add(newVertex)
        self.network[newVertex.name] = set()

    def add_edge(self, u, v, w):
        self.network[u].add(Edge(u, v, w))  # у всех вершин для диница уменьшить на 1 для теста
        self.network[v].add(Edge(v, u, 0, True))

    def add_vertexes(self, lst):
        for x in lst:
            if isinstance(x, collections.Iterable):
                self.add_vertex(*x)
            else:
                self.add_vertex(x)

    def get_edge(self, u, v):
        for edge in self.network[u]:
            if edge.start == u and edge.end == v:
                return edge
        return None

    def remove_edge(self, edge):
        self.network[edge.start].remove(edge)
