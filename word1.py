import sys

f = open('raw.txt', 'rb')

for line in f:
    #txt = line.strip()
    string = str(line)
    length = int(len(string))
    print(string[45: length-3])
