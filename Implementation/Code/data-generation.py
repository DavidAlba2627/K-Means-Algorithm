import numpy as np
from sklearn.datasets import make_blobs

# Choosing parameters
Num_points = 10000
k = 5
np.random.seed(0)

# Creating dataset
X, y_true = make_blobs(n_samples=Num_points, centers=k, cluster_std=0.8, random_state=3)
