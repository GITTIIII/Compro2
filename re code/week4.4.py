counteven = 0
sumeven = 0
print("Even number from 20 to 44: ",end="")
for x in range(20,45):
    if x%2==0:
        print(x,end=" ")
        counteven+=1
        sumeven+=x
print("There are %d even numbers."%counteven)
print("Sum of all even numbers are %d."%sumeven)

countodd = 0
sumodd = 0
print("Odd number from -5 to -29: ",end="")
for x in range(-5,-30,-1):
    if x%2!=0:
        print(x,end=" ")
        countodd+=1
        sumodd+=x
print("There are %d odd numbers."%countodd)
print("Sum of all odd numbers are %d."%sumodd)