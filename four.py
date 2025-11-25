fact=1
x={fact:=fact*i for i in range(1,6)}
print(x)

x=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(x)):
    for j in range(len(x[0])):
        print(x[i][j])

matrix = [[j for j in range(i, i+2)] for i in range(1,5)]
for i in matrix:
    print(i)