import math
import numpy as np
import start as start


class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def sort_vertex(self):
        self.graph = sorted(self.graph, key=lambda x: x[2])

    def create_adjacency_matrix(self):
        matrix = np.zeros((self.V, self.V))
        matrix[:] = math.inf
        for vertex in self.graph:
            matrix[vertex[0]][vertex[1]] = matrix[vertex[1]][vertex[0]] = vertex[2]
        return matrix


def kruskal(graph):
    spanning_graph = []
    connected = set()
    isoleted = dict()
    graph.sort_vertex()

    for vertex in graph.graph:
        count_unconnected = len([1 for x in [0, 1] if vertex[x] not in connected])
        # проверка для исключения циклов в остове
        if count_unconnected == 2:
            # если обе вершины не соединены, то формируем в словаре ключ с номерами вершин
            # и связываем их с одним и тем же списком вершин
            isoleted[vertex[0]] = isoleted[vertex[1]] = [vertex[0], vertex[1]]  #
        elif count_unconnected == 1:
            if not isoleted.get(vertex[0]):  # если в словаре нет первой вершины, то
                # добавляем в список первую вершину и добавляем ключ с номером первой вершины
                isoleted[vertex[1]].append(vertex[0])
                isoleted[vertex[0]] = isoleted[vertex[1]]
            else:
                isoleted[vertex[0]].append(vertex[1])
                isoleted[vertex[1]] = isoleted[vertex[0]]
                # иначе, все то же самое делаем со второй вершиной
        if count_unconnected == 0:
            continue
        spanning_graph.append(vertex)  # добавляем ребро в остов
        connected.add(vertex[0])  # добавляем вершины в множество U
        connected.add(vertex[1])

    for vertex in graph.graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if vertex[1] not in isoleted[vertex[0]]:  # если вершины принадлежат разным группам, то объединяем
            spanning_graph.append(vertex)  # добавляем ребро в остов
            gr1 = isoleted[vertex[0]]
            isoleted[vertex[0]] += isoleted[vertex[1]]  # объединем списки двух групп вершин
            isoleted[vertex[1]] += gr1
    print(spanning_graph)


def prim(graph):
    def get_min(con):
        res = (-1, -1, math.inf)
        for v in con:
            for x in graph.graph + [[-1, -1, math.inf]]:
                if (x[0] == v and x[1] not in con) or (x[1] == v and x[0] not in con):
                    res = min(res, x, key=lambda t: t[2])
        return res

    spanning_graph = []
    connected = set()
    connected.add(graph.graph[0][0])
    while len(connected) < graph.V:
        vertex = get_min(connected)  # ребро с минимальным весом
        if vertex[2] == math.inf:  # если ребер нет, то остов построен
            break
        spanning_graph.append(vertex)  # добавляем ребро в остов
        connected.add(vertex[0])  # добавляем вершины в множество U
        connected.add(vertex[1])
    print(spanning_graph)


def deikstra(graph, start_vertex, end_vertex):
    def arg_min(last_stroke, viewed):
        amin = -1
        m = math.inf  # максимальное значение
        for i, t in enumerate(last_stroke):
            if t < m and i not in viewed:
                m = t
                amin = i

        return amin

    matrix = graph.create_adjacency_matrix()
    last_stroke = [math.inf] * graph.V  # последняя строка таблицы

    vertex = start_vertex  # стартовая вершина (нумерация с нуля)
    viewed = {vertex}  # просмотренные вершины
    last_stroke[vertex] = 0  # нулевой вес для стартовой вершины
    best_way = [0] * graph.V  # оптимальные связи между вершинами

    while vertex != -1:  # цикл, пока не просмотрим все вершины
        for j, dw in enumerate(matrix[vertex]):  # перебираем все связанные вершины с вершиной v
            if j not in viewed:  # если вершина еще не просмотрена
                w = last_stroke[vertex] + dw
                if w < last_stroke[j]:
                    last_stroke[j] = w
                    best_way[j] = vertex  # связываем вершину j с вершиной v

        vertex = arg_min(last_stroke, viewed)  # выбираем следующий узел с наименьшим весом
        if vertex >= 0:  # выбрана очередная вершина
            viewed.add(vertex)  # добавляем новую вершину в рассмотрение

    print(f"Длина минимального пути от вершины {start_vertex} до вершины {end_vertex} ---> {last_stroke[end_vertex]}")

    # формирование оптимального маршрута:
    start = start_vertex
    end = end_vertex
    P = [end]
    while end != start:
        end = best_way[P[-1]]
        P.append(end)
    print(f"Лучший маршрут от вершины {start_vertex} до вершины {end_vertex} ---> {P[::-1]}")





g = Graph(5)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 9)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 15)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 7)
prim(g)
kruskal(g)
deikstra(g, 0, 4)
