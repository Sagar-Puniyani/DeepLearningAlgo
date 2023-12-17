from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from KMeans import KMeans

centroid = [(4,4) , (-4,4) , (4,-4) , (-4,-4)]
cluster_std = [1,2,1,1]

X,y = make_blobs(n_samples=100,
                cluster_std=cluster_std,
                centers=centroid,
                n_features=3,
                random_state=2)


km = KMeans(n_cluster = 2 , max_iter = 100 )
km.fit_predict(X)



# plt.scatter(X[:,0] , X[:,1])
# plt.show()