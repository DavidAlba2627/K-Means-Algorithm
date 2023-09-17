# K-Means Algorithm: Codebase Overview

Welcome to the technical segment of my K-Means repository. Herein, I've presented Python scripts that operationalize the K-Means algorithm. Whether you're well-versed in coding or are in the nascent stages of your programming journey, I've endeavored to ensure these scripts are both informative and accessible.

## File Structure

1. **data_generation.py**: Generates synthetic data using the `make_blobs` function from `sklearn.datasets`. The number of data points and clusters can be adjusted using function parameters.

2. **k_means_function.py**: Contains the custom implementation of the K-Means clustering algorithm. This script provides the core logic for clustering data points based on their proximity to centroids.

3. **plotting_results.py**: Provides visualization functions to display the clustering results. The `plot_clusters` function visualizes data points colored by their assigned cluster and shows the centroids.

4. **k_means_demo.py**: This script ties everything together. It demonstrates the K-Means clustering algorithm using both the custom implementation and the `sklearn` implementation. The results are visualized using functions from `plotting_results.py`.

## Usage

To run the demonstration:

- Execute the `k_means_demo.py` script.
