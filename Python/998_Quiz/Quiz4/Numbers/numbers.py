mynumbers = [6,9,32,28,15,22,3,18]
lownum = 100
for i in mynumbers:
    if i < lownum:
        lownum = i
print(lownum)


highnum = 0 
for i in mynumbers:
    if i > highnum:
        highnum = i
print(highnum)


b = 0 

for i in mynumbers:
    b+=i
avg = b / float(len(mynumbers))
print(avg)