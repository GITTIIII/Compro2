while(True):
    n = int(input("Enter an odd base (3-9): "))
    if n<3 or n>9 or n%2==0 :
        print("Invalid number!!!")
        print("The number must be an odd number from 3 to 9.")
    else : break

mid = n//2+1
mid1 = mid
mid2 = mid

for r in range(1,mid+1):
    print("Row",r,"-> ",end="")

    for space in range(1,mid1+1,1):
        print(end=" ")

    for fontnum in range(mid1,mid+1,1):
        print(fontnum,end="")
    
    for backnum in range(mid+1,mid2+1,1):
        print(backnum,end="")
    
    for space in range(mid,mid1,1):
        print(end=" ")
         
    mid1 = mid1-1
    mid2 = mid2+1
    print("")