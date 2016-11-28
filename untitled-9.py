def harmonic(n):
    if (n<=1):
        return 1
    else:
        return (1/n)+harmonic(n-1)   
    
       
def main():
    number=int(input("please enter the number: "))
    a=harmonic(number)
    print("result= %.2f"%a)
         
          
main()