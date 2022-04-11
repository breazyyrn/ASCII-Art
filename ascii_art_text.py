import graphics as gr 
import sys

def compose():
    alphabet = open('colossalFontAlphabet.txt')
    symbol = open('colossalFontSymbols.txt')
    '''Creates empty list'''
    alphabetList = []
    '''Reads ColossalFontAlphabet.txt line by line'''
    currentLine = alphabet.readline()
    '''Loops around characters read colosssalFontAlphabet.txt line by line'''
    for char in currentLine:
        '''Appends the characters read to the empty list alphabetList'''
        alphabetList.append(char)
        '''Creates empty dictionary'''
    myDic = {}
    '''Loops around the characters appended to the empty list before'''
    for items in alphabetList:
        '''Makes an empty list named listString'''
        listString = []
        for j in range (11):
            '''Appends characters read from the text colossalFontsymbols.txt to the listString empty list 11 times in order to have 11 lines.'''
            listString.append(symbol.readline().strip('\n'))
            '''Assigns the value of the items within the myDic from the symbol characters recently appended to the empty liststring list.'''
        myDic[items] = listString
        '''Returns the characters from the symbols file'''
    return myDic

def createString(string):
    '''Gets items from 'myDic' dictionary in order to convert the input to ascii image'''
    listString = []
    for char in string:
        listString.append(char)
    print(listString)

    symbolsDic = compose()
    lastString = ''
    for x in range(11):
        for items in listString:
            lastString += symbolsDic[items][x]
        lastString += '\n'
    print(lastString)

if __name__ == '__main__':
    '''Command line argument position 1'''
    createString(sys.argv[1])
    