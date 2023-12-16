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

        for i in range(self.max_iter):
            # assign Cluster 
            cluster_group = self.assign_cluster(Dataset)

            # move centroid 
            # check finish   

    def assign_cluster(self , Dataset ) :
        print("Enter")
        cluster_group = []
        distances = []

        for row in Dataset:
            distance = []
            for centroid in self.centroid:
                distance.append(np.sqrt(np.dot(row-centroid , row-centroid)))
                distances.append(distance)
        print("Distances")
        print(distances)

        return distances