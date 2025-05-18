# Find the Email is valid or not:
# 1. It should start with alphanumeric characters
# 2. It can have dots(.) or underscores(_)
# 3. It should have contain the @ symbol
# 4. After the @ symbol it should contain the alphanumeric characters or dots(.)
# 5. It should end with a domain e.g .com, .org, .in etc

import re

email = "example.email@gmail.com"
pattern = r"^[\w][\w._]+@[\w.]+\.[a-zA-Z]{2,3}$"
isValid = re.match(pattern, email)

if isValid:
    print("Email is Valid")
else:
    print("Email is not Valid")
