i=1 #initialize loop control variable
while(i<=4):
    j=1 #initialize loop control variable
    print('i = ',i)
    while(j<=len('word')):
        print(i*j)
        j=j+1 #update loop control variable
    i=i+1 #update loop control variable
    
#continue

i=0
total=0
while(i<5):
    number=int(input("Enter a number: "))
    if(number<0):
        continue
    i=i+1
    total=total+number
print(total)

#try-except

try:
    a=1/0
except ZeroDivisionError:
    print("error")
   