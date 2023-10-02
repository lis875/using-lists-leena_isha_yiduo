import random

restaurants = []

res_num = input("How many places are you thinking about for lunch?\n")
res_num = int(res_num)

for i in range(res_num):
    place = input("Enter the name of restuarant " + str(i+1) + ": ")
    restaurants.append(place)

result = int(random.randint(1,res_num))
print("You should go to", restaurants[result])