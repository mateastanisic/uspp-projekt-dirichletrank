import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse
    
def pagerank(M, U, error: float = 0.001, l: float = 0.85, num_iterations: int = 100):
    
    """
    Input: 
        M - neighbour matrix of "network", "stohastic"
        U - nxn uniform matrix with all values 1/n
        error - small treshold for detecting convergence 
        l - lambda value
        num_iterations - max number of iterations while searching for rank
        
    Output:
        Xk - vector that contains page ranks 
    """
    
    n = M.shape[1]
    X = np.ones(n)/n

    Mtilda = l * M + (1-l) * U

    for i in range(num_iterations):
        Xk = Mtilda * X
        done_i = np.zeros(n)

        for ii in range(n):
            if abs(Xk[ii] - X[ii]) > error : 
                done_i[ii] = False
            else :
                done_i[ii] = True


        done = True
        for ii in range(n):
            if done_i[ii]:
                continue
            else:
                done = False
                break
        X = Xk 

        if done: 
            break
        
    return X




