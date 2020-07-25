meta = input()                  
data = input()

metaList = meta.split(' ')
N = int(metaList[0])
M = int(metaList[1])

dataList = data.split(' ')

for i in range (N-1,-1,-1):
    if(int(dataList[i])==M):
        print(i+1)
        break
