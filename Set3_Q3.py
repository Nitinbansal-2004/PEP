n = int(input())
pnl = []
for i in range(n):
    pnl.append(int(input()))
k = int(input())
n = len(pnl)

max_sum = 0
for i in range(n):
    for j in range(i, min(i + k, n)):
        max_sum += pnl[j]
        
print(max_sum)