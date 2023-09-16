import matplotlib.pyplot as plt

def plot_clusters(X, Labels, Centroids, title="Clustering Results"):
    plt.figure(figsize=(7, 5))
    plt.scatter(X[:, 0], X[:, 1], c=Labels, cmap='spring')
    plt.scatter(Centroids[:, 0], Centroids[:, 1], c='black', s=200, alpha=0.5)
    plt.title(title)
    plt.show()
