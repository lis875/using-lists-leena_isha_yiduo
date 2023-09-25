#num_input=input("Enter the number of * you want to print")
sides_input=input("Enter the number of lines you want to print")

for count in range(0,int(sides_input)+1):
    for i in range(0,count):
        print("*", end="")
    
    print("")
  
