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
A_baseline = scipy.sparse.load_npz("sparse matrices baseline/stanford-baseline-A.npz")
M_baseline = scipy.sparse.load_npz("sparse matrices baseline/stanford-b-M.npz")
U_baseline = scipy.sparse.load_npz("sparse matrices baseline/stanford-b-U.npz")

A_after = scipy.sparse.load_npz("sparse matrices after/pr/stanford-spam-pr-A-k=30.npz")
M_after = scipy.sparse.load_npz("sparse matrices after/pr/stanford-spam-pr-M-k=30.npz")
U_after = scipy.sparse.load_npz("sparse matrices after/pr/stanford-spam-pr-U-k=30.npz")


## PAGERANK -------------------------------------------------------------
pr_baseline = pr(M_baseline,U_baseline,"baseline pagerank/stanford-pagerank-ranks.txt", "baseline pagerank/stanford-pagerank-values.txt")
pr_after = pr(M_after,U_after,"pagerank after/stanford-pagerank-ranks-k=30.txt","pagerank after/stanford-pagerank-values-k=30.txt")



## DIRICHLETRANK ---------------------------------------------------------
#A_after = scipy.sparse.load_npz("sparse matrices after/dr/stanford-spam-dr-A-k=30.npz")
#M_after = scipy.sparse.load_npz("sparse matrices after/dr/stanford-spam-dr-M-k=30.npz")
#U_after = scipy.sparse.load_npz("sparse matrices after/dr/stanford-spam-dr-U-k=30.npz")

dr_baseline = dr(A_baseline, M_baseline, U_baseline, "baseline dirichlet/stanford-dirichlet-ranks.txt", "baseline dirichlet/stanford-dirichlet-values.txt")
dr_after = dr(A_after, M_after, U_after, "dirichlet after/stanford-dirichlet-ranks-k=30.txt", "dirichlet after/stanford-dirichlet-values-k=30.txt")


## number of bogus pages
k=30
#plt.figure()
## xaxis - orginal rank, yaxis - rank after spam --------------------------

#plt.plot(pr_baseline, dr_baseline, 'o', markersize=0.2)
#plt.plot(dr_baseline, dr_after[:-k], 'o', color='red', markersize=0.2)
#plt.xlabel('PageRank stranice')
#plt.ylabel('DirichletRank stranice')
#plt.savefig('images/stanford-sametp-pr-dr.png', dpi=300)
#plt.show()

plt.figure()
## xaxis - orginal rank, yaxis - rank after spam --------------------------
plt.plot(pr_baseline, pr_after[:-k], 'o', markersize=0.2, label="PageRank")
plt.plot(dr_baseline, dr_after[:-k], 'o', color='red', markersize=0.2, label="DirichletRank")
plt.xlabel('Rang stranice prije dodavanja spam stranica')
plt.ylabel('Rang stranice nakon dodavanja spam stranica')
plt.savefig('images/stanford-spam-sametp-k=30.png', dpi=300)
plt.show()
