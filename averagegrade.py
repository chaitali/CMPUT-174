# print the average grade 

grades=int(input("Enter first grade: "))
answer=input("Do you want to input more (y/n): ")
glist=[grades]

while(answer=='y'):
    grades=int(input("Enter next grade: "))
    answer=input("Do you want to input more? ")
    glist.append(grades)
    
avg=sum(glist)/len(glist)
print(avg)

#list all the grades lower than the average 
for item in glist:
    if(item<avg):
        print(item)
        
    