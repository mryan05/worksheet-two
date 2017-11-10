s = input()
new = ""
for i in range (len(s)):
    if i % 3 != 0:
        new = new + s[i]
print(new)