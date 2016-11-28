#Chaitali Patel
#Lecture B2

print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")

#lists used in program
vocab=['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon','donkey', 'fox', 'giraffe']
hangman=['------------','|         |',"|          O","|         / |","|          | ","|         / |\n|\n|"]

#Entering number to choose from vocab list and error handling one
while True:
    try:
        choose=input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
        if choose=="":
            print("Empty input!")
        else:
            choose=int(choose)
            word=vocab[choose]
        
    except ValueError:
        print("Input must be a integer")
            
    except IndexError:
        print("Index is out of range!")
           
    if choose in range(0,10):
        break
    
#display length of chosen word
print("The length of the word is:",len(word))
print("")


#initialize loop control variables
wrong=0
right=0

#showing how many letters are correct
unfinishedword=list(("_")*len(word))
word=list(word)

#main program loop
while((right!=len(word)) and (wrong!=6)):
    #Second Error Handling
    while True:
        letter=input("Please enter the letter you guess: ").lower()
        if(len(letter)==1) and (str.isalpha(letter)):
            break        
        else:
            print("You need to input a single alphabetic character!")
            print("")
    #checking if letter in word
    if (letter in word):
        while(letter in word):
            position=word.index(letter)
            unfinishedword[position]=letter
            word.remove(letter)
            word.insert(position," ")
            newstring="".join(unfinishedword)
            right=right+1
        #output if letter in word 
        print("The letter is in the word.")
        print("Letters matched so far:", newstring)
        #ending program when word is correct
        if right==len(word):
            print("You have found the mystery word. You win!")       
        else:
            print("")
        
    #if a correct letter is inputted again    
    elif letter in unfinishedword:
        print("The letter is in the word.")
        print("Letters matched so far:", newstring)
        print("")
        
    #incorrect letter inputted
    else:
        newstring="".join(unfinishedword)
        print("The letter is not in the word. ")
        print("Letters matched so far: ", newstring)
        hangman_art=("\n").join(hangman[:wrong+1])
        print(hangman_art)
        print("")
        wrong=wrong+1
        
    

    
#if the word is incorrectly guessed   
if(wrong==6):
    print("Too many incorrect guesses. You lost!")
    print("The word was: "+vocab[choose]+".")
    
#Goodbye! shown if word is wrong or right
print("Goodbye!") 

    