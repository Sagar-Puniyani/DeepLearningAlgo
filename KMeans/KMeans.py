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

        for _ in range(0 , self.max_iter):
            # assign Cluster 
            cluster_group = self.assign_cluster(Dataset)
            print(cluster_group)
            # move centroid (calculation of the distances )
        
            # check finish   

    def assign_cluster(self , Dataset ) :
        cluster_group = []
        distance = []

        for row in Dataset:
            distance = []
            for centroid in self.centroid:
                distance.append(np.sqrt(np.dot(row-centroid , row-centroid)))
            

            Min_Distance = min(distance)
            Min_Index = distance.index(Min_Distance)
            cluster_group.append(Min_Index)
            distance.clear()

        return np.array(cluster_group)
    
    def Change_Cluster(self , Dataset , cluster_group ):
        Clusters = np.unique(cluster_group)

        for i in  Clusters:
            pass
