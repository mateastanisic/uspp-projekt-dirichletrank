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


A01 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=1.npz')
A05 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=5.npz')
A10 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=10.npz')
A15 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=15.npz')
A20 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=20.npz')
A30 = scipy.sparse.load_npz('p2p-Gnutella-A04-k=30.npz')

n01 = A01.shape[0]
n05 = A05.shape[0]
n10 = A10.shape[0]
n15 = A15.shape[0]
n20 = A20.shape[0]
n30 = A30.shape[0]

print("starting to make matrices:")
U01 = make_nxn_ones_over_n(n01)
M01 = make_column_stohastic(A01)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k1.npz', U01)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k1.npz', M01)
print("1")

U05 = make_nxn_ones_over_n(n05)
M05 = make_column_stohastic(A05)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k5.npz', U05)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k5.npz', M05)
print("5")

U10 = make_nxn_ones_over_n(n10)
M10 = make_column_stohastic(A10)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k10.npz', U10)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k10.npz', M10)
print("10")

U15 = make_nxn_ones_over_n(n15)
M15 = make_column_stohastic(A15)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k15.npz', U15)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k15.npz', M15)
print("15")

U20 = make_nxn_ones_over_n(n20)
M20 = make_column_stohastic(A20)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k20.npz', U20)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k20.npz', M20)
print("20")

U30 = make_nxn_ones_over_n(n30)
M30 = make_column_stohastic(A30)
scipy.sparse.save_npz('p2p-Gnutella-spam-U04-k30.npz', U30)
scipy.sparse.save_npz('p2p-Gnutella-spam-M04-k30.npz', M30)
print("30")




