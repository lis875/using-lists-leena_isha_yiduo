import random

restaurants = []

for i in range(3):
    place = input("Enter the name of restuarant " + str(i+1) + ": ")
    restaurants.append(place)

result = int(random.randint(1,3))
print(restaurants[result])