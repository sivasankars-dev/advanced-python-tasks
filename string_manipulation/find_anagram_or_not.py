# word1 = "listen"
# word2 = "silent"
# word1 = "triangle"
# word2 = "integral"
# word1 = "apple"
# word2 = "papel"
# word1 = "car"
# word2 = "rat"
# word1 = "aabbcc"
# word2 = "aabbc"
# word1 = "schoolmaster"
# word2 = "theclassroom"
# word1 = "Dormitory"
# word2 = "dirtyroom"
# word1 = "abc "
# word2 = "cab"
# word1 = "123"
# word2 = "321"
# word1 = "a"
# word2 = "A"
word1 = ""
word2 = ""

def checkAnagram(w1, w2):
    
    if len(w1) != len(w2):
        return "Not a Anagram"
        
    sort1 = "".join(sorted(word1))
    sort2 = "".join(sorted(word2))
    
    if sort1 == sort2:
        return "It's a Anagram"
    else: 
        return "Not a Anagram"
        
print(checkAnagram(word1, word2))