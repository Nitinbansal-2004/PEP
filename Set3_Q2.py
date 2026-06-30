def minTrip(weight):
    weight.sort()
    i = 0
    j = len(weight) - 1
    trips = 0
    while i <= j:
        if i == j:
            trips += 1
            break
        if weight[i] + weight[j] <= 3:
            i += 1
            j -= 1
        else:
            j -= 1
        trips += 1
    return trips

n = int(input())
w = []
for i in range(n):
    w.append(float(input()))
print(minTrip(w))