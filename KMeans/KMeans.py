class KMeans:
    def __init__(self , n_cluster = 2 , max_iter = 100) :
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.centroid = None

    