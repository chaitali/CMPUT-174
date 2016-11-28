def isDivisible(number):
    total=0
    for item in number:
        total=int(item)+total
    if total%7==0:
        print("True")
    else:
        print("False")
        
def main():
    n=input("Enter number: ")
    isDivisible(n)
    
main()