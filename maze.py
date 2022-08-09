def show(Map):
    for i in Map:
        print(*i)


n = list(map(int,input().split()))
Map = [[0 for i in range(len(n))] for j in range(len(n))]
index = 0
for i in range(0,len(n)):
    for j in range(0,len(n)):
        if j==index:
            Map[i][j] = 0
        else:
            if j<i:
                Map[i][j]
    index+=1




