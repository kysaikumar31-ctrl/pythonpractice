for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(i, "is not prime")
            break
    else:
        print(i, "is prime")

#2
for i in range(2, 10):
    if i % 2 == 0:
        print(i, "is even number")
    else:
        print(i, "is odd number")

fno = 0
sno = 1
while sno < 500:
    fib = fno + sno
    fno = sno
    sno = fib
    print(fib)