import random 
import numpy as np 
class KMeans:
    def __init__(self , n_cluster = 2 , max_iter = 100) :
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.centroid = None

    def fit_predict(self , Dataset ):
        random_point = random.sample(range(0 , Dataset.shape[0]) , self.n_cluster)
        self.centroid = Dataset[random_point]
        print( self.centroid )

        for i in range(0 , self.max_iter):
            # assign Cluster 
            cluster_group = self.assign_cluster(Dataset)

            # move centroid (calculation of the distances )
            # check finish   

    def assign_cluster(self , Dataset ) :
        cluster_group = []
        distance = []

        for row in Dataset:
            distance = []
            for centroid in self.centroid:
                distance.append(np.sqrt(np.dot(row-centroid , row-centroid)))

            if distance[0] <= distance[1]:
                cluster_group.append(0)
            else:
                cluster_group.append(1)

        return cluster_group