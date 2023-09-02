with open("number.txt","w") as num :
    for x in range(1,101):
        if x<10:
            num.write("00%d "%x)
        elif 10<=x<100:
            num.write("0%d "%x)
        else:
            num.write("%d "%x)
        if x%10==0 and x!=100:
            num.write("\n")