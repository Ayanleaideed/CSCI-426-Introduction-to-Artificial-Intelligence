# Author: Ayanle A 
# Date: 01/26/2025
# Description: Depth First Search Algorithm
# Course: CS344 - Artificial Intelligence
# School: NDSU - CSCI - Department - Computer Science Spring 2025
# ====================================================================================================

def depth_first_search(graph: dict, starting_node: int, goal: int) -> bool:
    """
    Depth First Search algorithm to find a target in a given graph.
    
    :param graph: Dictionary representing an adjacency list of the graph.
    :param starting_node: The node from which DFS starts.
    :param goal: The target node to search for.
    :return: True if goal is found, otherwise False.
    """
    
    # Create a stack for DFS
    stack = [starting_node]
    # Create a set to track visited nodes
    visited = set()
    
    while stack:
        # Pop the last inserted node (LIFO behavior)
        top_node = stack.pop()
        print(f"Exploring node: {top_node}")
        # Check if the goal is found
        if top_node == goal:
            print(f"Goal node {goal} found!")
            return True  # Goal found
        
        # If the node has not been visited, process it
        if top_node not in visited:
            visited.add(top_node)
            print(f"Visited nodes: {visited}")
            
            # Add neighbors to the stack (avoiding revisits)
            for neighbor in graph.get(top_node, []):
                if neighbor not in visited:
                    print(f"Adding neighbor {neighbor} of node {top_node} to the stack")
                    stack.append(neighbor)
    
    print(f"Goal node {goal} not found in the graph.")
    return False  # Goal not found

# Example graph represented as an adjacency list
graph_example = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

# Example usage
start = 1
goal = 7
found = depth_first_search(graph_example, start, goal)
print(f"Goal {goal} found: {found}")  # Expected output: True
