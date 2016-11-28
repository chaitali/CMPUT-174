def movefirst(blist):
    clist=[]+blist
    x=clist.pop(0)
    clist.append(x)
    return clist

def main(): 
    alist=[2,4,6,8] 
    print(movefirst(alist)) 
    print(alist) 
main()