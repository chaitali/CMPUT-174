def printcolumn(alist,column):
    print('The column is : ')
    for i in range(0,len(alist)):
        print(alist[i][column])

def printlist(alist):
    for i in range(0,len(alist)):
        for j in range(0,len(alist[0])):
            print(alist[i][j],end=" ")
        print()


def main():
    alist=[[1,3,5],[2,4,6],[0,1,0]]
    printlist(alist)
    printcolumn(alist,0)
    #printrow(alist,1)
    
main()