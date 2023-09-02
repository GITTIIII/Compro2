import my_factorial
while(1):
    n = int(input("Enter a number (1-100): "))
    if n<1 or n>100:
        print("Invalid Input!!!")
    else:
        break
print("Calculate Factorial Using Loop")
print("%d! = "%n,end="")
f = my_factorial.Fac.loop(n)
print("\n%d! = %d"%(n,f))

print("Calculate Factorial Using Recursion")
print("%d! = "%n,end="")
f = my_factorial.Fac.recursive(n)
print("\n%d! = %d"%(n,f))