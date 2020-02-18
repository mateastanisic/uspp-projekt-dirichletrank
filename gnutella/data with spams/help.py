import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse


A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=1.npz')
print(A04)
print(A04.shape[0])
A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=5.npz')
print(A04)
print(A04.shape[0])
A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=10.npz')
print(A04)
print(A04.shape[0])
A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=15.npz')
print(A04)
print(A04.shape[0])
A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=20.npz')
print(A04)
print(A04.shape[0])
A04 = scipy.sparse.load_npz('p2p-Gnutella04-k=30.npz')
print(A04)
print(A04.shape[0])