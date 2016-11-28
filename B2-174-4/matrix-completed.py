#Chaitali Patel
#Lecture B2
                                                                     
                                                                     
                                             
def prettyPrint(A):
    for i in range(len(A)):
        line = "\t|"+str(A[i][0])
        for j in range(1, len(A[i])):
            line = line + "\t" + str(A[i][j])
        line = line + "|"
        print(line)
    return

def matrixADD(A,B):
    Z = []
    for i in range(len(A)): #first matrix item
        row = []
        for j in range(len(A[0])): #for j within the length of the first matrix
            row.append(A[i][j]+B[i][j]) #add
        Z.append(row)
    return Z

def matrixSUB(A,B):
    Z = []
    for i in range(len(A)): #first matrix item
        row = []
        for j in range(len(A[0])): #for j within length of first matrix
            row.append(A[i][j]-B[i][j]) #subtract
        Z.append(row)
    return Z

def row(A,i):
    Z = []
    for a in range(0,len(A[i])): 
        Z.append(A[i][a]) #append the A[i] matrix and all items within it
    
    return Z

def col(B,j):
    Z = []
    for a in range(0,len(B)):
        Z.append(B[a][j])
    return Z

def dotProduct(x,y):
    multiply=0 #multiply numbers in matrix
    prod=0 #add all products together
    n=0 #number of items in matrix
    for i in x:
        multiply=i*y[0+n]
        prod=multiply+prod
        n=n+1
        
    return prod
       

def matrixMUL(A,B):
    Z=[]
    
    for item in range(len(A)): #fill Z with 0 for length of matrix A
        Z.append([0])
        
        for new in range(len(B[0])-1): #fill Z with 0 for length of B
            Z[item].append(0)  #append 0 in each list
            
    for i in range(len(A)): 
        for j in range(len(B[0])): #length of first B matrix
            for k in range(len(B)):
                Z[i][j]=A[i][k]*B[k][j]+Z[i][j] #append in each list A*B plus add previous Z[i][j]
                
    return Z
    
  
    

def main():
    #Test matrices
    A = [[2,4], [7,0], [6,3]]
    B = [[3,1], [-1,8], [-3, 3]]
    C = [[4,1,9], [6,2,8], [7,3,5]]
    D = [[2,9], [5,2], [1,0]]
    E = [[-3,4,5,-4], [-1,-2,0,2], [1,3,6,7]]
    F = [[-3,4,5,8], [-1,-4,9,-2], [10,11,1,2], [3,6,0,7]]
    G = [[2,3,4], [0,1,0], [-2,3,7]]
    H = [[1,2], [2, 1]]
    I = [[1,0,0], [0,1,0], [0,0,1]]
    
    # HINT: in Python, you can have multi-line comments, delimited by '''
    
    
    print("A + B:")
    prettyPrint(matrixADD(A,B))
    print("\nA - B:")
    prettyPrint(matrixSUB(A,B))
    print("\nrow(C,0):")
    print(row(C,0))
    print("\ncol(D,0):")
    print(col(D,0))
    print("\ndotProduct(row(C,0), col(D,0)):")
    print(dotProduct(row(C,0), col(D,0)))
    print("\nC * D:")
    prettyPrint(matrixMUL(C,D))
    print("\nG * C:")
    prettyPrint(matrixMUL(G,C))
    print("\nA + D:")
    prettyPrint(matrixADD(A,D))
    print("\nE * F:")
    prettyPrint(matrixMUL(E,F))
    print("\nG + C:")
    prettyPrint(matrixADD(G,C))
    print("\nH * H:")
    prettyPrint(matrixMUL(H,H))
    print("\nC * I:")
    prettyPrint(matrixMUL(C,I))
    
#run main function    
main()