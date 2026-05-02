# HackerRank - ACM ICPC Team

def acmTeam(topic):
    n = len(topic)
    max_t = 0
    counts = 0
    
    for i in range(n):
        for j in range(i+1, n):
            
            known = sum(1 for a, b in zip(topic[i], topic[j]) if a == '1' or b == '1')
            
            if known > max_t:
                max_t = known
                counts = 1
            elif known == max_t:
                counts += 1
    return [max_t, counts]

print(acmTeam(['11101', '10101', '11001', '10111', '10000', '11010', '00010', '01010'])) # [5, 9]
print(acmTeam(['10101', '11100', '11010', '00101'])) # [5, 2]
print(acmTeam(['10101', '11110', '00010'])) # [5, 1]
  