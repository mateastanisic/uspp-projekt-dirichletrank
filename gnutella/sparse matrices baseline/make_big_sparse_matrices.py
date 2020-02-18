import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse


def make_column_stohastic(A):
    n = A.shape[1]
    column_sum = A.sum(axis=0)
    row = []
    col = []
    data = []

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


A04 = scipy.sparse.load_npz('p2p-Gnutella04.npz')
A05 = scipy.sparse.load_npz('p2p-Gnutella05.npz')
A06 = scipy.sparse.load_npz('p2p-Gnutella06.npz')
A08 = scipy.sparse.load_npz('p2p-Gnutella08.npz')
A09 = scipy.sparse.load_npz('p2p-Gnutella09.npz')

n04 = A04.shape[0]
n05 = A05.shape[0]
n06 = A06.shape[0]
n08 = A08.shape[0]
n09 = A09.shape[0]

U04 = make_nxn_ones_over_n(n04)
U05 = make_nxn_ones_over_n(n05)
U06 = make_nxn_ones_over_n(n06)
U08 = make_nxn_ones_over_n(n08)
U09 = make_nxn_ones_over_n(n09)

M04 = make_column_stohastic(A04)
M05 = make_column_stohastic(A05)
M06 = make_column_stohastic(A06)
M08 = make_column_stohastic(A08)
M09 = make_column_stohastic(A09)


scipy.sparse.save_npz('p2p-Gnutella-U04.npz', U04)
scipy.sparse.save_npz('p2p-Gnutella-U05.npz', U05)
scipy.sparse.save_npz('p2p-Gnutella-U06.npz', U06)
scipy.sparse.save_npz('p2p-Gnutella-U08.npz', U08)
scipy.sparse.save_npz('p2p-Gnutella-U09.npz', U09)

scipy.sparse.save_npz('p2p-Gnutella-M04.npz', M04)
scipy.sparse.save_npz('p2p-Gnutella-M05.npz', M05)
scipy.sparse.save_npz('p2p-Gnutella-M06.npz', M06)
scipy.sparse.save_npz('p2p-Gnutella-M08.npz', M08)
scipy.sparse.save_npz('p2p-Gnutella-M09.npz', M09)

