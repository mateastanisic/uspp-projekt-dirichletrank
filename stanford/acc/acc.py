import numpy as np
from array import *
from scipy.sparse import csr_matrix
import scipy.sparse
import matplotlib.pyplot as plt

def make_array_of_file(filename):
	ranks = array('i')
	for line in open(filename, 'r'):
		number = [int(s) for s in line.split() if s.isdigit()]
		if len(number) == 1 :
			ranks.append(number[0])

	return ranks

def make_array_of_file_float(filename):
	ranks = array('f')
	for line in open(filename, 'r'):
		ranks.append(float(line))

	return ranks

ranks_pr = make_array_of_file("stanford-pagerank-ranks.txt")
ranks_dr = make_array_of_file("stanford-dirichlet-ranks.txt")
values_pr = make_array_of_file_float("stanford-pagerank-values.txt")
values_dr = make_array_of_file_float("stanford-dirichlet-values.txt")

sum_r = 0
sum_v = 0
acc_r = 0
acc_v = 0
for i in range(len(ranks_pr)):
	acc_r += abs(ranks_pr[i] - ranks_dr[i])
	acc_v += abs(round(values_dr[i],6) - round(values_pr[i],6))
	sum_r += ranks_pr[i]
	sum_v += values_pr[i]

print( "ranks: ", acc_r/sum_r )
print("values: ", acc_v/sum_v) 
