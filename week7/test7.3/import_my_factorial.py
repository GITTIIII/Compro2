import my_factorial
while(1):
    n = int(input("Enter a number (1-100): "))
    if n < 1 or n> 100:
        print("Invalid Input!!!")
    else:
        break

print("Calculate Factorial Using Loop")
print("%d! = "%n,end="")
facloop = my_factorial.Fac.loop(n)
print("%d! = %d"%(n,facloop))

print("Calculate Factorial Using Recursion")
print("%d! = "%n,end="")
facre = my_factorial.Fac.recursive(n)
print("%d! = %d"%(n,facre))
