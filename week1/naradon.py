while(True):
    n = int(input("Enter an odd base (3-9): "))
    if n<3 or n>9 or n%2==0 :
        print("Invalid number!!!")
        print("The number must be an odd number from 3 to 9.")
    else : break

mid = n//2+1
limit_first = mid 
limit_second = mid

row = 1

while(row <= mid):
    count = 1
    
    while(count <= mid):
        if(count >= limit_first):
            print(count, end = "")
        else:
            print(" ", end = "")
        count = count + 1
    print("")
        
    
    

    limit_first = limit_first - 1
    limit_second = limit_second + 1
    row = row + 1
    