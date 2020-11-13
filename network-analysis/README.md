# Network Analysis
- [Network Basics](#network-basics)

## Network Basics
### Definition
- Network/Graph: A representation of connections among a set of items
  - connections: edges
  - items: nodes
  ```python
  import networkx as nx
  G = nx.Graph()
  G.add_edge('A','B')
  G.add_edge('B','C')
  ```
  - if adding edges but nodes not exist, the graph will add the nodes automatically
- **Directed network**
  ```python
  G = nx.DiGraph()
  G.add_edge('B','A)
  G.add_edge('B', 'C')
  ```
- **Weighted networks**
  - Not all relationships are equal, some carry higher weight than others
  ```python
  G = nx.Graph()
  G.add_edge('A', 'B', weight=6)
  ```
- **Signed Networks**
  - edges are assigned positive / negative sign
  - e.g. can carry information about friendship/antagonism 
  ```python
  G.add_edge('A', 'B', sign='+')
  ```
- Edge Attributes
  ```python
  G.add_edge('A', 'B', relation='friend')
  ```
- **Multi Graph**
  - multiple edges can connect the same nodes (parallel edges)
  - a pair of nodes can have different types of relationships simultaneously
  ```python
  G = nx.MultiGraph()
  G.add_edge('A', 'B', relation='friend')
  G.add_edge('A', 'B', relation='neighbor')
  ```

  
  
  
  
  
  
  
  
