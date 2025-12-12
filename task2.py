i = int(input("input a number"))
summ=0
while i > 0:
    summ += i % 10
    i //= 10
print(summ)
