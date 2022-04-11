#You should print out 3.141592653589793238462643383279502884197169399375105820974
string = ""
crs = open("pi.txt", "r")
s = crs.readline()
while s:
    string += s.strip()
    s = crs.readline()
print(string)

