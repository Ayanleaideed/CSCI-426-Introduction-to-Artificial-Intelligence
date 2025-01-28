# Author: Ayanle A
# Date: 01/26/2025
# Description: Breadth First Search Algorithm (with debugging prints)
# Course: CS344 - Artificial Intelligence
# School: NDSU - CSCI - Department - Computer Science Spring 2025
# ====================================================================================================

# using the deque from collections for efficient 
from collections import deque

def breadth_first_search(graph: dict, starting_node: int, goal: int) -> bool: 
    """
    Breadth First Search algorithm to find a target in a given graph.
    
    :param graph: Dictionary representing an adjacency list of the graph.
    :param starting_node: The node from which BFS starts.
    :param goal: The target node to search for.
    :return: True if goal is found, otherwise False.
    """

    # Use deque for efficient FIFO queue operations
    queue = deque([starting_node])

    # Create a set to track visited nodes
    visited = set([starting_node])  # Mark as visited when enqueued

    print(f"Starting BFS from node {starting_node}")
    
    while queue:
        # Remove the first element of the queue (FIFO behavior)
        first_node = queue.popleft()
        print(f"\nVisiting node: {first_node}")
        
        # Check if we found the goal
        if first_node == goal:
            print(f"Goal {goal} found! 🎯")
            return True 
        
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(first_node, []):
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited when enqueued
                queue.append(neighbor)
                print(f"Enqueuing neighbor: {neighbor}")

        # Debugging: Print queue state after each level
        print(f"Queue state: {list(queue)}")

    print(f"Goal {goal} not found in the graph. ❌")
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
goal = 6
found = breadth_first_search(graph_example, start, goal)
print(f"\nFinal Result: Goal {goal} found? {found}")  # Expected output: True
