w = int(input("Width: ")) 
for n in range(1,w+1):
    if n!=w and n>2 :
        print(str(n)+" "*(n-2)+str(n))
    else : print(str(n)*n)