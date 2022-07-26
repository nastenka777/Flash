f = open('17(1).txt')
m = list(map(int, f.readlines()))
l = len(m)
k, mxk, mx = 0, 0, 0
for i in range(l - 3):
    a, b, c, d = m[i], m[i + 1], m[i + 2], m[i + 3]
    if a < b < c < d:
        k = 4
        mxk = max(mxk, k)
        mx = max(mx, d)
        for j in range(i + 4, l):
            h = m[j]
            if m[j - 1] < h:
                k += 1
                if (mxk < k) or (mxk == k and mx < h):
                    mxk = k
                    mx = h
            else:
                break
print(mxk, mx)
