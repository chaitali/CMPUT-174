def leapyr(yr):
    if (yr%4==0 and yr%100!=0) or (yr%400==0):
        return True
    else:
        return False
    
def main():
    year=int(input("Enter year: "))
    n=leapyr(year)
    print(n)
main()