import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse
import networkx as nx

gc.collect()
#U = scipy.sparse.load_npz('sparse matrices baseline/stanford-baseline-U.npz')
#print(U)
M = scipy.sparse.load_npz('sparse matrices after/stanford-spam-pr-M-k=5.npz')
print(M)


# def make_row_stohastic(A):
#     n = A.shape[1]
#     M = np.zeros((n, n))

#     for i in range(n):
#         row_sum = np.sum(A[i, :])
#         if row_sum > 0:
#             for j in range(n):
#                 M[i, j] = A[i, j] / row_sum

#     return M


# def make_column_stohastic(A):
#     n = A.shape[1]
#     M = np.zeros((n, n))
#     for i in range(n):
#         column_sum = np.sum(A[:, i])
#         if column_sum > 0:
#             for j in range(n):
#                 M[j, i] = float(A[j, i] / column_sum)
#     return M


# G = np.array([[0, 0, 0, 0, 1],
#               [1, 0, 0, 0, 0],
#               [1, 0, 0, 0, 0],
#               [0, 1, 1, 0, 0],
#               [0, 0, 1, 1, 0]])

# Gr = make_row_stohastic(G)
# Gc = make_column_stohastic(G.T)
# print(Gr)
# print(Gc)