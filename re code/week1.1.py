n = int(input("Width: "))
for x in range(1,n+1):
    for y in range(1,n+1):
        if x==1 or x==n or y==1 or y==n:
            print("*",end="")
        else:
            print(" ",end="")
    print("")