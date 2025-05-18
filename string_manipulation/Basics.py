import re
# Reverse a string
text = "siva"
res = text[::-1]
print("Reverse String: ", res)

# Check if a string is palindrome or not
input1 = "madam"
input2 = "hello"
input3 = "malayalam"
 
def checkIsPrime(inp):
    first = 0
    last = len(inp)-1

    for i in range(len(inp)):
        if inp[first] == inp[last]:
            first += 1
            last -= 1
            continue
        else:
            return False

    return True

print("Prime" if checkIsPrime(input1) else "Not Prime")
print("Prime" if checkIsPrime(input2) else "Not Prime")
print("Prime" if checkIsPrime(input3) else "Not Prime")

# Count vowels and consonants
user_input = "chatgpt"
res = {}
vowel_inputs = ['a','e','i','o','u']
def checkVowels(vowl):
    for value in vowl:
        if value in vowel_inputs:
            res['vowel'] = res.get('vowel', 0) + 1
        else: 
            res['consonants'] = res.get('consonants', 0) + 1

    return res

print(checkVowels(user_input))

# Remove duplicates
# Step1
rem_dup = "programming"
# res = ""
# for i in rem_dup:
#     if i not in res:
#         res += i
# Step2
res = "".join(dict.fromkeys(rem_dup))
print("Removed duplicate keys: ", res)

# Find the Most Frequent Characters
words = "mississippi"
freq_dic = {}
for word in words:
    freq_dic[word] = freq_dic.get(word, 0) + 1

freq_char = max(freq_dic, key=freq_dic.get)
print(freq_char)

# Capitalize first word of each letter
low_chr = "hello world"
first_word_capital = low_chr.title()
print("First word Capital ",first_word_capital)

# Replace with hyphens
with_space = "I love coding"
rep_hyp = with_space.replace(" ", "-")
print("Replaced Hyphens ",rep_hyp)

# Remove All non-alphabetic characters
alpha_chr = "he!!o@123"
rem_alpha_chr = re.sub(r"[^a-zA-Z]", '',alpha_chr)
print("Removed non-alphabetic characters ",rem_alpha_chr)

# Find longest word in the sentences
long_sent = "I love artificial intelligence"
split_sent = long_sent.split()
long_word = ""
for word in split_sent:
    if len(long_word) < len(word):
        long_word = word

print("Longest Word", long_word)

# Find all duplicate word










