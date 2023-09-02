import csv
data = [["Preecha",32,"preecha@gmail.com","0894257777","Male"],
        ["Dara",28,"dara_dara@gmail.com","0866442277","Female"],
        ["Busara",29,"b_sara@yahoo.com","0991112229","Female"],
        ["Suradej",41,"dej_2020@gmail.com","0959595111","Male"]]
with open("worker.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
file.close()