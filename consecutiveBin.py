import sys

n = int(input().strip())
binaryString = bin(n)
count = 0
MAX = 0
binaryString = binaryString[2:]

while len(binaryString)>0:
	if binaryString[0] == '1':
		count +=1
		if count>MAX:
			MAX = count
	else:
		count = 0
	binaryString = binaryString[1:]

print(MAX)