import random

head=0

for i in range(20):
    num = random.randint(1,2)
    if (num == 1):
        print("Heads")
        head+=1
    else:
        print("Tails")
        
print("Number of heads ", head)
print("Number of tails ", (20-head))