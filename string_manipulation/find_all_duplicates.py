# Find All Duplicates in a String
# Input: "banana"
# Output: ['a', 'n']

# Before Optimization
inp = "banana"
dup = []
res = []
for val in inp:
    if val in dup:
        dup.append(val)
        res.append(val)
    else:
        dup.append(val)

finres = set(res)
print(list(finres))

# After Optimization
dupOpt = set()
resOpt = set()
for optVal in inp:
    if optVal in dupOpt:
        resOpt.add(optVal)
    else:
        dupOpt.add(optVal)

finOptRes = list(resOpt)
print(finOptRes)