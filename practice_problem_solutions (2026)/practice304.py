# CodeWars - Strip Comments

def strip_comments(strng, markers):
    arr = [s for s in strng.split('\n')]
    
    for i in range(len(arr)):
        temp = []
        for mark in markers:
            ind = arr[i].find(mark)
            if ind >= 0:
                temp.append(ind)
        if temp:
            arr[i] = arr[i][:min(temp)].rstrip()
    
    return '\n'.join(arr)

print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) # "apples, pears\ngrapes\nbananas")
print(strip_comments("   a #b\nc\nd $e f g", ["#", "$"]))                                 # "   a\nc\nd")
print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]))                                    # "a\nc\nd")