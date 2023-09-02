s = input("Enter a sentence: ")
print('"'+s+'"')
l = 0
d = 0

for x in (s) :
    if True == x.isalpha():
        l = l+1
    elif True == x.isdigit():
        d = d+1
        
print("contains %d letter(s) and %d digit(s)"%(l,d))