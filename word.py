import sys

f = open('final.txt', 'rb')

for line in f:
    #txt = line.strip()
    string = str(line)
    length = int(len(string))
    new = string[2:length-3]
    space = new.replace(',', ' ')
    print(space)
