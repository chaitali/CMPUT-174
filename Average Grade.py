grades=int(input("Enter first grade: "))
answer=input("Do you want to more (y/n): ")
glist=[grades]

while(answer=='y'):
    grades=int(input("Enter next grade: "))
    answer=input("Do you want more? ")
    glist.append(grades)
    
avg=sum(glist)/len(glist)
print(avg)
for item in glist:
    if(item<avg):
        print(item)
        
    