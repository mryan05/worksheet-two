s = input()
a = s[0 : s.find('h')]
b = s[s.find('h') : s.rfind('h') + 1]
b = b[::-1]
c = s[s.rfind('h')+1 : len(s)]
print(a + b + c)