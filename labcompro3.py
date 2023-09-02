print("--- Part 1 ---")
while(1):
    n = int(input("How many name(2-6): "))
    if n<2 or n>6:
        continue   
    else:
        break

name = []
x = 1
print("\n--- Part 2 ---")
while(x<=n):
    n1 = input("Name %d: "%x)
    name.append(n1)
    x+=1


z = 1
print("\n--- Part 3 ---")
for x in name:
    lastname = x.split(" ")
    print("Name %d:"%z,x)
    print("   Last name = %s"%lastname[1])
    print("   Total last name length is %d"%len(lastname[1]))
    z+=1