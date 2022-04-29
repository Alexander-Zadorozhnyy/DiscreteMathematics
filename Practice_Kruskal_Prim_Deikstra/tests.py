from All_Algorithms import Graph, kruskal, prim, deikstra

first_tested_graph = Graph(7)
first_tested_graph.add_edge(0, 1, 1)
first_tested_graph.add_edge(0, 4, 9)
first_tested_graph.add_edge(1, 2, 7)
first_tested_graph.add_edge(1, 6, 8)
first_tested_graph.add_edge(2, 6, 10)
first_tested_graph.add_edge(2, 3, 4)
first_tested_graph.add_edge(3, 4, 3)
first_tested_graph.add_edge(3, 5, 5)
first_tested_graph.add_edge(4, 5, 2)
first_tested_graph.add_edge(5, 6, 6)

second_tested_graph = Graph(8)
second_tested_graph.add_edge(0, 5, 4)
second_tested_graph.add_edge(0, 1, 12)
second_tested_graph.add_edge(4, 5, 10)
second_tested_graph.add_edge(5, 6, 8)
second_tested_graph.add_edge(6, 7, 13)
second_tested_graph.add_edge(1, 4, 7)
second_tested_graph.add_edge(4, 7, 15)
second_tested_graph.add_edge(3, 4, 2)
second_tested_graph.add_edge(1, 3, 5)
second_tested_graph.add_edge(3, 7, 18)
second_tested_graph.add_edge(1, 2, 20)
second_tested_graph.add_edge(2, 7, 19)


def is_answer_matching(ans, lst_res):
    all_edges_spanning_tree = [[x[0], x[1]] for x in lst_res]
    return all([sublist in ans for sublist in all_edges_spanning_tree])


def sum_of_the_path(lst):
    return sum([x[2] for x in lst])


def test_kruskal_alg_first():
    right_answer = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    kruskal_result = kruskal(first_tested_graph)

    assert is_answer_matching(right_answer, kruskal_result)
    assert sum_of_the_path(kruskal_result) == 23


def test_kruskal_alg_second():
    right_answer = [[0, 5], [4, 5], [3, 4], [1, 3], [5, 6], [6, 7], [2, 7]]
    kruskal_result = kruskal(second_tested_graph)

    assert is_answer_matching(right_answer, kruskal_result)
    assert sum_of_the_path(kruskal_result) == 61


def test_prim_alg_first():
    right_answer = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    prim_result = prim(first_tested_graph)

    assert is_answer_matching(right_answer, prim_result)
    assert sum_of_the_path(prim_result) == 23


def test_prim_alg_second():
    right_answer = [[0, 5], [4, 5], [3, 4], [1, 3], [5, 6], [6, 7], [2, 7]]
    prim_result = prim(second_tested_graph)

    assert is_answer_matching(right_answer, prim_result)
    assert sum_of_the_path(prim_result) == 61


def test_deikstra_alg_first():
    right_answer = [0, 1, 6]
    deikstra_result = deikstra(first_tested_graph, 0, 6)

    assert set(deikstra_result[0]) == set(right_answer)
    assert deikstra_result[1] == 9


def test_deikstra_alg_second():
    right_answer = [0, 1, 2, 5]
    deikstra_result = deikstra(second_tested_graph, 5, 2)

    assert set(deikstra_result[0]) == set(right_answer)
    assert deikstra_result[1] == 36
