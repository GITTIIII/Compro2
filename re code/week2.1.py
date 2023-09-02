i = 1
dic = {}

while(i<=4):
    pro = input("Product %d: "%i)
    pri = int(input("    Price: "))
    dic[pro] = pri
    i+=1

maxpro = max(dic,key=dic.get)
maxpri = max(dic.values())
print("Product in dictionary:",dic)
print("Product with the highest price is "+'"'+maxpro+'".')
print('Its price is "%d" baht.'%maxpri)