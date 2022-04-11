'''Opens file'''
wholeFile = open("abcs2.txt", "r")
'''reads file'''
bigString = wholeFile.read()
allLines = bigString.split('\n')
correctedLines = []
letterDict = {}
for i in range (len(allLines) -1):
    if i % 3 == 0:
        entry = allLines[i] + ' ' + allLines[i+1] + ' ' + allLines[i+2]
        # print(entry)
        letterDict[allLines[i]] = entry
print(letterDict)



