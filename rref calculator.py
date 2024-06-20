# Sample Matrix
# Matrix=[[0,0,3,5,6,8,-9],[0,5,6,2,1,0,3],[1,8,-9,1,5,7,0],[0,8,-9,1,5,7,0],[5,8,-9,1,5,7,0]]

def interchange(l,x,y):                      # X and Y indices of l are to be interchanged
    l[x],l[y]=l[y],l[x]
    return l
def corresp_diff(l2,l1):
    return [l2[j]-l1[j] for j in range(len(l1))]
def reduce(l,i):                             #l is the list and i is the required index, whose value is to be divided
    if l[i]!=0:
        return [elt/l[i] for elt in l]
    else:
        return l
def scaling(M,x):
    return [x*elt for elt in M]
def count_zero_rows(M):
    count=0
    for row in M:
        if row==[0]*len(row):
            count+=1
    return count
def remove_zero_rows(l):
    for item in l:
        if item==[0 for elt in range(len(l[0]))]:
            l.remove(item)
    return l
def rref(M):
    if not M: return
    no_of_rows,no_of_columns=len(M),len(M[0])
    leading_entry_index = 0
    for r in range(no_of_rows):
        if leading_entry_index >= no_of_columns:
            return
        i = r
        while M[i][leading_entry_index]==0:
            i+=1
            if i==no_of_rows:
                i=r
                leading_entry_index+=1
                if no_of_columns==leading_entry_index:
                    return M
        M=interchange(M,i,r)
        index = M[r][leading_entry_index]
        M[r]=reduce(M[r],leading_entry_index)
        for i in range(no_of_rows):
            if i!=r:
                index = M[i][leading_entry_index]
                scaled=scaling(M[r],index)
                M[i]=corresp_diff(M[i],scaled)
        leading_entry_index += 1
    return M

m,n=list(map(int,input("No. of rows and columns in the matrix A from Ax=0 : ").split()))
matrix=[]
i=1
while i<=m:
    matrix.append(list(map(int,input("Row {}: ".format(i)).split())))
    i+=1

rref(matrix)
no_of_rows=len(matrix[0])
no_of_zero_rows=count_zero_rows(matrix)
print("\nThe Required RREF is :\n")
for row in matrix:
    print(" ".join(str(row)[1:-1].split(', ')))

pivots=[]
sol=[]
sol.append(str([0 for elt in range(len(matrix[0]))]))
i=0
columns=[]
free_var=[]
basic_var=[]
#matrix=remove_zero_rows(matrix)
for j in range(no_of_rows):                      
    col=[]
    for row in matrix:
        col.append(row[j])
    columns.append(col)
for item in columns:
    if item.count(1.0)==1 and item.count(0.0)==len(item)-1:
        pivots.append((item.index(1.0)+1,i+1))
        basic_var.append("x{}".format(i+1))
    else:
        free_var.append("x{}".format(i+1))
    i+=1
print("\nPIVOT POSITIONS : \n",pivots)
#print("Columns",columns)
#print("sol",sol)
print("\nFree Variables : ",free_var)

col_no=[int(i[1:]) for i in free_var]
not_col_no=[z for z in range(len(col_no)) if z not in col_no]
k=not_col_no[0]
k=0
if free_var!=[]:
    para_sol=[[0 for elt in range(no_of_rows)]]
    for i in range(len(free_var)):
        k=0
        sample=[0 for elt in range(no_of_rows)]
        n_col=int(free_var[i][1:])
        for j in range(len(columns)): 
            if n_col-1==j:            
                sample[j]=1.0                
            elif j+1 in col_no and n_col-1!=j:
                sample[j]=0.0                
            else:
                sample[j]=-(columns[n_col-1][k])      
                k+=1                    
        para_sol.append(sample)

print("\nSolution of the given matrix equation in parametric form is :\n\n",str(para_sol[0]),"+",end="")
for i in range(len(para_sol[1:])):
    for j in range(len(free_var)):
        if i==j and i!=len(free_var)-1:
            print(str(free_var[j])+"*"+str(para_sol[1:][j])+" + ",end="")
        elif i==j and i==len(free_var)-1:
            print(str(free_var[j])+"*"+str(para_sol[1:][j]),end="")
