for i in range(3):
    for j in range(3-i-1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

rows = int(input("Enter the number of rows: "))
for i in range(1, rows+1):
    c = 1
    for j in range(rows-i):
        print(" ",end="")
    for j in range(1, i+1):
        print(c, end=" ")
        c = c*(i-j)//j
    print()