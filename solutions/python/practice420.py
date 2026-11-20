# Problem: Remove the parentheses
# Source: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8
# Note: 
# Status: IN PROGRESS

def remove_parentheses(st):
    result = ""
    depth = 0
    for char in st:
        depth += char == "("
        if not depth:
            result += char
        depth -= char == ")"
    return result


char = "example(unwanted thing)example"
print(remove_parentheses(char))

assert remove_parentheses("example(unwanted thing)example") == "exampleexample"
assert remove_parentheses("example (unwanted thing) example") == "example  example"
assert remove_parentheses("a (bc d)e") == "a e"
assert remove_parentheses("a(b(c))") == "a"
assert remove_parentheses("hello example (words(more words) here) something") == "hello example  something"
assert remove_parentheses("(first group) (second group) (third group)") == "  "
assert remove_parentheses("a)b") == "ab"
assert remove_parentheses("hello ) world") == "hello  world"
assert remove_parentheses(")test(") == "test"