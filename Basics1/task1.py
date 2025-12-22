
numbers =[int(chis) for chis in input("input some numbers").split()]
maxi = numbers[0]
mini = numbers[0]
for i in numbers:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print("max is ", maxi,"min is", mini)
