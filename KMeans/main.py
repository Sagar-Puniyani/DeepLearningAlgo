from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

centroid = [(4,4) , (-4,4) , (4,-4) , (-4,-4)]
cluster_std = [1,2,1,1]

X,y = make_blobs(n_samples=100,
                cluster_std=cluster_std,
                centers=centroid,
                n_features=3,
                random_state=2)

plt.scatter(X[:,0] , X[:,1])
plt.show()