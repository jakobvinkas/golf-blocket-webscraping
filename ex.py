

class car:
    def __init__(self, year, price, mile):
        self.year = year
        self.price = price
        self.mile = mile

import csv
import matplotlib.pyplot as plt



car_array = []
with open('golf.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row  in reader:
        year = int(row[0])
        price = int(row[1])
        mile = int(row[2])
        car_array.append(car(year,price,mile))

plt.plot((4000,14000),(100000,100000),'--', color = 'black')

for car in car_array:
    if car.year == 2014:
        plt.scatter(car.mile, car.price, color = 'b',marker = 'o', label = car.year)
    elif car.year == 2015:
        plt.scatter(car.mile, car.price, color = 'g',marker = 'o', label = car.year)

handles, labels = plt.gca().get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.xlabel('Mil')
plt.ylabel('Pris')
plt.title('Golf bilar på blocket')
#plt.grid()
plt.show()
