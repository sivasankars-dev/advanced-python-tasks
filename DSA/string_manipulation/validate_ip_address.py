# Validate IP Address
# Write a regex to validate an IPv4 address
# An IPv4 address consists of four octets seperated by dots(.), where each octet is a number between 0 to 255
import re

pattern = r"^[\d]{0-255}.[\d]{0-255}.[\d]{0-255}.[\d]{0-255}"

ipaddress = "192.200.0.1"

isValid = re.match(pattern, ipaddress)

if isValid:
    print("Ip Address is valid")
else:
    print("Ip address is not valid")