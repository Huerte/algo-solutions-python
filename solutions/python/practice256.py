# Problem: Word Ladder
# Source: https://leetcode.com/problems/word-ladder/
# Note: Implement BFS for shortest transformation sequence using deque
# Status: ✅ Done

from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet: 
        return 0
    queue = deque([(beginWord, 1)])
    wordSet.discard(beginWord)

    # BFS
    while queue: 
        word, steps = queue.popleft()
        if word == endWord: 
            return steps
        for i in range(len(word)): 
            for character in "abcdefghijklmnopqrstuvwxyz": 
                if character == word[i]: 
                    continue
                newWord = word[:i] + character + word[i+1:]
                if newWord in wordSet: 
                    wordSet.remove(newWord)
                    queue.append((newWord, steps + 1))
    return 0

# Example
dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder("hit", "cog", dictionary))  # 5
