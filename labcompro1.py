print("--- Part 1 ---")
while(1):
    n = int(input("How many string (2-6): "))
    if n<2 or n>6:
        continue
    else:
        break
print("")

print("--- Part 2 ---")
s = 1
l =  []
while(s<=n):
    str = input("String %d: "%s)
    l.append(str)
    s += 1
print("")

print("--- Part 3 ---")
for x in range(len(l)):
    print("String %d: %30s--> Length = %d"%(x+1,l[x],len(l[x])))
print("")
print("Maximum: %-30s, Length = %d"%(max(l,key = lambda l : len(l)) ,max(len(x) for x in l)))
print("Minimum: %-30s, Length = %d"%(min(l,key = lambda l : len(l)) ,min(len(x) for x in l)))