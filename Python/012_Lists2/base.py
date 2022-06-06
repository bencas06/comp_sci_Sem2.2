import random
x = int(input("How many numbers would you like to imput?"))
thislist = [1,2,3,4,5,6,7,8,9,10]

for y in range(0,x):
    c = random.choice(thislist)
    print(c , end = " , ")