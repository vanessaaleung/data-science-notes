# Clustering

| Method | Parameters | Usecase | Metric Used |
| ---    |  ---       | ---     | ---         |
| K-Means | Number of clusters | Gneral-purpose, even cluster size, not too many clusters | Distances between points |
| DBSCAN  | neighborhood size  | Non-flat geometry, uneven cluster sizes | Distances between nearest points |

- [KMeans](#kmeans)
- [DBSCAN](#DBSCAN)

## KMeans
_Clustering data by trying to separate samples in n groups of **equal variance**, minimizing inertia or within-cluster sum-of-squares_

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sum_{i=0}^{n}\min_{\mu_j&space;\in&space;C}(||x_i&space;-&space;\mu_j||^2)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\sum_{i=0}^{n}\min_{\mu_j&space;\in&space;C}(||x_i&space;-&space;\mu_j||^2)" title="\sum_{i=0}^{n}\min_{\mu_j \in C}(||x_i - \mu_j||^2)" /></a>
</p>

- non-overlapping clusters without any internal cluster structure

### Inertia
_How internally coherent clusters are_

- Drawbacks
  - Assumes that clusters are convexx and isotropic
  - Not normalized: just know lower are better and 0 is optimal
  - Curse of dimensionality: in high dimensional spaces, Euclidean distances tend to become inflated
    - Solution: run dimensionality reduction (e.g. PCA) before clustering

### 3 Steps
1. Choose initial centroids
  - random data points, highly volatile
  - k-means++: randomly select first centroid, choose the subsequent ones based on a probability proportional to the squared distance away from a given point's nearest existing centroid
2. Looping between:
    1. Assigns each sample to its nearest centroid
    2. Creates new centroids by taking the mean value of all samples in each previous centroid
  until difference between the old and new centroids is less than a threshold

- Average complexitiy: O(k n T), n: number of samples, T: number of iterations

### MiniBatchMeans
_Incremental updates of centers positions using mini-batches_

## DBSCAN
_Views clusters as areas of high density separated by areas of low density_
- Density-Based Spatial Clustering of Applications with Noise
- clusters found by DBSCAN can be any shape, as opposed to k-means which assumes that clusters are convex shaped
  - can find a cluster completely surrounded by another cluster
- A cluster is a set of core samples
  - core samples: samples that are in areas of high density
- Deterministic: always generating the same clusters when given the same data in the same order
- Has a notion to noise: robust to outliers
- Doesn't require specification of number of clusters
- scikit-learn: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN
