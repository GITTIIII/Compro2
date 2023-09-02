while(True):
    num = int(input("How many word? (3-5): "))
    if num<3 or num>5:
        print("Invalid number!!!")
    else: break

w = 1
dic = {}
while(w<4):
    word = input("Word "+str(w)+": ")
    dic[word]=len(word)
    w = w+1
print("Data in the dictionary:",dic)