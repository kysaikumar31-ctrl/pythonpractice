for row in range(1,6):
    for space in range(6-row):
        print(" ",end="")
    for star in range(1,row+1):
        print("*",end=" ")
    print()


for i in range(1, 6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()


rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    c = 1
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(c, end=" ")
        c = c * (i - j) // j
    print()

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

