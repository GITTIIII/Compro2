import csv
with open("worker.csv","r") as file:
    read = csv.reader(file)
    print('{:10}{:5}{:20}{:12}{:6}'.format("Name","Age","E-mail","Mobile","Sex"))
    for x in read:
        print('{:10}{:5}{:20}{:12}{:6}'.format(x[0],x[1],x[2],x[3],x[4])) 
file.close()