#Chaitali Patel

import random
number=random.randint(1,100)

guess=int(input("Enter a number between 1-100: "))
guesses=0

while(guess!=number):       
    if(guess<number):
        print("Guess is too low")
    elif(guess>number):
        print("Guess is too high")
    guess=int(input("Enter a number: "))
    guesses=guesses+1
    
print("Well done! You guessed", number,"in" ,guesses,"guesses")
    