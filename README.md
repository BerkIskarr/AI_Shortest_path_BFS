# AI_Shortest_path_BFS

## Overview of Each Function

### Graph Creation (map function):
Reads a file line by line to identify connections between nodes marked by "#" symbols.
Stores connections in a temporary list (path), ensuring uniqueness.
Constructs a dictionary (graph) where each letter is a key, and its value is a list of connections to other letters.
Flexible approach enables handling changes in the graph structure.

### Breadth-First Search (BFS) Algorithm (bfs function):
Takes a graph and a starting point as parameters.
Utilizes a queue and a visited list to systematically explore nodes.
Adds neighbors to both the queue and visited list, iteratively marking nodes as visited.
Provides a generic BFS implementation adaptable to any graph and root.

### Shortest Path Finding (shortest_way function):
Finds the shortest path between two nodes in the graph.
Takes the graph, initial node, and goal node as parameters.
Limits the visited list with the ending node (goal) and constructs a one-way valid path (path_goal).
Handles cases where the ASCII value of the initial node is greater than that of the goal node by swapping nodes.
Demonstrates adaptability and correctness in pathfinding.

### Visited List Retrieval (visited_list function):
Returns the visited list limited by the goal node.
Internally used in the shortest_way function.
    
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Feel free to customize it further based on your preferences and the specific details of your project.
