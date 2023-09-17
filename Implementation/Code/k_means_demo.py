import numpy as np
from sklearn.cluster import KMeans
from k_means_function import custom_kmeans
from data_generation import generate_data
from plotting_results import plot_clusters

def main():
    # Generate data with specific parameters
    X, y_true = generate_data(Num_points=10000, k=5)

    # Using custom KMeans
    custom_centroids, custom_labels = custom_kmeans(X, 5)
    plot_clusters(X, custom_labels, custom_centroids, title="Custom KMeans Clustering")

    # Using KMeans from the sklearn library
    kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
    sklearn_labels = kmeans.labels_
    sklearn_centroids = kmeans.cluster_centers_
    plot_clusters(X, sklearn_labels, sklearn_centroids, title="Sklearn KMeans Clustering")

if __name__ == "__main__":
    main()
