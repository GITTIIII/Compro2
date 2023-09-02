while(True):
    n = int(input("Enter an odd base (3-9): "))
    if n<3 or n>9 or n%2==0 :
        print("Invalid number!!!")
        print("The number must be an odd number from 3 to 9.")
    else : break

mid = n//2+1
mid1 = mid 

for r in range(1,mid+1):
    for num in range(1,r+1):
        print(r,end="")
    print("")

for r in range(mid+1,n+1):
    for botnum in range(1,mid1):
        print(r,end="")
    mid1 = mid1-1
    print("")    