'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

'''

def max_vowles(s,k):
    v = 0
    max_vowles = 0
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for i in range(0,k):
        c = s[i]
        if c in vowels:
            v+=1
    
    max_vowles = v

    for i in range(k, len(s)):
        c = s[i]
        if s[i-k] in vowels:
            v-=1
        if s[i] in vowels:
            v+=1
        max_vowles = max(max_vowles, v)
    
    return max_vowles

print(max_vowles(s = "abciiidef", k = 3))