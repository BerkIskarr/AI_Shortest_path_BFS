'''
    The algorithm consists of three main sections.

    In the first section, the `map` function is responsible for creating a graph. 
    It reads a file line by line and identifies connections between nodes indicated by "#" symbols.
    Connections are stored in a temporary list (`path`), ensuring uniqueness. After processing all lines,
    it constructs a dictionary (`graph`) where each letter is a key, and its value is a list of connections 
    to other letters. This flexible approach allows the `map` function to handle changes in the graph structure. 
    The function returns the dictionary of connections.

    The second section implements the Breadth-First Search (BFS) algorithm. The `bfs` function takes the graph 
    and a starting point as parameters. It utilizes a queue and a visited list to explore nodes systematically. 
    Starting from the initial node, it adds neighbors to both the queue and the visited list, iteratively exploring
    and marking nodes as visited. This section provides a generic BFS implementation that works with any given graph and root.

    The third section contains the `shortest_way` function, which finds the shortest path between two nodes in the graph.
    It takes the graph, initial node, and goal node as parameters. The function limits the visited list with the ending
    node (`goal`) and constructs a one-way valid path (`path_goal`). Once the goal node is reached, the complete path is
    constructed by iterating over the connections in the graph. An important consideration is handling cases where the 
    ASCII value of the initial node is greater than that of the goal node. In such cases, the function swaps the initial 
    and goal nodes, ensuring correct pathfinding.

    Additionally, the code includes a function (`visited_list`) that returns the visited list limited by the goal node. 
    This function is internally used in the `shortest_way` function.

    The overall algorithm demonstrates effectiveness by leveraging BFS properties to find the shortest path. The dynamic 
    graph creation and the adaptable nature of the functions contribute to a robust solution capable of handling various scenarios.
'''
import numpy as ny
# creation of the graph
def map(file):
    with open(file, "r+") as graph_file:
        list=[]
        lines_file=graph_file.readlines()
        every_letter=[]
        for line in lines_file:
            temp_list=[]
            for count, character in enumerate(line):
                # adds only nodes coming after the char '#'
                if character=="#":
                    temp_list.append(line[count+1])
                    every_letter.append(line[count+1])
            list.append(temp_list)
    # sorts and clears duplicates
    every_letter= ny.unique(every_letter) 
    dicts={}
    path=[]
    for letter in every_letter:
        dicts[letter]=path
    # creates connections and adds to the belonging key node
    for key in dicts:
        path=[]
        for nested_list in list:
            if key == nested_list[0]:
                path.append(nested_list[1])
            if key == nested_list[1] and key not in path:
                path.append(nested_list[0])
            dicts[key]=path
    return dicts

# the Breadth-first search algorithm
def bfs(graph,start):
    queue=[]
    visited=[]
    queue.append(start)
    visited.append(start)
    while queue:
        first= queue[0]
        # adds to both queue and visited
        for neighbour in graph[first]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
        # removes the already explored node
        queue.remove(first)
    
    return visited

reverse = False

def shortest_way(graph, initial, goal):
    visited = bfs(graph, initial)
    path_goal = []
    ways = []
   

    # create a new visited list limited by the goal node
    path_goal.append(initial)
    for element in visited:
        for key in graph:
            if element in graph[key] and element not in path_goal:
                path_goal.append(element)
        # if goal is reached
        if path_goal[-1] == goal:
            ways.append(path_goal[-1])
            for news in ways:
                for char in path_goal:
                    if news in graph[char] and char not in ways:
                        ways.append(char)
                        break
            
                    # if the initial is bigger than goal, reverse the list                   
                    if ways[-1] == initial:
                        ways.reverse()
                        return ways
                      

# just to return visited list that is limited by the goal node 
# (same function used in shortest_way for creating the path_goal)
def visited_list(graph, initial, goal):
    visited = bfs(graph, initial)
    visited_goal = []
    visited_goal.append(initial)
    for element in visited:
        for key in graph:
            if element in graph[key] and element not in visited_goal:
                visited_goal.append(element)
        if visited_goal[-1] == goal:
            return visited_goal

while True:
    try:
        start = input("The starting point >> ").upper()
        end = input("The goal point >> ").upper()
        graphics = map("Graph_info.txt")
        # If the goal is not found the graph will change therefore save the original version to display
        graph_copy=graphics.copy()
        path = shortest_way(graphics, start, end)
        visited = bfs(graph_copy,start)
        print("The graph is >>", graph_copy,"\nThe visited list is >>", visited,"\nThe path is >>", path)
        break
    except:
        print("No valid path found from", start, "to", end)
    
       
    
    
