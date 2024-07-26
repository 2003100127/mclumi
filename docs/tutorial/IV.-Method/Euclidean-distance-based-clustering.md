## Euclidean distance

Apart from the graph-based clustering methods in mclUMI, we implemented several Euclidean distance-based clustering methods, including density-based spatial clustering of applications with noise (DBSCAN)[^1], balanced iterative reducing and clustering using hierarchies (BIRCH)[^2], and Affinity propagation[^3].

These methods do not need to build a UMI graph to remove PCR duplicates.

UMI sequences are represented by one-hot encodings, which are then flatten to be fed into distance-based clustering algorithms. Our results demonstrate that methods implemented in mclUMI together with DBSCAN, Birch, and Directional show an apparent advantage of UMI collapsing over Unique and Adjacency in all the six sequencing settings.

Users can access the Euclidean distance-based clustering methods by passing the following parameters to the YAML file.

For DBSCAN
```yaml
dbscan_eps: 1.5
dbscan_min_spl: 1
```

For BIRCH
```yaml
birch_thres: 1.8
birch_n_clusters: None
```

For Affinity propagation, there are no parameters to impose on.

[^1]: Schubert E, Sander J, Ester M, Kriegel HP, Xu X. DBSCAN Revisited, Revisited: Why and How You Should (Still) Use DBSCAN. ACM Trans Database Syst [Internet]. 2017;42. Available from: https://doi.org/10.1145/3068335

[^2]: Zhang T, Ramakrishnan R, Livny M. BIRCH: A New Data Clustering Algorithm and Its Applications. Data Min Knowl Discov [Internet]. 1997;1:141–82. Available from: https://doi.org/10.1023/A:1009783824328

[^3]: Shang F, Jiao LC, Shi J, Wang F, Gong M. Fast affinity propagation clustering: A multilevel approach. Pattern Recognit [Internet]. 2012;45:474–86. Available from: https://www.sciencedirect.com/science/article/pii/S0031320311002007