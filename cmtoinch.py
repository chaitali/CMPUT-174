#Chaitali Patel
#Lecture B2
#Lab H05

#input
cm=float(input("Enter the length in centimetres: "))

#processing
inches=cm/(2.54)
yards=inches/36
feet=((yards-(inches//36))*3)
inch=(feet-int(feet))*12

#output
print("The length is" ,int(yards) ,"yard," ,int(feet),"foot, and %.4f"%inch,"inches")
