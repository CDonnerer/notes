# 01 - Intro, ML for Graphs

Graphs - language for entities with interactions

Many types of natural data are graphs

Rich relational structure, when presented as relational graphs, for better modelling

Modern ML: mostly sequences & grids -> Graphs are frontier for DL


## Representation learning for graphs

Map graph nodes to embeddings - similar nodes embedded close together.

Methods:

- Traditional: Graphlets, Graph Kernels
- Node embeddings: DeepWalk, Node2Vec
- GNN: GCN, GraphSage


## Tasks

- Graph level:
	- Classification
	- Generation
- Node level:
	- Classification
- Edge level:
	- Link prediction (missing connection?)
- Clustering:
	- Do nodes from a community

## Graph representation

- Objects: nodes, vertices (N)
- Interactions: links, edges (E)
- System: network, graph G(N, E)

Links:
- Undirected (symmetrical, reciprocal)
- Directed (arcs)

Heterogeneous graph: $G = (V, E, R, T)$
- Nodes with nodes types $V$
- Edges with relations $v_i, r, v_j \epsilon E$
- Node type $T(v_i)$
- Relation type $r \epsilon R$

Node degree, $k_i$:
- (Undirected) Number of edges adjacent to node i
- (Directed) In-degree and out-degree (and total)

Bipartite graph:
- Nodes can be divided into disjoint sets U, V (independent)
- E.g. Authors to papers, recipes to ingredients
- Projections

Adjacency matrix
- N x N matrix, {1, 0} for link existing
- Undirected: symmetric matrix
- Directed: not
- Sparse

Edge list:
- List of edges

Adjacency list:
- 1: {3, 4}
- 3: {2, 4}

Node and edge attributes:
- Weight (frequency of comms)
- Ranking (best friend, second)
- Type (relative, co-worker)
- Sign

Connectivity
- Disconnected UG: two or more connected components
- Strongly connected DG: path from / to each node
- Weakly connected DG: no direct paths between nodes
- Strongly connected components (SCCs) (in-component / out-component)
