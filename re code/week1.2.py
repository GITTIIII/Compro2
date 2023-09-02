n = int(input("Width: "))
for x in range(1,n+1):
    for y in range(1,n+1):
        if x==y or x==n or y==1:
            print(x,end="")
        else:
            print(" ",end="")
    print("")