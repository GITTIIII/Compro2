while(1):
    n = int(input("How many number (5-20): "))
    if n<5 or n>20:
        print("Invalid Number!!!")
    else:
        break

lst = []
x = 1
while(x<=n):
    error = 0
    n1 = int(input("Number %d: "%x))
    if (n1 in lst):
        print("Invalid!!!, %d is already in the list"%n1)
        error = 1
    if error==0:
        lst.append(n1)
        x+=1
    
print("Original data:",lst)
lst = sorted(lst)
print("Sorted data:",lst)

s = int(input("Enter a number to be searched: "))
left = 0
right = len(lst)-1

while(left <= right):
    if s in lst:
        mid = (left+right)//2
        if lst[mid]==s:
            print("Found '%s' at index %d"%(s,mid))
        if lst[mid] < s:
            left = mid+1
        else:
            right = mid-1
    else:
        print("Cannot find number %d"%s)
        break