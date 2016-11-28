'''
try:
    inFile=open("example.txt",'r') #opening file- file name in example.txt
    numLines=0
    MyGrades=[]
    for line in inFile:
        if line[0]!="/n": #if line is not blank
            line=line.strip() #strip line
            name,grade=line.split() #split name and grade
            MyGrades.append((name,float(grade))
            numLines=numLines+1
        print(line)
    inFile.close #closing file
    print(numLines)
except:
    print("Error opening file")
    
    
    
#read entire file

myVar=inFile.read()
print(myVar)
#read one line
myVar=inFile.readline()
print(myVar)


#can not split empty line
'''

#import.ospath to check if file exists
#numbers must be converted into string before putting in file
