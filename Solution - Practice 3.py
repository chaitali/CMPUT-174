# This program implements the code breaker game.
#Assign a code to a variable
code="ABFB"
#Create a list called validLetters (A,B,C,D,E,F)
validLetters=['A','B','C','D','E','F']
#Ask the user to enter guess and then change it to upper
guess=input("Enter a guess")
guess=guess.upper()
# Check for validity of guess
#A guess is valid if its length is = 4 
# A guess is valid if it contains letters that are found in validLetters
#if any of the above is not true then set invalid to True
notValid=False
if(len(guess)!=4):
    notValid=True

for letter in guess:
    if letter not in validLetters:
        notValid=True



# Start a while loop which should execute only if
# guess is not equal to code and the guess is not invalid
while((guess !=code) and (notValid != True)):
    
#Convert the code string into list
#Convert the guess string into list 
    codelst=list(code)
    guesslst=list(guess)
    position=0
    match=0
#Declare any variable that you would need    



#GIVE FEEDBACK
#FEEDBACK#1 HOW MANY CHARACTERS IN PLACE
#Now implement a while loop that compares the character in codeLst
#and guessLst
#The matched ones should be marked by changing the letter to #
#report how many are in place
    while(position<4):
        if(guesslst[position]==codelst[position]):
            match=match+1
            guesslst[position]="#"
            codelst[position]='#'
        position=position+1
        
        
        
        
    print(match," letters match the code ")  
    
#FEEDBACK#2 HOW MANY CHARACTERS OUT OF PLACE
#Consider EACH letter in guessLst. If it is not "#", compare it to 
#EVERY letter in codeLst. 
#If there is a match then:
#1. ofp should be incremented
#2 The letter in codeLst should be set to "#"  
#3 Stop comparing the guessLst letter, when the match is found 
    ofp=0
                    
    for letter in guesslst:
        if(letter!='#'):
            if letter in codelst:
                ofp=ofp+1
                position=codelst.index(letter)
                codelst[position]='#'
                    
                    
                        
    print(ofp, "letters are out of place ")    
    
    #Get the input and check whether the guess is valid or not
    
    guess=input("Enter a guess")
    guess=guess.upper()
    invalid=False
    if(len(guess)!=4):
        invalid=True
    
    for letter in guess:
        if letter not in validLetters:
            notValid=True
    
 
    
    
   
    
     
     
# When you quit the while loop
# You have to check because guess could be invalid
if(guess == code):
    print("Congratulations!")
else:
    print("Invalid guess")
    print("The code was :",code)