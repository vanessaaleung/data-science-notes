# Clustering

| Method | Parameters | Usecase | Metric Used |
| ---    |  ---       | ---     | ---         |
| K-Means | Number of clusters | Gneral-purpose, even cluster size, not too many clusters | Distances between points |

- [KMeans](#kmeans)

## KMeans
_Clustering data by trying to separate samples in n groups of **equal variance**, minimizing inertia or within-cluster sum-of-squares_

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sum_{i=0}^{n}\min_{\mu_j&space;\in&space;C}(||x_i&space;-&space;\mu_j||^2)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\sum_{i=0}^{n}\min_{\mu_j&space;\in&space;C}(||x_i&space;-&space;\mu_j||^2)" title="\sum_{i=0}^{n}\min_{\mu_j \in C}(||x_i - \mu_j||^2)" /></a>
</p>

### Inertia
_How internally coherent clusters are_

- Drawbacks
  - Assumes that clusters are convexx and isotropic
  - Not normalized: just know lower are better and 0 is optimal
  - Curse of dimensionality: in high dimensional spaces, Euclidean distances tend to become inflated
    - Solution: run dimensionality reduction (e.g. PCA) before clustering

### 3 Steps
  1. Choose initial centroids
  2. Looping between:
      1. Assigns each sample to its nearest centroid
      2. Creates new centroids by taking the mean value of all samples in each previous centroid
    until difference between the old and new centroids is less than a threshold
