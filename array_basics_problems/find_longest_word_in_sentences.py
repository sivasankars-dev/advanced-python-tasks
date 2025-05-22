# Find the Longest Word in a Sentence
# Input: "I love artificial intelligence"
# Output: "intelligence"

# Psudo code:
# 1. convert that string to array
# 2. declare count and result variable and assign 0 to count, empty string to result.
# 3. iterate upto that array length
# 4. find length of each iterable string count 
# 5. if that iterable count is higher than or equalto previous count we have to reassigned to count
#    assigned that string to result
# 6. else ignore it
# 7. return result

def findLongestStr(strWord):
    arr = strWord.split()
    cnt = 0
    result = ""
    for val in arr:
        if cnt <= len(val):
            cnt = len(val)
            result = val
    return result

print(findLongestStr("I love artificial intelligence"))         # → "intelligence"
print(findLongestStr("AI is fun"))                              # → "fun"
print(findLongestStr("Hello"))                                  # → "Hello"
print(findLongestStr(""))                                       # → ""
print(findLongestStr("A aa aaa aaaa aaaaa"))                    # → "aaaaa"
print(findLongestStr("Same size word test"))                    # → "Same" or similar-length word
print(findLongestStr("Wow, this is awesome!"))                  # → "awesome"
print(findLongestStr("Up-to-date AI models work well"))         # → "Up-to-date"
print(findLongestStr("Newlines\nand\ttabs work"))               # → "Newlines"
print(findLongestStr("supercalifragilisticexpialidocious"))     # → "supercalifragilisticexpialidocious"
print(findLongestStr("Test123 case456"))                        # → "Test123"
print(findLongestStr("multiple   spaces"))                      # → "multiple"
print(findLongestStr("dog cat hat"))                            # → "dog" (or whichever appears first with same max length)


