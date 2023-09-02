s = input("Enter a string: ")
print("Original String =",s)
print("Using function sorted():",sorted(s))
l = list(s)
print("Convert string to list:",l)
print("")
print("Using Bubble Sort")

for x in range(1,len(s)):
    for y in range(0,len(s)-1):
        if l[y]>l[y+1]:
            z = l[y+1]
            l[y+1] = l[y]
            l[y] = z 
    print("After Round %d:"%x,l)
print("Sorted List: ",l)