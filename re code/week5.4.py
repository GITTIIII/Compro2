n = int(input("Enter a number: "))
prime=1
for x in range(2,n):
    if n%x==0:
        prime=0

if prime==0:
    print("%d is not a prime number."%n)
else:
    print("%d is a prime number."%n)
        