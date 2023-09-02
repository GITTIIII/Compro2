def str_reverse(s):
    l = 0
    re = ""
    while(l<=len(s)-1):
        re += s[len(s)-l-1]
        l+=1
    return(re)

s = input("Enter a string: ")
re = str_reverse(s)
print("Original string :",s)
print("Reverse string:",re)