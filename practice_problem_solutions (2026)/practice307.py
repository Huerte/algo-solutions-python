# CodeWars - Most frequently used words in a text

from collections import Counter
import re

def top_3_words(text):
    
    words = re.findall(r"[a-z']+", text.lower())
    
    words = [w for w in words if any(c.isalpha() for c in w)]
    
    return [word for word, _ in Counter(words).most_common(3)]

print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")) # ['e', 'ddd', 'aa']
print(top_3_words("  //wont won't won't "))                                 # ["won't", "wont"]
print(top_3_words(" ''' , e   .. "))                                        # ["e"]