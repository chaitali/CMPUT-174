#Chaitali Patel
#Lecture B2
#Lab H05

#input
cases=int(input("Enter number of cases: "))
#initialize loop 1 control
totalcases=1 

#loop 1
while(totalcases<=cases):
    
    print("Case", totalcases)
    
    num_students=int(input("Enter number of students: "))
    total_students=0 #loop 2 control
    total_mark=0
    highest=0
#loop 2    
    while(total_students<num_students):
        name=input("Enter name of student: ")
        mark=int(input("Enter mark of student: "))
        total_mark=total_mark+mark
        total_students=total_students+1
        if(mark>highest):
            highest=mark
            highscore_student=name
            
    average=total_mark/total_students
    
#output    
    print("Case", totalcases,"Result")
    print("Average is: %.2f"%average)
    print("Highest Score is: %.2f"%highest)
    print("Student with the highest score is: ",highscore_student)
    totalcases=totalcases+1 #loop 1 control variable
    
