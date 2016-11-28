#First we will open the file for reading and the file for
#writing
import os.path
endofprogram=False

try:
    filename1=input("Enter name of input file> ")
    infile=open(filename1,"r")
    filename2=input("Enter name of output file > ")
    #while(os.path.isfile(filename2)):
    #    filename2=input("File Exists!Enter name again>")
    outfile=open(filename2,"w")
except IOError:
    print("Error reading file. End of program")
    endofprogram=True
    
    
if endofprogram==False:
    countlines=0
    for line in infile:
        countlines=countlines+1
        outfile.write(line)
    print("number of lines",countlines)
    infile.close()
    outfile.close()
    
    #if no close, chosen file will not change