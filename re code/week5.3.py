def odd_and_sum(lst):
    sumodd=0
    odd = []
    for x in lst:
        if x%2!=0:
            sumodd += x
            odd.append(x)
    return(sumodd,odd)
lst = [4,1,7,9,2,6,8,3]
sum,l = odd_and_sum(lst)
print("Original list:",lst)
print("New odd list:",l)
print("Sum of all odd number:",sum)