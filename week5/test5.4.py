def check_prime(num):
    if num%num==0 and num%1==0 and num%2!=0 and num%3!=0:
        a = "is a prime number."
    else:
        a = "is not a prime number."
    return(a)

num = int(input("Enter a number: "))
a = check_prime(num)
print(num,a)

