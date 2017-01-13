#myDict={"one":"uno","two":"dos",3:"tres"}
#in operator works for keys not values


def histogram(str):
    d=dict()
    for char in str:
        if char not in d:
            d[char]=1
        else:
            d[char]=d[char]+1
    return d

def print_hist(ahistogram):
    for item in ahistogram:
        print(item,ahistogram[item])
        
#reverse look up        
'''
def reverse(d,v):
    for k in d:
        if d[k] == v:
            print(k) 
            '''
def main():
    result=histogram('parrot')
    print_hist(result)

#can use list as values but not keys
#can use tuples as keys b/c they are non-mutable
main()