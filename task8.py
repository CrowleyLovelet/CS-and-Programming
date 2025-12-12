number = input("Введите число: ")
length = 0
for h in number:
    length += 1
i= 0
while i < length:
    digit = int(number[i])
    power = 10 ** (length - i - 1)
    print(digit * power)
    i += 1
    if i < length:
        print('+')
    
