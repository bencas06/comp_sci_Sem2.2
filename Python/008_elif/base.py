x = int(input("Input an integer"))
z = int(input("Input another integer"))
y = input("Input an operator")
a = (x*z)
b = (x/z)
c = (x-z)
d = (x+z)
if(y== "*"):
    print(str(x) + "*" + str(z) + "=" + str(a))
elif(y=="/"):
    print(str(x) + "/" + str(z) + "=" + str(b))
elif(y=="-"):
    print(str(x) + "-" + str(z) + "=" + str(c))
else:
    print(str(x) + "+" + str(z) + "=" + str(d))

