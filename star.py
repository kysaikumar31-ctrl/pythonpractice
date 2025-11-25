
for i in range(1, 6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(1, i+1):
        print("*", end=" ")
    print()


for i in range(1,5):
    print("*"*i)

for i in range(5,0,-1):
    print("*"*i)