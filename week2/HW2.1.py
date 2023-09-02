item = 1
dic = {}
while(item < 5):
    product = input("Product "+str(item)+": ")
    price = int(input("    Price: "))
    dic[product]=price
    item = item+1

p =  max(dic.values())
p1 = max(dic,key=dic.get)

print("Product in dictionary:",dic)
print("Product with the highest price is "+'"'+p1+'"'+".")
print("It price is "+'"'+str(p)+'"'+" baht"+".")     