# Visualization of Non-Numeric Data

## Graphs and Networks
### Graphs
- Directed v. undirected
- Cyclic v. acyclic
- Tree: minimally connected, n nodes, n-1 edges
- Hierarchy: acyclic direected graph

### Face
_The region bounded by cycle of edges, starting and ending at the smae node_

### Isomorphic
_Two different embeddings of the same graph

### Node Degree
_= Number of edges_

- Directed graph nodes have an in-degree and an out-deggree
- Social networks
  - many low degree nodes and fewer high deggree nodes
  - logarithmic, power-law graphs
  <img src="images/social-networks.png" height="250px">
  
### Adjacency Matrix
_Matrix representation of a graph_

<img src="images/adjacency-matrix.png" height="300px">

- Square matrix: # of rows & columns = # of nodes
- [i, j] is set to 1 if edge connects i and j
- Symmetric, unless directed graph
- Diagonal represent edge between node and itself

## Embedding Planar Graphs
### Planar Embedding
_Edges connecting the nodes don't cross_

<img src="images/planar-graph.png" height="300px">

### Graph Embedding
- Create the graphc Laplacian Matrix: Adjacency matrix with elements <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;L_{ij}=\frac{1}{degree(i)}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;L_{ij}=\frac{1}{degree(i)}" title="L_{ij}=\frac{1}{degree(i)}" /></a> for an edge between i and j

  <img src="images/laplacian-matrix.png" height="200px">

- Zero out the rows for nodes we have already positioned, subtract it from the identity matrix

  <img src="images/zero-out.png" height="200px">
- Create linear systems of equations
  - Solve <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Ax=B_x" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Ax=B_x" title="Ax=B_x" /></a> for x coordinates
  - Solve <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;Ay=B_y" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;Ay=B_y" title="Ay=B_y" /></a> for y coordinates

  <img src="images/linear-systems.png" height="200px">
  
