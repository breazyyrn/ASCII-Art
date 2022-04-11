string = ""
mks = open("digits.txt", "r")
k = mks.readline()
while k:
    string += k.strip()
    string += " "
    k = mks.readline()

newString = "\n".join(string.split())
print(newString)


'''This code creates a new file named 'digits2.txt' with values derived from 'newString' '''
bks = open("digits2.txt", "w")
bks.write(newString)
bks.close()
