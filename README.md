# MST Algorithm Performance Testing

This project includes the implementation of three Minimum Spanning Tree (MST) algorithms: Kruskal's, Prim's, and Borůvka's. The goal is to test and compare the performance of these algorithms when applied to graphs generated using the Erdős-Rényi model.

## Performance Testing Overview

The performance tests evaluate the execution time of each algorithm for various graph configurations. The following factors are considered in the tests:

- **Number of Nodes**: The number of nodes in the graph, ranging from 50 to 500.
- **Edge Probability**: The probability that an edge exists between two nodes, with values of 0.1, 0.25, and 0.5.
- **Algorithms**: The three MST algorithms tested are:
  - **Kruskal's Algorithm**
  - **Prim's Algorithm**
  - **Borůvka's Algorithm**

## Technologies Used

- **Python 3.x**: The programming language used for implementation.
- **NetworkX**: A Python library for creating, analyzing, and visualizing graphs. Used for graph generation and MST algorithm implementations.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations. Used for visualizing the performance test results.
- **Random**: A Python module for generating random numbers, used to create random edge weights for the graph.
- **Time**: A Python module used to measure the execution time of each MST algorithm.

