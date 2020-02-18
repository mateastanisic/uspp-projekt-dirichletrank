import gc
import numpy as np
from scipy.sparse import csr_matrix
import scipy.sparse

row = []
col = []
data = []

done = False
last_done = 0

def parse_input(name):

    global done
    global last_done
    global row
    global col
    global data

    for line in open(name, 'r'):
        if "Nodes" in line:
            integers = [int(s) for s in line.split() if s.isdigit()]
            n = integers[0]
            break

    if done :
        i = 0
        for line in open(name, 'r'):
            i += 1
            # pročitaj komentare
            if i<=last_done:
                continue    
            else: 
                # pretpostavka da smo učitali n
                nodes = [int(s) for s in line.split() if s.isdigit()]
                if( len(nodes) == 2 ):
                    row.append(nodes[1])
                    col.append(nodes[0])
                    data.append(1)
                gc.collect()
                
        last_done = i
    else :
        for line in open(name, 'r'):
            last_done += 1
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
        done = True
    return csr_matrix((data, (row, col)), shape=(n, n))



A = parse_input("p2p-Gnutella04-k=1.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=1.npz', A)
print("1")
A = parse_input("p2p-Gnutella04-k=5.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=5.npz', A)
print("5")
A = parse_input("p2p-Gnutella04-k=10.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=10.npz', A)
print("10")
A = parse_input("p2p-Gnutella04-k=15.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=15.npz', A)
print("15")
A = parse_input("p2p-Gnutella04-k=20.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=20.npz', A)
print("20")
A = parse_input("p2p-Gnutella04-k=30.txt")
scipy.sparse.save_npz('p2p-Gnutella04-k=30.npz', A)
print("30")


#sparse_matrix = scipy.sparse.load_npz('test.npz')
#print(sparse_matrix)
