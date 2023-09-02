s = "ANIMALS"
index = 0

str = input("Enter a character to be searched: ")
found = 0

for x in s:
    if str==x:
        found = 1
        break
    index += 1

if found==1:
    print("Found '%c' at index %d"%(str,index))
else:
    print("Cannot find '%c'"%str)