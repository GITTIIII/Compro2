print("--- Part 1 ---")
while(1):
    n = int(input("How many integer (5-10): "))
    if n<5 or n>10:
        print("Must be 5 to 10")
    else:
        break
print("")

print("--- Part 2 ---")
num = []
x = 1
while(x<=n):
    n1 = int(input("Number %d = "%x))
    num.append(n1)
    x+=1
print("Number =",num)
print("")

print("--- Part 3 ---")
sum = 0
n2 = 1
for x in num:
    print("Number %d ==> %d"%(n2,x))
    if x%2==0:
        print("\t%d is added."%x)
        sum+=x
    else:
        print("\t%d is an odd number and it is not added."%x)
    n2+=1
print("Total sum of even numbers is %d."%sum)