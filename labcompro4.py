num = []
while(1):
    n = int(input("How many number (4-10): "))
    if n<4 or n>10:
        continue
    else:
        break

x = 1
while(x<=n):
    n1 = int(input("number[%d]: "%x))
    num.append(n1)
    x+=1
print("")

z=1
sumall = 0
sumeven = 0
sumodd = 0
countall = 0
counteven = 0
countodd = 0
for y in num:
    if y%2==0:
        print("number[%d]: %-15d==> is an even number."%(z,y))
        sumall += y
        countall += 1
        sumeven += y
        counteven += 1
        z += 1
    else:
        print("number[%d]: %-15d==> is an odd number."%(z,y))
        sumall += y
        countall += 1
        sumodd += y
        countodd += 1
        z += 1

print('\nSum of all number is "%d".'%sumall)
print('Sum of even number is "%d".'%sumeven)
print('Sum of odd number is "%d".'%sumodd)
print('Number of all number is "%d".'%countall)
print('Number of even number is "%d".'%counteven)
print('Number of odd number is "%d".'%countodd)