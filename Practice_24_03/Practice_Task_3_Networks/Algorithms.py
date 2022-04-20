from Practice_Task_2_Graph.All_Algorithms import Graph
import math


class OrientedGraph(Graph):
    def create_adjacency_matrix(self):
        matrix = []
        for i in range(self.V):
            matrix.append(list())
            for j in range(self.V):
                matrix[i].append([0, 0, 1])

        for vertex in self.graph:
            matrix[vertex[0]][vertex[1]] = [vertex[2], 0, 1]
            matrix[vertex[1]][vertex[0]] = [vertex[2], 0, -1]
        return matrix


def get_max_vertex(k, matrix, viewed):
    m = 0  # наименьшее допустимое значение
    v = -1
    for i, w in enumerate(matrix[k]):
        if i in viewed:
            continue
        if w[2] == 1 and m < w[0]:  # движение по стрелке
            m = w[0]
            v = i
        elif w[2] == -1 and m < w[1]:  # движение против стрелки
            m = w[1]
            v = i

    return v


def get_max_flow(T):
    return min(T, key=lambda x: x[0])


def update_matrix(matrix, T, f):
    for t in T:
        if t[1] == -1:  # это исток
            continue

        sign = matrix[t[2]][t[1]][2]  # направление движения

        # меняем веса в таблице для (i,j) и (j,i)
        matrix[t[1]][t[2]][0] -= f[0] * sign
        matrix[t[1]][t[2]][1] += f[0] * sign

        matrix[t[2]][t[1]][0] -= f[0] * sign
        matrix[t[2]][t[1]][1] += f[0] * sign


def ford_falkerson(graph, start_vertex, end_vertex):
    matrix = graph.create_adjacency_matrix()
    max_route = []  # максимальные потоки найденных маршрутов

    j = start_vertex
    while j != -1:
        k = start_vertex  # стартовая вершина (нумерация с нуля)
        T = [(math.inf, -1, start_vertex)]  # метки маршрута с включенной первой меткой (a, from, vertex)
        viewed = {start_vertex}  # множество просмотренных вершин

        while k != end_vertex:  # пока не дошли до стока
            j = get_max_vertex(k, matrix, viewed)  # выбираем вершину с наибольшей пропускной способностью
            if j == -1:  # если следующих вершин нет
                if k == start_vertex:  # и мы на истоке, то
                    break  # завершаем поиск маршрутов
                else:  # иначе, переходим к предыдущей вершине
                    k = T.pop()[2]
                    continue

            c = matrix[k][j][0] if matrix[k][j][2] == 1 else matrix[k][j][1]  # определяем текущий поток
            T.append((c, j, k))  # добавляем метку маршрута
            viewed.add(j)  # запоминаем вершину как просмотренную

            if j == end_vertex:  # если дошди до стока
                max_route.append(get_max_flow(T))  # находим максимальную пропускную способность маршрута
                update_matrix(matrix, T, max_route[-1])  # обновляем веса дуг
                break

            k = j

    print(f"Максимальный поток равен: {sum([x[0] for x in max_route])}")

# 1.a
'''g = OrientedGraph(6)
g.add_edge(0, 1, 7)
g.add_edge(0, 2, 7)
g.add_edge(2, 1, 5)
g.add_edge(1, 3, 4)
g.add_edge(2, 4, 10)
g.add_edge(1, 4, 3)
g.add_edge(4, 3, 11)
g.add_edge(4, 5, 4)
g.add_edge(3, 5, 8)
ford_falkerson(g, 0, 5)'''

g = OrientedGraph(16)
g.add_edge(0, 4, 8)
g.add_edge(0, 5, 1)
g.add_edge(0, 9, 6)
g.add_edge(4, 5, 3)
g.add_edge(4, 8, 5)
g.add_edge(4, 9, 10)
g.add_edge(5, 9, 6)
g.add_edge(9, 8, 7)
g.add_edge(9, 13, 7)
g.add_edge(8, 13, 12)
g.add_edge(13, 12, 7)
g.add_edge(13, 15, 6)
g.add_edge(12, 15, 7)
g.add_edge(8, 12, 5)
g.add_edge(12, 11, 8)
g.add_edge(8, 7, 8)
g.add_edge(11, 8, 12)
g.add_edge(3, 4, 4)
g.add_edge(7, 4, 10)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 6)
g.add_edge(2, 6, 4)
g.add_edge(2, 3, 3)
g.add_edge(6, 3, 9)
g.add_edge(3, 7, 4)
g.add_edge(6, 10, 5)
g.add_edge(7, 6, 8)
g.add_edge(10, 7, 10)
g.add_edge(7, 11, 5)
g.add_edge(10, 14, 6)
g.add_edge(11, 10, 8)
g.add_edge(11, 14, 9)
ford_falkerson(g, 0, 15) # 13
ford_falkerson(g, 0, 14) # 13




