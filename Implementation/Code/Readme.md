# K-Means Algorithm: Codebase Overview

Welcome to the technical segment of my K-Means repository. This directory encapsulates the Python implementation of the K-Means clustering algorithm, a cornerstone in unsupervised machine learning. The scripts housed here are the culmination of rigorous development and testing, ensuring both accuracy and efficiency. They serve not only as a demonstration of the algorithm's capabilities but also as a modular foundation for further exploration or adaptation in diverse applications.

## File Structure

1. **data_generation.py**: Generates synthetic data using the `make_blobs` function from `sklearn.datasets`. The number of data points and clusters can be adjusted using function parameters.

2. **k_means_function.py**: Contains the custom implementation of the K-Means clustering algorithm. This script provides the core logic for clustering data points based on their proximity to centroids.

3. **plotting_results.py**: Provides visualization functions to display the clustering results. The `plot_clusters` function visualizes data points colored by their assigned cluster and shows the centroids.

4. **k_means_demo.py**: This script ties everything together. It demonstrates the K-Means clustering algorithm using both the custom implementation and the `sklearn` implementation. The results are visualized using functions from `plotting_results.py`.

## Usage

To run the demonstration:

- Execute the `k_means_demo.py` script.
