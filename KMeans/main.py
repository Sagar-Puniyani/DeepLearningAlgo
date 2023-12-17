from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from KMeans import KMeans

centroid = [(4,4) , (-4,4) , (4,-4) , (-4,-4)]
cluster_std = [1,1,1,1]

X,y = make_blobs(n_samples=100,
                cluster_std=cluster_std,
                centers=centroid,
                n_features=3,
                random_state=2)


km = KMeans(n_cluster = 4 , max_iter = 100 )
y_pred = km.fit_predict(X)



plt.scatter(X[y_pred == 0,0] , X[y_pred == 0,1] , color='red')
plt.scatter(X[y_pred == 1,0] , X[y_pred == 1,1] , color='yellow')
plt.scatter(X[y_pred == 2,0] , X[y_pred == 2,1] , color='blue')
plt.scatter(X[y_pred == 3,0] , X[y_pred == 3,1] , color='green')

plt.show()