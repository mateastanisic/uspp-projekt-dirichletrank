import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse

def make_column_stohastic(A):
    row = []
    col = []
    data = []

    n = A.shape[1]
    column_sum = A.sum(axis=0)

    for j in range(n):
        csum = column_sum[0,j] 
        if csum > 0 :
            for i in range(n):
                if A[i,j] != 0 :
                    row.append(i)
                    col.append(j)
                    data.append(A[i,j]/csum)

    return csr_matrix((data, (row, col)), shape=(n, n))

def make_nxn_ones_over_n(n):
    row = []
    col = []
    data = []

    for i in range(n):
        for j in range(n):
            row.append(i)
            col.append(j)
            data.append(1/n)
                    
    return csr_matrix((data, (row, col)), shape=(n, n))



A = scipy.sparse.load_npz('sparse matrices after/stanford-spam-dr-A-k=30.npz')
n = A.shape[0]
print("k=30")
print(n)
print("before U")
U = make_nxn_ones_over_n(n)
print("done U")
M = make_column_stohastic(A)
scipy.sparse.save_npz('sparse matrices after/stanford-spam-dr-M-k=30.npz', M)
scipy.sparse.save_npz('sparse matrices after/stanford-spam-dr-U-k=30.npz', U)






