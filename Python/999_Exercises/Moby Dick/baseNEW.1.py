sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
count = 0 
for i in range(0,len(sentence)):
    if sentence[i:i+5] == "whale":
        count= count + 1
        
print(count)