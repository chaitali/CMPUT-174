def MergeTwoStrings(s1,s2):
    if (len(s1)<=len(s2)):
        j=len(s1)
        rem=s2[j:]
    else:
        j=len(s2)
        rem=s1[j:]
    i=0
    s3=""
    
    while(i<j):
        s3=s3+s1[i]+s2[i]
        i=i+1
    return s3+rem

def main():
    k="litmus"
    l="paper"
    a=MergeTwoStrings(k,l)
    print(a)
    
main()
    