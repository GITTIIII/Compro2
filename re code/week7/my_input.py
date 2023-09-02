def get(l,h):
    while(1):
        n = int(input("Enter a number (%d-%d): "%(l,h)))
        if n<l or n>h:
            print("Invalid Input!!!")
        else:
            return(n)