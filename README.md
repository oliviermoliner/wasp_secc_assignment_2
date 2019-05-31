


# Results:

## SVD

4 nodes @ 1vcpu
- exdata_1.mtx (6001 x 6001, 1137751 nnz): 3m 21s


## QR
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