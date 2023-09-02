while(1):
    n = int(input("How many word? (3-5): "))
    if n<3 or n>5:
        print("Invalid number!!!")
    else:
        break

w = 1
dic = {}
while(w<=n):
    word = input("Word %d: "%w)
    dic[word] = len(word)
    w+=1

print("Data in dictionary:",dic)