s = input("Enter a string: ")
print("Original String =",s)
print("Using function sorted():",sorted(s))
s = list(s)
print("Convert string to list:",s)
print("")
print("Using Bubble Sort")

r=1
while(r<len(s)):
    for x in range(0,len(s)-1):
        if s[x]>s[x+1]:
            z = s[x+1]
            s[x+1] = s[x]
            s[x] = z
    print("After Round %d:"%r,s)
    r+=1
print("Sorted List:",s)