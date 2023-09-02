def str_count(s):
    countlow = 0
    countup = 0
    for x in s:
        if x>='a' and x<='z':
            countlow+=1
        elif x>='A' and x<='Z':
            countup+=1
    return(countlow,countup)
s = input("Enter a string: ")
low,up = str_count(s)
print("Original string:",s)
print("Total lower case characters:",low)
print("Total upper case characters:",up)