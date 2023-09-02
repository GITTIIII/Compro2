while(1):
    n = int(input("Enter an odd base (3-9): "))
    if n<3 or n>9 or n%2==0:
        print("Invalid number!!!")
        print("The number must be an odd number from 3 to 9.")
    else:
        break

mid = n//2+1
for x in range(1,mid+1):
    print("Row %d ->  "%x,end="")
    for y in range(1,mid+1):
        if y==mid or y>mid-x:
            print(y,end="")
        else:
            print(" ",end="")
    for y in range(mid+1,n+1):
        if y<mid+x:
            print(y,end="")
    print("")