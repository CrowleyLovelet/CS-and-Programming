while True:
    chis = input("input a bin number: ")

    valid = True
    for c in chis:
        if c not in "01":
            valid = False
            break
    if valid and chis != "":
        break
norm = 0
for c in chis:
    norm = norm * 2      
    if c == "1":
        norm += 1      

print(norm)
