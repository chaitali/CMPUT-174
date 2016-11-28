i=0
alist=[]
while(i<=4):
    info=input('Enter name of student followed by grade >')
    name,grade=info.split()
    record=(name,float(grade))
    alist.append(record)
i=i+1
print(alist)