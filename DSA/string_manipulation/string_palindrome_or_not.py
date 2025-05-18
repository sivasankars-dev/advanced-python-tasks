inp = "malayalam"
# inp = "madam"

def checkPalindrom(word):
    first = 0
    last = -1
    
    for value in word:
        if word[first] == word[last]:
            first += 1
            last -= 1
            continue
        else:
            return False
            
    return True
    
    
print(checkPalindrom(inp))