"""Orbits
"""
import numpy as np
import networkx as nx

test_input_1 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
]

test_input_2 = [
    "COM)B",
    "B)C",
    "C)D",
    "D)E",
    "E)F",
    "B)G",
    "G)H",
    "D)I",
    "E)J",
    "J)K",
    "K)L",
    "K)YOU",
    "I)SAN",
]


def get_nodes_and_edges(orbit_input):
    edges = [tuple(connection.split(")")) for connection in orbit_input]
    nodes = {e for tup in edges for e in tup}
    return nodes, edges


def populate_graph(graph, orbit_input):
    nodes, edges = get_nodes_and_edges(orbit_input)

    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def load_input(path="input.dat"):
    return list(np.loadtxt(path, dtype="str"))


def main():
    orbit_input = load_input()

    # Part 1
    directed_orbit_graph = populate_graph(nx.DiGraph(), orbit_input)
    spl = dict(nx.all_pairs_shortest_path_length(directed_orbit_graph))

    n_orbits = sum(spl["COM"].values())
    print(f"Total number of orbits = {n_orbits}")

    # Part 2
    orbit_graph = populate_graph(nx.Graph(), orbit_input)
    spl = dict(nx.all_pairs_shortest_path_length(orbit_graph))
    n_transfers = spl["YOU"]["SAN"] - 2  # subtract because of definitions

    print(f"Minimum number of orbital transfers = {n_transfers}")


if __name__ == "__main__":
    main()
