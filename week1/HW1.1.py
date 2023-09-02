w = int(input("Width: "))
for n in range(1,w+1):
    if n==1 or n==w :
        print("*"*w)
    else : print("*"+" "*(w-2)+"*")