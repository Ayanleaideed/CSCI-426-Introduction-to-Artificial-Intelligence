# Author: Ayanle A
# Date: 01/28/2025
# Description: Breadth First Search Algorithm (with debugging prints)
# Course: CS344 - Artificial Intelligence
# School: NDSU - CSCI - Department - Computer Science Spring 2025
# ====================================================================================================

import heapq 
from collections import deque # Importing deque from collections
from typing import List, Tuple  # Importing List and Tuple types

# Implementing Greedy Best First Search Algorithm
class Graph:
    def __init__(self):
        self.edges = {}  # Adjacency list representation
        self.heuristics = {}  # Heuristic values for each node

    def add_edge(self, node, neighbor, cost=1):
        if node not in self.edges:
            self.edges[node] = []
        self.edges[node].append((neighbor, cost))

    def set_heuristic(self, node, h_value):
        self.heuristics[node] = h_value

    def greedy_best_first_search(self, start, goal):
        open_list = []  # Priority queue (min-heap)
        heapq.heappush(open_list, (self.heuristics[start], start))  # (heuristic, node)
        
        came_from = {}  # To reconstruct the path
        came_from[start] = None
        closed_list = set()

        while open_list:
            _, current = heapq.heappop(open_list)  # Node with the lowest heuristic

            if current == goal:
                return self.reconstruct_path(came_from, goal)  # Goal reached
            
            closed_list.add(current)

            for neighbor, _ in self.edges.get(current, []):
                if neighbor in closed_list:
                    continue  # Skip already visited nodes
                
                if neighbor not in [node for _, node in open_list]:  # Not in open list
                    came_from[neighbor] = current
                    heapq.heappush(open_list, (self.heuristics[neighbor], neighbor))

        return None  # No path found

    def reconstruct_path(self, came_from, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        return path[::-1]  # Reverse the path

# Example Usage
graph = Graph()

# Adding edges (Graph Structure)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'G')
graph.add_edge('F', 'G')

# Setting heuristic values (Straight-line distance to goal)
graph.set_heuristic('A', 6)
graph.set_heuristic('B', 4)
graph.set_heuristic('C', 4)
graph.set_heuristic('D', 2)
graph.set_heuristic('E', 2)
graph.set_heuristic('F', 2)
graph.set_heuristic('G', 0)  # Goal node

# Running Greedy Best-First Search
start_node = 'A'
goal_node = 'G'
path = graph.greedy_best_first_search(start_node, goal_node)

# Output the result
if path:
    print("Path found:", " → ".join(path))
else:
    print("No path found!")
