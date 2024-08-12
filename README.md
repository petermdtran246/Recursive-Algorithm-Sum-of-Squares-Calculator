# Recursive Algorithm: Sum of Squares Calculator
## Overview
This project contains a Python implementation of a recursive algorithm that calculates the sum of the squares of the first n positive integers. The algorithm is designed to compute the sum without using a closed-form formula, relying entirely on recursion.

## Contents
  -  sum_of_squares.py: Python script implementing the recursive algorithm.
  -  README.md: Documentation for the project.
  -  Example usage in the main block for testing the algorithm with different values of n.

## Algorithm Description
### Problem Statement
The task is to calculate the sum of the squares of the first n positive integers, using a recursive algorithm. The algorithm adds n^2 to the sum of squares of the integers from 1 to n−1.

### Recursive Logic
  - Base Case:  If n=1, the sum of squares is 1^2 =1.
  - Recursive Case: If n>1, the sum is the sum of squares of the integers from 1 to n−1 plus n^2
The recursive function performs the arithmetic for all the squares, ensuring the sum is correctly calculated.

## Testing
### Example Outputs
Run the script using the provided main block to see the output for the problem instances:
  -  Input: n=12
        -  Output: The sum of squares up to 12 is: 650
  -  Input: n=20
        -  Output: The sum of squares up to 20 is: 2870
   
## Asymptotic Analysis
### Recurrence Relation
The work performed by the algorithm in the worst case for a problem of size n is represented by the following recurrence relation:
                      T(n)=T(n−1)+1, with the base case: T(1)=1

### Asymptotic Complexity
Using the back-substitution method, we determine that:
                      T(n)=n
Thus, the time complexity of the algorithm is O(n).
