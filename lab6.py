# program for removing duplicates 

def eliminateDuplicates(lst):
    newlist=[]
    for item in lst:
        if item not in newlist:
            newlist.append(item)    
       
    return newlist
    
def main():
    alist=[]
    integers=[]
    number=input("Enter numbers: ")
    a=number.split()
    for item in a:
        item=int(item)
        integers.append(item)
    print(integers)
    newlist=eliminateDuplicates(integers)
    print("The distinct numbers are:",newlist)
    

main()  
    
