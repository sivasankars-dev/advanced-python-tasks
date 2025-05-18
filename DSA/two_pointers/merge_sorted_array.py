a = [1,3,5]
b = [2,4,6]

res = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

res += a[i:]
res += b[j:]

print(res)