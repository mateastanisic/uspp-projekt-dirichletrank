import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse

def parse_input(name):

    nodes = []
    rangs  = []
    i = 0

    for line in open(name, 'r'):
        i += 1
        v = int(line)
        if v<=100:
            nodes.append(i)
            rangs.append(v)
    
    ##print(nodes)
    print(rangs)
    # print("from: ", sum_from, "\n to: ", sum_to )
    # print("sum<=2000: ", sum_to+sum_from )
    # print("summ: ", svih)
    # print("precent: ", float( (sum_to+sum_from)/svih ) )


parse_input("p2p-Gnutella04-pagerank-ranks.txt")




#sparse_matrix = scipy.sparse.load_npz('test.npz')
#print(sparse_matrix)
