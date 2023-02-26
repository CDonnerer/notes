# 02 - Traditional ML Methods

## Tasks

- Node-level prediction
- Link-level prediction
- Graph-level prediction

## Tradtional ML

Features for nodes/links/graphs, train and apply

*Effective features* are key to achieving good performance

(focus is on undirected graphs)

E.g. Node-level prediction

- Given G = (V, E)
- learn mapping function : V -> R

## Node level features

E.g. structure & position of node
- Node degree
- Node centrality
- Clustering coefficient
- Graphlets

Node degree: number of edges of node (equal count)
Node centrality: takes *node importance* into account

Importance could be eigenvector centrality, betweenness centrality, etc

### Eigenvector centrality

- Node $v$ important if neighbours are important
- Centrality:

$c_v = \frac{1}{λ} ∑_{u ϵ N(v)} c_u$

it's recursive, rewrite as

$λ c = A c$

A ... adjacency matrix
c ... centrality vector
$λ$ ... Eigenvalue

### Betweenness centrality

- Node is important if it's on shortest path of other nodes

$c_v = ∑_{s ≂̸ v ≂̸ t} \frac{# shortest path s-t with v}{# shortest paths between s and t}$

### Closeness centrality

- Node is important if short path to all other nodes

$c_v = \frac{1}{∑_{u ≂̸ v} shortest path length between u and v}$

### Clustering coefficient

- How connected neighbouring nodes are

$e_v = \frac{# edges among neighbours}{k_v choose 2} ϵ [0,1]$

$k_v$ ... number of neighbours

### Graphlets

- Counting # of pre-specified subgraphs, i.e. graphlets
- Describe network structure around node

### Summary

Node level features:
- Importance based
- Structure based


## Link prediction task and features

- Predict new links based on existing links
- Design features for pair of nodes

### Link level features

- Distance based features

E.g. shortest path between two nodes

- Local neighourhood overlap

Number of common neighbours between two nodes
(Always zero if no overlap)

- Global neighbourhood overlap

Katz index: number of walk betwen pair of nodes

Compute via adjacency matrix:

$A_{uv} = 1$ if $u ϵ N(v)$

$P_{uv}^{(k)}$ ... number of walks of length K between u and v

Can show $P^k = A^k$

Katz index is sum over all walk lengths:

$S_{v_1 v_2} = ∑_{l=1}^∞ β^l A_{v_1 v_2}^l$
