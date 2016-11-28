#Chaitali Patel
#Lecture B2
#Lab H05

import random
number=random.randint(1,99)

#preliminaries
print("The purpose of this exercise is to enter a number of coin values that add up to a displayed target value.")
print("")
print("Enter coins values as 1-penny, 5-nickel, 10-dime,and 25-quarter.")
print("Hit return after the last entered coin value.")
print("")


#loop control variable
answer="y" 

while((answer=="Y")or(answer=="y")):
    import random
    number=random.randint(1,99)    
    
    print("Enter coins that add up to", number, "cents, one per line.")
    print("")
    #input
    coin=str(input("Enter first coin: "))
    total=0 #loop control variable
    
    
    if((coin=="25")or(coin=="10")or(coin=="5")or(coin=="1")):
        coin=int(coin)
        total=total+coin
    elif(coin==""):
        coin=0
    else:
        print("Invalid Entry")
    
        
    while((number>total)and(coin!=0)):
            coin=str(input("Enter next coin: "))
            if(coin==""):
                break
            coin=int(coin)
            total=total+coin
            
    
    if(total<number):
        print("Sorry- you only entered", total, "cents.")
    elif(total>number):
        print("Sorry- total amount exceeds", number, "cents.")
    elif(total==number):
        print("Correct!")
    print("")
    answer=str(input("Try again (y/n)?: "))
    if((answer=="n")or(answer=="N")):
        print("Thanks for playing...goodbye")

    
    
