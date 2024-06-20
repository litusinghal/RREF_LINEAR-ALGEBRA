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


Example
For a matrix 
A:
No. of rows and columns in the matrix A from Ax=0: 5 7
Row 1: 0 0 3 5 6 8 -9
Row 2: 0 5 6 2 1 0 3
Row 3: 1 8 -9 1 5 7 0
Row 4: 0 8 -9 1 5 7 0
Row 5: 5 8 -9 1 5 7 0
The script will output the RREF of the matrix, the pivot positions, the free variables, and the solution in parametric form.

Output
The Required RREF is:
0.0  1.0  0.0  0.0  0.0  -1.0357142857142858  0.21428571428571427
1.0  0.0  0.0  0.0  0.0  0.35714285714285715  0.42857142857142855
0.0  0.0  1.0  0.0  0.0  1.25  0.07142857142857142
0.0  0.0  0.0  1.0  0.0  0.5  -0.14285714285714285
0.0  0.0  0.0  0.0  1.0  -0.35714285714285715  -0.2857142857142857

PIVOT POSITIONS:
[(1, 2), (2, 1), (3, 3), (4, 4), (5, 5)]

Free Variables:
['x6', 'x7']

Solution of the given matrix equation in parametric form is:
[0, 0, 0, 0, 0, 0, 0] + x6*[1.0357142857142858, -0.35714285714285715, -1.25, -0.5, 0.35714285714285715, 1.0, 0.0] + x7*[-0.21428571428571427, -0.42857142857142855, -0.07142857142857142, 0.14285714285714285, 0.2857142857142857, 0.0, 1.0]
