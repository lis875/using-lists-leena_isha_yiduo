import random

head=0

flip=input("Enter number of coin flips\n")
flip=int(flip)

for i in range(flip):
    num = random.randint(1,2)
    if (num == 1):
        print("Heads")
        head+=1
    else:
        print("Tails")
        
print("Number of heads ", head)
print("Number of tails ", (flip-head))