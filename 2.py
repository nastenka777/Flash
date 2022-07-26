f = open('17(2).txt')
m = list(map(int, f.readlines()))
sr = 0
k, k1 = 0, 0
mn = 10 ** 10
for i in range(len(m)):
    if m[i] > 55:
        sr += m[i]
        k1 += 1
sr /= k1
print(sr)
for i in range(len(m)):
    if m[i] > sr:
        k += 1
        mn = min(mn, m[i])
print(k, mn)

