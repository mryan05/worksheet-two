s = input()
words = s[s.find('h') +1 : s.rfind('h')]
new = ""
for w in words:
    if w == 'h':
        w = 'H'
        new = new + w
    elif w != 'h':
        new = new + w
a = s[0 : s.find('h') + 1]
b = s[s.rfind('h') : len(s)]
print(a + new + b)