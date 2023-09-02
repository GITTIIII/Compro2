s = input("Enter a sentence: ")
print('"'+s+'"')
alpha = 0
digit = 0
for x in s:
    if True == x.isalpha():
        alpha+=1
    elif True == x.isdigit():
        digit+=1
print("    contain %d letter(s) and %d digit(s)"%(alpha,digit))