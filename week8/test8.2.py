l = []
while(1):
    n = int(input("How many number (5-10): "))
    if n<5 or n>10:
        print("Invalid Number!!!")
    else:
        break

x = 1
while(x<=n):
    n1 = int(input("Number %d: "%x))
    l.append(n1) 
    x+=1

print("Original List:",l)
for x in range(len(l)-1):
    min = x
    for y in range(x+1,len(l)):
        if l[y]<l[min]:
            min = y
    if min != x:
        z = l[x]
        l[x] = l[min]
        l[min] = z 
    print("After Round %d:"%(x+1),l)
print("Sorted List:",l)