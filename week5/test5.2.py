def str_count(s):
    count_upper = 0
    count_lower = 0
    s1 = []

    for x in s :
        if x == " " or x == ".":
            pass
        else:
            s1.append(x)

    for x in s1:
        if x == x.upper():
            count_upper += 1
        elif x == x.lower():
            count_lower += 1
    return(count_lower,count_upper)

s = input("Enter a String: ")
print("Original String:",s)
n1,n2 = str_count(s)
print("Total lower case characters:",n1)
print("Total upper case characters:",n2)