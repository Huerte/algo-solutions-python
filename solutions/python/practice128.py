# Problem: Length of Last Word
# Source: https://leetcode.com/problems/length-of-last-word/

def get_length(s):
    """Return the length of the last whitespace-separated word."""
    return len(s.split()[-1])
    
print(get_length('Hello World'))
print(get_length('     fly me   to    the    mooon   '))
