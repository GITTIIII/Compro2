while(1):
    n = int(input("How many number (5-20): "))
    if n<5 or n>20:
        print("Invalid Number!!!")
    else:
        break

lst = []
x = 1
while(x<=n):
    n1 = int(input("Number %d: "%x))
    lst.append(n1)
    x+=1

index = 0
found = 0
s = int(input("Enter a number to be searched: "))
for y in lst:
    if y==s:
        print("Found number %d at index %d"%(s,index))
        found += 1
    index += 1
    
if found==0:
    print("Cannot find number %d"%s)
else:
    print("Total found = %d"%found)