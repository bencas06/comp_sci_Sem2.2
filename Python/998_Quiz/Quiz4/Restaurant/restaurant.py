import random
mylist = ["McDonalds","King Taco","Burger King"]
mclist = ["Big mac", "chicken nuggets", "happy meal"]
kinglist = ["burrito","Tacos","sopes"]
burgerlist = ["footlettuce","whopper","bacon king"]
y = random.choice(mylist)
print(y)
if y == "McDonalds":
    x = random.choice(mclist)
    print(x)
elif y == "King Taco":
    b = random.choice(kinglist)
    print(b)
elif y == "Burger King":
    n = random.choice(burgerlist)
    print(n)
    


    
