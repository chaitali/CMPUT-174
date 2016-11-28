#converts string(input) to list
#prints sentence as list of string objects
#loop to remove punctuation
#list to string
#prints sentence w/out punctuation

punctuation=['(', ')','?',':',';',',','.','!','/','"',"'"]

sentence=input("Type in a single line of text: ")
char=list(sentence)
print(char)

for item in punctuation:
    while(item in char):
            char.remove(item)

#fg.,k
newchar="".join(char)
print(newchar)
