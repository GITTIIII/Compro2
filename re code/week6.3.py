def dec_2_hex(n):
    hex = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',}
    if n>0:
        dec_2_hex(int(n/16))
        print(hex[n%16],end="")

n = int(input("Enter an integer: "))
print("Decimal %d = "%n,end="")
dec_2_hex(n)
print(" Hexadecimal")