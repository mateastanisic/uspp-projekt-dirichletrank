import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse
from array import * 


def make_omegas(A, mi: int = 20):
    #about 8sec for n=10 000
    n = A.shape[1]

    rowcol = array('i')
    data1 = array('f')
    data2 = array('f')
    li = A.sum(axis=0)

    for i in range(n):
        ## |Lv| equals to sum of the elements of the row corresponding to page v in A
        rowcol.append(i) 
        lii = li[0,i] 
        data1.append( float(1 - ( mi / (lii + mi) )) )
        data2.append( float( mi / (lii + mi) ) )

    Omega_1 = csr_matrix((data1, (rowcol, rowcol)), shape=(n, n))
    Omega_2 = csr_matrix((data2, (rowcol, rowcol)), shape=(n, n))

    return [Omega_1, Omega_2]



def dirichletrank( A, M, U, error: float = 0.001, mi: int = 20, num_iterations: int = 100):
    """
    Input:
        A - neighbour matrix of "network" - for calculating Omega_1 and Omega_2
        M - neighbour matrix of "network", "stohastic"
        U - nxn uniform matrix with all values 1/n
        error - small treshold for detecting convergence 
        mi - mi value
        num_iterations - max number of iterations while searching for rank
        
    Output:
        Xk - vector that contains page ranks 
    """
    
    n = M.shape[1]
    X = np.ones(n)/n

    [Omega_1, Omega_2] = make_omegas(A, mi)

    Mtilda = Omega_2 * M + Omega_1 * U

    for i in range(num_iterations):
        Xi = Mtilda * X
        done_i = np.zeros(n)

        for ii in range(n):
            if abs(Xi[ii] - X[ii]) > error : 
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
        X = Xi 

        if done: 
            break
        
    return X

