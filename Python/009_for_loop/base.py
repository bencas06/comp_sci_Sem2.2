y = int(input("please enter a line lenght"))
z = input("Do you want a horizontal or Vertical line")
if(z=="vertical"):
    for x in range(0,y):
        print(x)
elif(z=="horizontal"):
    for x in range(0,y):
        print(x,end=" ")
        