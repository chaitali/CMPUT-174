def putTogether(alist,blist):
 clist=alist+blist
 return clist

def mergealternate(alist,blist):
 z=[]
 for i in range(len(alist)):
  row=[]
  row.append(alist[i])
  row.append(blist[i])
  z.append(row)
 return z


def main(): 
 alist=[2,4,6,8] 
 blist=[1,3,5,7] 
 print(putTogether(alist,blist)) 
 print(mergealternate(alist,blist)) 
main() 
