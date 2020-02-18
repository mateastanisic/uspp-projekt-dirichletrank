import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse

def parse_input(name):

    for line in open(name, 'r'):
        if "Nodes" in line:
            integers = [int(s) for s in line.split() if s.isdigit()]
            n = integers[0]
        elif line[0] != '#':
            nodes = [int(s) for s in line.split() if s.isdigit()]
            if( len(nodes) == 2 ):
                if( nodes[0] >= n ):
                    n = nodes[0] + 1
                if( nodes[1] >= n ):
                    n = nodes[1] + 1

    row = []
    col = []
    data = []

    for line in open(name, 'r'):
        # pročitaj komentare
        if line[0] == '#':
            continue    
        else: 
            # pretpostavka da smo učitali n
            nodes = [int(s) for s in line.split() if s.isdigit()]
            if( len(nodes) == 2 ):
                row.append(nodes[1])
                col.append(nodes[0])
                data.append(1)
            gc.collect()
    return csr_matrix((data, (row, col)), shape=(n, n))


A = parse_input("stanford-spam-dr-k=1.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=1.npz', A)
A = parse_input("stanford-spam-dr-k=5.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=5.npz', A)
A = parse_input("stanford-spam-dr-k=10.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=10.npz', A)
A = parse_input("stanford-spam-dr-k=15.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=15.npz', A)
A = parse_input("stanford-spam-dr-k=20.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=20.npz', A)
A = parse_input("stanford-spam-dr-k=30.txt")
scipy.sparse.save_npz('stanford-spam-dr-A-k=30.npz', A)



#sparse_matrix = scipy.sparse.load_npz('test.npz')
#print(sparse_matrix)
