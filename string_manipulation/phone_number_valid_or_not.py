# Phone Number Valid or not
# 1. It should start with country code(optional) proceded by a + sign.
# 2. It should be followed by 10 digits

import re
num = "+91 7530045523"
pattern = r"^\+[\d]*\s[\d]{10}$"
isValid = re.match(pattern, num)
if isValid:
    print("valid")
else:
    print("not valid")