""""
clase python que permite realiza el algoritmo de Queyranne
en el cual se relaizan las k-particiones de un conjunto de datos
"""
import numpy as np
import random
import itertools as iter
import math


class Queyranne:
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.partitions = []
        self.centroids = []
        self.clusters = []
        self.cluster_size = []
        self.cluster_mean = []
        self.cluster_std = []
        self.cluster_min = []
        self.cluster_max = []
        self.cluster_median = []
        self.cluster_mode = []
        self.cluster_var = []
        self.cluster_iqr = []
        self.cluster_skew = []
        self.cluster_kurtosis = []
        self.cluster_entropy = []
        self.cluster_entropy_norm = []
        self.cluster_entropy_norm_log = []
        self.cluster_entropy_norm_log2 = []
        self.cluster_entropy_norm_log10 = []
        self.cluster_entropy_norm_log100 = []
        self.cluster_entropy_norm_log1000 = []
        self.cluster_entropy_norm_log10000 = []
        self.cluster_entropy_norm_log100000 = []
        self.cluster_entropy_norm_log1000000 = []
        self.cluster_entropy_norm_log10000000 = []
        self.cluster_entropy_norm_log100000000 = []
        self.cluster_entropy_norm_log1000000000 = []
        self.cluster_entropy_norm_log10000000000 = []
        self.cluster_entropy_norm_log100000000000 = []
        self.cluster_entropy_norm_log1000000000000 = []
        self.cluster_entropy_norm_log10000000000000 = []
        self.cluster_entropy_norm_log100000000000000 = []
        self.cluster_entropy_norm_log1000000000000000 = []
        self.cluster_entropy_norm_log10000000000000000 = []

    def run(self):
      """
      metodo que permite ejecutar el algoritmo de Queyranne
      """
      self.partitions = self.k_partitions()

    def k_partitions(self):
      """
      metodo que permite realizar las k-particiones de un conjunto de datos
      """
      partitions = []
      for i in range(self.k):
        partitions.append(self.data[i::self.k])
        print(partitions)
      return partitions

    def permutations(self):
      """
      metodo que permite realizar las permutaciones de un conjunto de datos
      """
      permutations = iter.permutations(self.data)
      
      return [permutations]

if __name__ == '__main__':
  """
  metodo principal que permite ejecutar el algoritmo de Queyranne
  """
  data = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  k = 3
  queyranne = Queyranne(data, k)
  queyranne.run()
  print(queyranne.partitions)
  """"
  funcion lambda de permutaciones
  """
  permutations = list(map(lambda x: list(x), queyranne.permutations()))
  print(permutations)