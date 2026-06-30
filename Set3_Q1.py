from collections import Counter

text = input()
k = int(input())
words = text.split()
ans = []
visited = set()
count = Counter(words)

for i in words:
    if i not in visited and count[i] >= k:
        ans.append(i)
        visited.add(i)

print(ans)
