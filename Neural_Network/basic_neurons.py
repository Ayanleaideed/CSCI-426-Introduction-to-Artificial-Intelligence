# Author: Ayanle A 
# Date: 04/15/2025
# Description: This code implements my first simple neural network.

import numpy as np

"""
BASIC NEURAL NETWORK IMPLEMENTATION

This is my first neural network implementation! I'm creating a simple perceptron
that models the OR logical function. This is the foundation of neural networks -
a single artificial neuron that can make basic decisions.

The perceptron in this implementation uses:
1. Two input neurons (x₁ and x₂)
2. Fixed weights of 1 for both connections 
3. A bias of -1
4. A step activation function

The step activation function is defined as:
    g(x) = 0 if x < 0
    g(x) = 1 if x >= 0

The neuron computes: g(-1 + 1·x₁ + 1·x₂)

This creates a decision boundary that perfectly models the OR function:
- When both inputs are 0: -1 + 0 + 0 = -1, which is negative, so output = 0
- When one input is 1: -1 + 1 + 0 = 0 or -1 + 0 + 1 = 0, which is 0, so output = 1 
- When both inputs are 1: -1 + 1 + 1 = 1, which is positive, so output = 1

This matches the truth table for OR:
    x₁ | x₂ | Output
    ---------------
    0  | 0  | 0
    0  | 1  | 1
    1  | 0  | 1
    1  | 1  | 1
"""

# Simple function to compute the output of our neuron
def compute_output(x1, x2):
    """
    Computes the output of our perceptron for the given inputs.
    
    Args:
        x1: First input (0 or 1)
        x2: Second input (0 or 1)
        
    Returns:
        The output of the perceptron (0 or 1)
    """
    # Calculate the weighted sum plus bias
    weighted_sum = (-1 + 1*x1 + 1*x2)
    
    # Apply the step activation function
    if weighted_sum >= 0:
        return 1
    else:
        return 0

# Test our perceptron with all possible input combinations
print("\n===== MY FIRST NEURAL NETWORK: OR FUNCTION =====\n")
print("This perceptron implements the OR logic function")
print("The neuron computes: g(-1 + 1·x₁ + 1·x₂)\n")

print("OR Function Truth Table:")
print("----------------------")
print("x₁ | x₂ | Output")
print("----------------------")
print("0  | 0  |", compute_output(0, 0))
print("0  | 1  |", compute_output(0, 1))
print("1  | 0  |", compute_output(1, 0))
print("1  | 1  |", compute_output(1, 1))

# Demonstrate how the perceptron processes inputs step by step
print("\nDetailed calculation examples:")
print("------------------------------")

# Example 1: Both inputs are 0
x1, x2 = 0, 0
weighted_sum = -1 + 1*x1 + 1*x2
output = 1 if weighted_sum >= 0 else 0
print(f"Input [0,0]: -1 + 1·0 + 1·0 = {weighted_sum} → Output: {output}")

# Example 2: x1=0, x2=1
x1, x2 = 0, 1
weighted_sum = -1 + 1*x1 + 1*x2
output = 1 if weighted_sum >= 0 else 0
print(f"Input [0,1]: -1 + 1·0 + 1·1 = {weighted_sum} → Output: {output}")

# Example 3: x1=1, x2=0
x1, x2 = 1, 0
weighted_sum = -1 + 1*x1 + 1*x2
output = 1 if weighted_sum >= 0 else 0
print(f"Input [1,0]: -1 + 1·1 + 1·0 = {weighted_sum} → Output: {output}")

# Example 4: Both inputs are 1
x1, x2 = 1, 1
weighted_sum = -1 + 1*x1 + 1*x2
output = 1 if weighted_sum >= 0 else 0
print(f"Input [1,1]: -1 + 1·1 + 1·1 = {weighted_sum} → Output: {output}")

print("\nThis demonstrates how a single artificial neuron with")
print("appropriate weights and bias can implement the OR function!")