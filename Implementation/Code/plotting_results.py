import matplotlib.pyplot as plt

def plot_clusters(X, Labels, Centroids, k=5, title="Clustering Results"):
    plt.figure(figsize=(7, 5))
    scatter = plt.scatter(X[:, 0], X[:, 1], c=Labels, cmap='spring')
    plt.scatter(Centroids[:, 0], Centroids[:, 1], c='black', s=200, alpha=0.5)
    plt.title(title)
    plt.legend(handles=scatter.legend_elements()[0], labels=range(k), title='Clusters')
    plt.show()

