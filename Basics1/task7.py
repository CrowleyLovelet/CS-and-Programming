number=int(input("dec number"))
binnum=''
while number > 0:
    binnum= str(number % 2) + binnum
    number//=2
print(binnum)
