
print("----------Capital Alphabet Patten------------")
Asci = 65
rows = 9

for i in range(1, rows):
    for j in range(1, i):
        Charater = chr(Asci)
        Asci += 1
        print(Charater, end='')
    print("")

print("----------Small Alphabet Patten------------")
Asci = 97
rows = 9

for i in range(1, rows):
    for j in range(1, i):
        Charater = chr(Asci)
        Asci += 1
        print(Charater, end='')
    print("")