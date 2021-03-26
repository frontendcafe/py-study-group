def ensure_question(s):
    if s == '' or s[-1] is not '?':
        return s + '?'
    else:
        return s

print(ensure_question(''))
print(ensure_question('asd'))
print(ensure_question('dsa?'))