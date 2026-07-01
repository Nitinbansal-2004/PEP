n = int(input())
pnl = []
for i in range(n):
    pnl.append(int(input()))
k = int(input())
max_sum = 0
for i in range(n):
    curr_sum=0
    for j in range(i, min(i + k, n)):
        curr_sum += pnl[j]
    if max_sum<curr_sum:
        max_sum=curr_sum
        
print(max_sum)


