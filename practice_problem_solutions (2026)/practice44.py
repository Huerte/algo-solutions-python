# Length of Last Word

def get_length(s):
    return len(s.split()[-1])
    
print(get_length('Hello World'))
print(get_length('     fly me   to    the    mooon   '))
