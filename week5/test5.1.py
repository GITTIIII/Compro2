def str_reverse(s):
    n = len(s)
    s1 = ""
    while 0!=n:
        s1 = s1+s[n-1]
        n -=1
    return(s1)

s = input("Enter a String: ")
print("Original String:",s)
re = str_reverse(s)
print("Reversed String:",re)