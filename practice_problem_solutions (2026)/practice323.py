# Word Ladder

from collections import deque

def word_ladder(start, end, word_list):
    words = set(word_list)

    if end not in words:
        return
    
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        
        word, paths = queue.popleft()

        for i in range(len(word)):
            for c in [chr(i) for i in range(97, 123)]:
                cur = word[:i] + c + word[i+1:]

                if cur == end:
                    return paths + [cur]
                
                if cur in words and cur not in visited:
                    visited.add((cur))
                    queue.append((cur, paths + [cur]))

    print(0)


n = int(input('Enter word array length: '))
print('Enter the word list:')
words = [input().strip() for _ in range(n)]

start = input('Enter start word: ')
end = input('Enter end word: ')

print(word_ladder(start, end, [start] + words))