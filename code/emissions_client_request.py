import random
import matplotlib.pyplot as plt

class Vehicle:
    def __init__(self,sdv_probability):
        r = random.random()
        if r < sdv_probability:
            self.is_self_driving = True
        if r > sdv_probability:
            self.is_self_driving = False

        if self.is_self_driving:
            self.speed = random.randint(50,80)
        else:
            self.speed = random.randint(10,100)

    def get_emissions(self):
        emission = round(0.0019 * self.speed**2 - 0.2506* self.speed + 13.74, 3)
        return emission

#car1 = Vehicle(0.2)
#print(car1.get_emissions())

def average_calculate(k):
    cars = []
    emissions = []

    for i in range(10000):
        cars.append(Vehicle(k))
    for j in cars:
        emissions.append(j.get_emissions())
    average = (sum(emissions)/len(emissions))
    return average

average = []
for i in range(1,11):
    average.append(average_calculate(i/10))

plt.plot([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],average, label = "Freq:5")
plt.ylabel('emission[L/100Km]')
plt.xlabel('sdv probability[%]')
plt.show()