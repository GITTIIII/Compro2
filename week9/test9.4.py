s = "BANGPRETOY"
print("Original data:",s)
s = sorted(s)
print("Sorted data:",s)
search = input("Enter a character to be searched: ")

left = 0
right = len(s)-1
while(left<=right):
    if search in s:    
        mid = (left+right)//2
        if s[mid]==search:
            print("Found '%s' at index %d"%(search,mid))
        if s[mid] < search:
            left = mid+1
        else:
            right = mid-1
    else:
        print("Cannot find '%s'"%search)
        break