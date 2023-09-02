def sum_of_n(n):
    if n==1:
        print("%d = "%n,end="")
        return(1)
    print("%d+"%n,end="")
    return(n+sum_of_n(n-1))

n = int(input("Enter a number: "))
sum = sum_of_n(n)
print(sum)