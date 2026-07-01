from collections import Counter

text = input()
k = int(input())
words = text.split()
count = Counter(words)
ans = []

for i in count:
    if count[i] >= k:
        ans.append(i)
print(ans)
