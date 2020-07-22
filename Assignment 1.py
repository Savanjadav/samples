x=[]
n=int(input("Enter number of students: "))
for a in range (0,n):
    a=int(input("Enter marks: "))
    while (a>50):
        print("Invalid input")
        a=int(input("Re-enter marks: "))
    x.append(a)

#Number of absent students
def absent(x):
    count=0
    for i in range (0,n):
        if x[i]==-1:
            count=count+1
    return (count)

#Sum of marks   
def sum(x):
    sum=0
    for i in range (0,n):
        if x[i]!=-1:
            sum=sum+x[i]
    return (sum)

#Average of marks
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

#Percentage of marks
def percentage(x):
    if (n-absent(x))==0:
        percentage=0
    else:
        percentage = (((sum(x) / ((n-absent(x)) * 50)) * 100))
    return(percentage)

#Maximum marks
def highest(x):
    y=x[0]
    for i in range(0,n):
        if y<x[i]:
            y=x[i]
    if y == -1:
        y = 0
    return(y)

#Minimum marks
def lowest(x):
    y=x[0]
    for i in range(0,n):
        if y==-1 or (x[i]!=-1 and y>x[i]):
            y=x[i]
    if y == -1:
        y = 0
    return(y)
 
#For sepratinng the marks wrt to their range
lst1,lst2,lst3,lst4,lst5,abs=[],[],[],[],[],[]
for i in x:
    if (i==-1):
        abs.append(i)
    else:
        if (i>=0 and i <=10):
            lst1.append(i)
        elif (i>10 and i<=20):
            lst2.append(i)
        elif (i>20 and i<=30):
            lst3.append(i)
        elif (i>30 and i<=40):
            lst4.append(i)
        else:
            lst5.append(i)
#finding the frequency of each score range
pl1,pl2,pl3,pl4,pl5,pl6=len(lst1),len(lst2),len(lst3),len(lst4),len(lst5),len(abs)  
length=[pl1,pl2,pl3,pl4,pl5,pl6]
maxlength=0
#to get the highest frequency range
for i in length: 
    if (i>maxlength):
        maxlength=i
    
# class stats declaration
print("Marks of student are:",x)
print("No. of absent students are:",absent(x))
print("Maximum marks are:",highest(x))
print("Minimum marks are:",lowest(x))
print("Total marks of all students are:",sum(x))
print("Average marks of students are:",avg(x))
print("Percentage marks are {}%".format(percentage(x)))
if (maxlength==pl1):
    print("The highest frequency range is 0-10")
elif(maxlength==pl2):
    print("The highest frequency range is 11-20")
elif(maxlength==pl3):
    print("The highest frequency range is 21-30")
elif(maxlength==pl4):
    print("The highest frequency range is 31-40")
elif(maxlength==pl5):
    print("The highest frequency range is 41-50")
elif(maxlength==pl6):
    print("All students are absent")
