#Chaitali Patel
#Lecture B2

   


def printsection1(animals, station1, station2):
    print("Number of times each animal visited each station : ")
    print("Animal Id             Station 1             Station 2")
    for a in animals:
        print(a," "*(20-len(a)),station1[a]," "*(20-len(str(station1[a]))),station2[a])
    print("="*60)
        

    
def printsection2(animals, station1, station2):
    print("Animals that visited both stations at least 4 times")
    for item in animals:
        if (station1[item]>=4 and station2[item]>=4):
            print(item)
    print("="*60)
    

    
def printsection3(animals,station1,station2):
    print("Total Number of visits for each animal")
    for a in animals:
        totalVisits=station1[a]+station2[a]
        print(a," "*20,totalVisits)
    print("="*60)

   
    
def printsection4(items):
    print("Print the month that has the highest number of visits to the stations")

    months=[]
    for i in items:
        dates=i[1].split("-")
        months.append(dates[0])
    
    mostVisits=0
    for most in months:
        visits=months.count(most)
        if visits>mostVisits:
            mostVisits=visits
            highestmonth=most
    print(highestmonth)
    
   
    


def main():
    #input
    file1=input("Enter name of input file >")
    try:
        infile=open(file1,"r") 
        
    except IOError:
        print("File does not exist")
        return
        
    #required variables   
    station1={}
    station2={}
    record=()
    items=[]
    animals=[]
    
    #remove blank and comment lines
    for line in infile:
        if len(line)==0 or line[0]=="#" or line[0]=="\n":
            continue
        (animal,time,station)=line.strip("\n").split(":")
        record=(animal,time,station)
        items.append(record)
        
        #Create list of animals
        if animal not in animals:
            animals.append(animal)
            animals=sorted(animals)  
            
    #create dictionary for station 1 and station 2
    for x,y,z in items:
        if z=="s1":
            station1[x] = station1.get(x, 0) + 1        
        else:
            station2[x]= station2.get(x,0)+1
    #if animal doesn't visit station, visits=0
    for a in animals:
        if a not in station1:
            station1[a]=0
        elif a not in station2:
            station2[a]=0
        
                     
    #print all sections
    printsection1(animals,station1,station2)
    printsection2(animals,station1,station2)
    printsection3(animals,station1,station2)
    printsection4(items)
    
    #close file
    infile.close()

main()