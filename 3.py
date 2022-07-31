f = open('17(3).txt')
m = [int(i) for i in f]
k = 0
sr = sum(m) / len(m)
for i in range(len(m)):
    if m[i] < sr:
        k += 1
print(int(sr),k)


