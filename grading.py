with open('msft.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word)    