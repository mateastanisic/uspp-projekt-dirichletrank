from sparse_dirichletrank import dirichletrank
from sparse_pagerank import pagerank
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse
import matplotlib.pyplot as plt

def pr(M,U,filename_r, filename_v):
    pr = pagerank(M, U)
    n = len(pr)
    order = (-pr).argsort()[:n]
    ranks = order.argsort()

    ## save results (array where array[i] is rank of page with index i) to a file
    with open(filename_v, "wb") as f:
        np.savetxt(f, pr, fmt='%f')
    with open(filename_r, "wb") as f:
        np.savetxt(f, ranks, fmt='%i')

    return ranks

def dr(A,M,U,filename_r, filename_v):
    dr = dirichletrank(A, M, U)
    n = len(dr)
    order = (-dr).argsort()[:n]
    ranks = order.argsort()

    ## save results (array where array[i] is rank of page with index i) to a file
    with open(filename_v, "wb") as f:
        np.savetxt(f, dr, fmt='%f')
    with open(filename_r, "wb") as f:
        np.savetxt(f, ranks, fmt='%i')

    return ranks

## saved sparse matrices
A_baseline = scipy.sparse.load_npz("sparse matrices baseline/p2p-Gnutella-A04.npz")
M_baseline = scipy.sparse.load_npz("sparse matrices baseline/p2p-Gnutella-M04.npz")
U_baseline = scipy.sparse.load_npz("sparse matrices baseline/p2p-Gnutella-U04.npz")

A_after = scipy.sparse.load_npz("sparse matrices with spam/p2p-Gnutella-A04-k=30.npz")
M_after = scipy.sparse.load_npz("sparse matrices with spam/p2p-Gnutella-spam-M04-k30.npz")
U_after = scipy.sparse.load_npz("sparse matrices with spam/p2p-Gnutella-spam-U04-k30.npz")



## PAGERANK -------------------------------------------------------------
pr_baseline = pr(M_baseline,U_baseline,"baseline pagerank/p2p-Gnutella04-pagerank-ranks.txt", "baseline pagerank/p2p-Gnutella04-pagerank-values.txt")
pr_after = pr(M_after,U_after,"after pagerank/p2p-Gnutella04-after-pagerank-ranks-k=30.txt","after pagerank/p2p-Gnutella04-after-pagerank-values-k=30.txt")

## DIRICHLETRANK ---------------------------------------------------------
dr_baseline = dr(A_baseline, M_baseline, U_baseline, "baseline dirichlet/p2p-Gnutella04-dirichlet-ranks.txt", "baseline dirichlet/p2p-Gnutella04-dirichlet-values.txt")
dr_after = dr(A_after, M_after, U_after, "after dirichlet/p2p-Gnutella04-after-dirichlet-ranks-k=30.txt","after dirichlet/p2p-Gnutella04-after-dirichlet-values-k=30.txt")

## number of bogus pages
k=30

plt.figure()
## xaxis - orginal rank, yaxis - rank after spam --------------------------
plt.plot(pr_baseline, dr_baseline, 'o', markersize=0.2)
#plt.plot(dr_baseline, dr_after[:-k], 'o', color='red', markersize=0.2)
plt.xlabel('PageRank stranice')
plt.ylabel('DirichletRank stranice')
plt.savefig('images/p2p-Gnutella04-pr-dr.png', dpi=300)
plt.show()

plt.figure()
## xaxis - orginal rank, yaxis - rank after spam --------------------------
plt.plot(pr_baseline, pr_after[:-k], 'o', markersize=0.2, label="PageRank")
plt.plot(dr_baseline, dr_after[:-k], 'o', color='red', markersize=0.2, label="DirichletRank")
plt.xlabel('Rang stranice prije dodavanja spam stranica')
plt.ylabel('Rang stranice nakon dodavanja spam stranica')
plt.savefig('images/p2p-Gnutella04-spam-k=30.png', dpi=300)
plt.show()

