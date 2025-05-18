# Remove All Non-Alphabetic Characters
# Input: "he!!o@123"
# Output: "heo"
import re

inp = "he!!o@123"
# With Regex
res = re.findall(r'[a-z]+', inp)
print("".join(res))

# Without Regex
withOutReg = []
for val in inp:
    if val.isalpha():
        withOutReg.append(val)

finRes = "".join(withOutReg)
print(finRes)

