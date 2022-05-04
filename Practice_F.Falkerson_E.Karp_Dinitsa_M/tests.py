from Graph import Graph
from Dinitsa import dinitsa
from Edmonds_Carp import edmonds_carp
from Ford_Falkerson import ford_falkerson
from Scaling_The_Flow import max_flow_by_scaling
import copy

first_tested_graph = Graph(8)
edges = [(0, 5, 4), (0, 1, 12), (4, 5, 10), (5, 6, 8), (6, 7, 13), (1, 4, 7), (4, 7, 15), (3, 4, 2), (1, 3, 5),
         (3, 7, 18), (1, 2, 20), (2, 7, 19)]
first_tested_graph.add_vertexes([[0, True], [2, False, True], *[x for x in range(0, 8) if x not in [0, 2]]])
for edge in edges:
    first_tested_graph.add_edge(*edge)

second_tested_graph = Graph(6)
edges = [(0, 1, 3), (0, 2, 5), (2, 1, 4), (1, 3, 5), (2, 4, 2), (3, 4, 6), (3, 5, 5), (4, 5, 7)]

second_tested_graph.add_vertexes([[0, True], [5, False, True], 1, 2, 3, 4])
for edge in edges:
    second_tested_graph.add_edge(*edge)

third_tested_graph = Graph(16)
edges = [(0, 4, 8), (0, 5, 1), (0, 9, 6), (4, 5, 3), (4, 8, 5), (4, 9, 10), (5, 9, 6), (9, 8, 7), (9, 13, 7),
         (8, 13, 12), (13, 12, 7), (13, 15, 6), (12, 15, 7), (8, 12, 5), (12, 11, 8), (8, 7, 8), (11, 8, 12),
         (3, 4, 4), (7, 4, 10), (1, 3, 6), (1, 2, 6), (2, 6, 4), (2, 3, 3), (6, 3, 9), (3, 7, 4), (6, 10, 5),
         (7, 6, 8), (10, 7, 10), (7, 11, 5), (10, 14, 6), (11, 10, 8), (11, 14, 9)]

third_tested_graph.add_vertexes([[0, True], [15, False, True], *[i for i in range(1, 15)]])
for edge in edges:
    third_tested_graph.add_edge(*edge)


def test_dinitsa_alg_first():
    copy_graph = copy.deepcopy(first_tested_graph)
    assert dinitsa(copy_graph) == 12


def test_dinitsa_alg_second():
    copy_graph = copy.deepcopy(second_tested_graph)
    assert dinitsa(copy_graph) == 7


def test_dinitsa_alg_third():
    copy_graph = copy.deepcopy(third_tested_graph)
    assert dinitsa(copy_graph) == 13


def test_edmonds_carp_alg_first():
    copy_graph = copy.deepcopy(first_tested_graph)
    assert edmonds_carp(copy_graph) == 12


def test_edmonds_carp_alg_second():
    copy_graph = copy.deepcopy(second_tested_graph)
    assert edmonds_carp(copy_graph) == 7


def test_edmonds_carp_alg_third():
    copy_graph = copy.deepcopy(third_tested_graph)
    assert edmonds_carp(copy_graph) == 13


def test_ford_falkerson_alg_first():
    copy_graph = copy.deepcopy(first_tested_graph)
    assert ford_falkerson(copy_graph) == 12


def test_ford_falkerson_alg_second():
    copy_graph = copy.deepcopy(second_tested_graph)
    assert ford_falkerson(copy_graph) == 7


def test_ford_falkerson_alg_third():
    copy_graph = copy.deepcopy(third_tested_graph)
    assert ford_falkerson(copy_graph) == 13


def test_max_flow_by_scaling_alg_first():
    copy_graph = copy.deepcopy(first_tested_graph)
    assert max_flow_by_scaling(copy_graph) == 12


def test_max_flow_by_scaling_alg_second():
    copy_graph = copy.deepcopy(second_tested_graph)
    assert max_flow_by_scaling(copy_graph) == 7


def test_max_flow_by_scaling_alg_third():
    copy_graph = copy.deepcopy(third_tested_graph)
    assert max_flow_by_scaling(copy_graph) == 13
