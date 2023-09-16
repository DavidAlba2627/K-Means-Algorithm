import numpy as np

# Assigning one point to closest centroid
def getCluster(point, Centroids):
    Distances = []
    for j in range(len(Centroids)):
        Dif = point - Centroids[j]
        Distances.append(sum(Dif**2))
    Cluster = Distances.index(min(Distances))
    return Cluster
  
# Kmeans algorithm
def custom_kmeans(X, k):
    # Initializing the k centroids by random
    Centroids = np.array(X[np.random.choice(len(X), k, replace=False)])
    # Repeating K-means algorithm 30 times
    for m in range(30):
        # Assigning each point to the closest centroid
        Clusters = np.array([getCluster(point, Centroids) for point in X])
        # Updating centroids
        for i in range(len(Centroids)):
            Centroids[i] = np.mean(X[Clusters == i], axis=0)
    return Centroids, Clusters
