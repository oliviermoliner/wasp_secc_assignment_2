## Configuration

**Getting Spark to use all cores**

Set:

- `spark.executor.instances` to the number of yarn cores
- `spark.executor.cores` to 1
- `spark.dynamicAllocation.enabled` set to `false` to control work allocation
- Repartition the data into 2xN partitions where N is the number of cores.


## Results:

### SVD
*Compute the top 5 singular values and corresponding singular vectors.*

**Data:**
- [INDEED Test Matrix](https://sparse.tamu.edu/GHS_psdef/ldoor)
  - 952,203 rows x 952,203 cols
  - 42,493,817 non-zero elements
  - Partitioned into 20 cached partitions

**Cluster:**
- Master: 4 vcpu, 15 GB ram, 500 GB disk
- Worker: 4 vcpu, 15 GB ram, 500 GB disk, 1 yarn core per vcpu

| # workers | # cores 	| SVD time (s)	| Data loading time (s) |
|--- |---	|---	| ----    |
| 5   |  2  | 2394 | 275 |
| 5   |  5  | 1100 | 111 |
| 5   |  10 | 609 | 111 |
| 5   |  14 | 524 | 153 |

### QR
**Data:**
- [landmark Test Matrix](https://sparse.tamu.edu/Pereyra/landmark)
  - 71,952 rows x 2,704 cols
  - 1,151,232 non-zero elements
  - Partitioned into 20 cached partitions

**Cluster:**
- Master: 4 vcpu, 15 GB ram, 500 GB disk
- Worker: 4 vcpu, 15 GB ram, 500 GB disk, 1 yarn core per vcpu

| # workers | # cores | QR time (s) | Data loading time (s) |
| --- | --- | --- | --- |
|  5  |   2 | 136 |  20 |
|  5  |   4 |  95 |  26 |
|  5  |   6 |  97 |  22 |
|  5  |   8 |  88 |  27 |
|  5  |  12 |  87 |  24 |
|  5  |  16 |  83 |  26 |
|  5  |  20 |  82 |  25 |

