x=[]
n=int(input("Enter number of students: "))
for a in range (0,n):
    a=int(input("Enter marks: "))
    while (a>50):
        print("Invalid input")
        a=int(input("Re-enter marks: "))
    x.append(a)
print(x)

def absent(x):
    count=0
    for i in range (0,n):
        if x[i]==-1:
            count=count+1
    return (count)
print(absent(x))
    
def sum(x):
    sum=0
    for i in range (0,n):
        if x[i]!=-1:
            sum=sum+x[i]
    return (sum)
print(sum(x))

def avg(x):
    sum=0
    for i in range (0,n):
        if x[i]!=-1:
            sum=sum+x[i]
    if (n-absent(x))==0:
        average=0
    else: 
        average=(sum/(n-absent(x)))

    return (average)
print(avg(x))

def highest(x):
    y=x[0]
    #for c in range (0,n):
        #if x[c]!=-1:
    for i in range(0,n):
        if y<x[i]:
            y=x[i]
        else:
            pass
        #else:
            #pass
    if y == -1:
        y = 0
    return(y)
print(highest(x))

def lowest(x):
    y=x[0]
    #for c in range (0,n):
        #if x[c]!=-1:
    for i in range(0,n):
        if y==-1 or (x[i]!=-1 and y>x[i]):
            y=x[i]
        #else:
            #pass
    if y == -1:
        y = 0
    return(y)
print(lowest(x))