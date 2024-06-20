RREF Calculator
This repository contains a Python script to compute the Reduced Row Echelon Form (RREF) of a given matrix. The script also identifies pivot positions, free variables, and provides the solution in parametric form for a system of linear equations 
Ax=0.

Features
Computes the RREF of a matrix
Identifies pivot positions
Identifies free variables
Provides the solution of the system in parametric form
Functions
interchange(l, x, y)
Interchanges the elements at indices x and y in list l.

corresp_diff(l2, l1)
Returns a list where each element is the difference between the corresponding elements of lists l2 and l1.

reduce(l, i)
Divides all elements of list l by l[i], if l[i] is not zero.

scaling(M, x)
Scales all elements of list M by x.

count_zero_rows(M)
Counts the number of zero rows in matrix M.

remove_zero_rows(l)
Removes all zero rows from list l.

rref(M)
Converts matrix M to its Reduced Row Echelon Form.
