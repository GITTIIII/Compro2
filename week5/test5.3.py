def odd_and_sum(l):
    newl = []
    sum_newl = 0
    for x in l:
        if x%2!=0:
            newl.append(x)
            sum_newl +=x
    return(newl,sum_newl)
l = [4,1,7,9,2,6,8,3]
print("Original list:",l)
newl,sum_newl = odd_and_sum(l)
print("New odd list:",newl)
print("Sum of all odd number:",sum_newl)