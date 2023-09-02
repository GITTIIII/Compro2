def dec_2_oct(n):
    if n>0:
        dec_2_oct(int(n/8))
        print("%d"%(n%8),end="")
        

n = int(input("Enter an integer: "))
print("Decimal %d = "%n,end="")
dec_2_oct(n)
print(" Octal")