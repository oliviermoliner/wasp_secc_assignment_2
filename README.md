## Configuratio

**Getting Spark to use all cores**

Set:

- `spark.executor.instances` to the number of yarn cores
- `spark.executor.cores` to 1
- `spark.dynamicAllocation.enabled` set to `false` to control work allocation
- Repartition the data into 2xN partitions where N is the number of cores.


## Results:

https://sparse.tamu.edu/GHS_psdef/ldoor

### SVD

larger: https://sparse.tamu.edu/GHS_psdef/ldoor

*Compute the top 5 singular values and corresponding singular vectors.*

**Data:**
- [DNV-Ex 6 : Ship section/detail from production run-1999-01-17](https://sparse.tamu.edu/DNVS/shipsec8)
  - 114,919 rows x 114,919 cols
  - 3,303,553 non-zero elements
  - Partitioned into 20 cached partitions

**Cluster:**
- Master: 4 vcpu, 15 GB ram, 500 GB disk
- Worker: 4 vcpu, 15 GB ram, 500 GB disk, 1 yarn core per vcpu

| # workers | # cores 	| SVD time (s)	| Data loading time (s) |
|--- |---	|---	| ----    |
| 5   |  10 | 609 | 111 |
| 5   |  14 | 524 | 153 |






### QR
4 nodes @ 1vcpu
- impcol_d.mtx (425 x 425, 1339 nnz): 1m 0s
- ch7-6-b2.mtx (4200 x 630, 12600 nnz): 0m 46s
- abtaha2.mtx (37932 x 331, 137228 nnz): 0m 53s
- relat7b.mtx (21924 x 1045, 81355 nnz): 0m 59s
- landmark.mtx (71952 x 2704, 1151232 nnz): 2m 55s, 2m 59s, 2m 55s

3 nodes @ 1vcpu
- landmark.mtx (71952 x 2704, 1151232 nnz): 2m 59s, 2m 51s, 2m 48s

2 nodes @ 1vcpu
- landmark.mtx (71952 x 2704, 1151232 nnz): 4m 23s, 4m 20s, 4m 8s

# MATLAB
tic; qr(Problem.A); toc
Elapsed time is 0.315548 seconds.
