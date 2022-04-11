# dic = {'a': 'Hi', 'b': 'there', 'c': 'CS151!'}
# print(dic['a'], dic['b'], dic['c'])

alphabet = {'a': 'a is for apple',
'b': 'b is for banana',
'c': 'c is for cookie',
'd': 'd is for donut',
'e': 'e is for everyone',
'f': 'f is for flipper',
'g': 'g is for goat',
'h': 'h is for happy',
'i': 'i is for igloo',
'j': 'j is for jump',
'k': 'k is for kook',
'l': 'l is for lamb',
'm': 'm is for morning',
'n': 'n is for noon',
'o': 'o is for open',
'p': 'p is for potato',
'q': 'q is for quiet',
'r': 'r is for rooster',
's': 's is for stamp',
't': 't is for truck',
'u': 'u is for umbrella',
'v': 'v is for viking',
'w': 'w is for water',
'x': 'x is for xylitol',
'y': 'y is for yippie',
'z': 'z is for zebra'
}

# print(alphabet['z'])

print(len(alphabet.keys())) #26
print(list(alphabet.keys()) [:5]) #['a','b','c','d','e']
# print(alphabet['a']) # a is for apple
# print(alphabet['b']) # b is for banana
# print(alphabet['z']) # z is for zebra
print(alphabet['a'] + ',', alphabet['b'] + ',', alphabet['z'])
