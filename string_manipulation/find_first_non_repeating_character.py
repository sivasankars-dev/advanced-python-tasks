from collections import Counter

def first_non_reating_char(s):
    counter = Counter(s)

    for val in s:
        if counter[val] == 1:
            return val
        
    return None

print(first_non_reating_char("aabbajcc"))