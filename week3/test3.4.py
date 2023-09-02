s = input("Enter 5 numbers seperated by space: ")
s = s.split()
i = []

for x in (s):
    i.append(int(x))

print("Original:",i)
print("Step 1: Add 8 and 4 to the end of the list")
i.append(8)
i.append(4)
print("    ",i)
print("Step 2: insert 2 after 3 and 6 after 5")
i.insert(1,2)
i.insert(4,6)
print("    ",i)
print("Step 3: remove 1 and 8")
i.remove(1)
i.remove(8)
print("    ",i)