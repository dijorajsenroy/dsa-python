"""
1. Matrix Operations:

(i) Addition - O(m*n)

res(i,j) = a(i,j) + b(i,j)

(ii) Subtraction - O(m*n)

res(i,j) = a(i,j) - b(i,j)

(iii) Multiplication - O(m*n*p)

m x n * n * p = m * p
res(0,0) = a(0,0) * b(0,0) + a(0,1) * b(1,0) + a(0,2) * b(2,0) 
res(0,1) = a(0,0) * b(0,1) + a(0,1) * b(1,1) + a(0,2) * b(2,1) 
res(i,j) = a(i,k=0) * b(k=0,j) + a(i,k=1) * b(k=1,j) + a(i,k=2) * b(k=2,j)

Therefore, res(i,j) = Summation(0<=k<p) { a(i,k) * b(k,j) }

"""
def add(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2)):
            row[j] = mat1[i][j] + mat2[i][j]
        res.append(row)
    return res

def sub(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2)):
            row[j] = mat1[i][j] - mat2[i][j]
        res.append(row)
    return res

def mul(mat1, mat2):
    m = len(mat1); n=len(mat1[0]); p = len(mat2[0])
    res = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(n):
        for j in range(n):
            for k in range(p):
                res[i][j] += mat1[i][k]* mat2[k][j]
    return res

"""
2. Determinant of a Matrix:

The determinant of a matrix is calculated by computing the cofactor of all elements and adding/subtracting them
alternatively. To compute the co factor of an we take the smaller matrix not having the row or column of the element.
Thus it is recursive in nature, and the base case can be for n == 1 where we return one element. 
"""
def getCofactor(mat, cf, p, q, n):
    i = 0; j = 0
    for row in range(n):
        for col in range(n):
            # p and q are blacklisted row and column
            if row != p and col != q:
                cf[i][j] = mat[row][col]
                j += 1
            # reset col index
            if j == n - 1:
                j = 0
                i += 1
    return cf

def determinant(mat, n):
    d = 0
    # base case for one element
    if n == 1:
        return mat[0][0]
    # matrix to store cofactors
    cf = [[0 for _ in range(n)] for _ in range(n)]
    # for each element of first row
    for i in range(n):
        # get cofactor of mat[0][i]
        cf = getCofactor(mat, cf, 0, i, n)
        # compute determinant recursively
        d += ((-1)**i) * mat[0][i] * determinant(cf, n - 1)
    return d

"""
2. Print Snake Pattern:

The task is to print an MxN matrix storing natural numbers in Snake pattern. 
rows = 3, columns = 5
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
will be prited as: 00 01 02 03 04, 14 13 12 11 10, 20 21 22 23 24, and so forth
The simple pattern here is when i is odd the correct order is printed, and when
it is even the reverse order is printed. 

"""
def printSnake(mat):
    rows = len(mat); cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if i % 2 == 0:
                print(mat[i][j], end = " ")
            else:
                print(mat[i][j - cols], end = " ")
        print("\n")

"""
3. Matrix Boundary Traversal Problem:

For a given matrix print the boundary elements. For example, 
rows = 3, columns = 5
[[00, 01, 02, 03, 04],
[10, 11, 12, 13, 14],
[20 ,21 ,22 ,23 ,24]]
The elements printed: 00, 01, 02, 04, 14, 24, 23, 22, 21, 20, 10
4 loops for 4 boundaries, as the number of boundaries is always fixed.
"""

def printBoundary(mat):
    rows = len(mat); cols = len(mat[0])

    for i in mat[0]:
        print(i, end =" ")

    for i in range(rows):
        print(mat[i][cols-1], end=" ")

    for i in mat[-1][::-1]:
        print(i, end=" ")

    for i in reversed(range(1,rows)):
        print(mat[i][0], end=" ")

"""
4. Transpose of a Matrix:

The transpose of an NxN Matrix can easily be achieved by swapping the a(i,j) and a(j,i) elements.
"""
def transpose(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = (mat[j][i], mat[i][j])
    return mat

"""
5. Matrix Rotation Problem:

(i) 90 deg anti clockwise
Reverse of row order of transpose
(ii) 90 deg clockwise
Reverse the order of elements in a row of transpose
"""

# reversing the 2D array - reverses order of rows
anticlockwise90 = lambda mat: transpose(mat)[::-1]
# reverse each row in 2D array - reverse order of elements in a row
clockwise90 = lambda mat: [row[::-1] for row in transpose(mat)]

"""
6. Searching in Row and Column wise sorted Matrix:

The Naive solution is to search all elements in O(n*n) time. However the solution can be optimised in linear time complexity.
The steps involved in this algorithm, for an search element x, is explained as follows:

(i) We start from the top-right corner and check is the element is smaller then x then we check the array, or else we traverse
To the next array (as we know the row doesnt contain x) We save the row index, and if the element is found as a corner element,
we save the column index as well. 
(ii) If the row element isnt found, x doesnt exist, but if the column element isnt found we can look for it in the row index.
Ultimately if column index value remains unchanged as well we return false, or else we return the value found.

The time complexity of this code is O(rows+cols)
"""
def search(mat, x):
    rows = len(mat); cols = len(mat[0])
    r_idx = -1; c_idx = -1

    # obtaining value of r_idx
    for i in range(rows):
        if x < mat[i][-1]:
            r_idx = i
            break
        elif x == mat[i][-1]:
            r_idx = i
            c_idx = cols - 1
            break
        else:
            pass
    # x not found if r_idx is unchanged
    if r_idx == -1:
        return -1
    else:
        # computing c_idx if not found 
        if c_idx == -1:
            for i in range(cols):
                if mat[r_idx][i] == x:
                    c_idx = i

    # if c_idx and r_idx are found                
    if r_idx != -1 and c_idx != -1:
        return (r_idx, c_idx)
    else:
        return -1


"""
7. Median of Row-wise sorted Matrix:

The assumptions are the elements are all distinct and the matrix size is of odd size. Median in that case
is the middle element of all the values. It is denoted by the rows*cols/2 th element in the sorted array.
Sorting takes O(nlogn) and creating the array takes O(n*n). Thus complexity is O(n*n)
"""
def median(mat):
    rows = len(mat); cols = len(mat[0])
    flat = []
    for i in range(rows):
        for j in range(cols):
            flat.append(mat[i][j])
    flat = sorted(flat)
    return flat[rows*cols//2]
