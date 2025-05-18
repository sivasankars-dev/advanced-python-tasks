inp = "siva"

# Step1
print(inp[::-1])

# Step2
print("".join(list(reversed(inp))))

# Step3
res = []
for key, val in enumerate(inp):
    res.append(inp[len(inp)-key-1])

print("".join(res))