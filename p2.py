a = input("")
s = {}
for i in a:
    if s.get(i):
        s[i] += 1
    else:
        s[i] = 1
print(s)
