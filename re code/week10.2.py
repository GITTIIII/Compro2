with open("number.txt","r") as num:
    for x in num:
        n = x.split(" ")
        for y in n:
            if y=="\n" or y=="":
                pass
            else:
                y = int(y) 
                if y%10==0:
                    print("%4d"%y)
                else:
                    print("%4d"%y,end=" ")
num.close()