n = input("Enter numbers separated by a space: ")
l = n.split()
print(l)
s = set(l)

if len(l) == len(s):
    print("All numbers are different.")
else :
    print("Some numbers are repeated!!!")