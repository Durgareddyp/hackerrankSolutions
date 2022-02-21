shoes, sizeList, coust = int(input()), input(), int(input())
sizeList = sizeList.split(" ")
b = []
d = {}
for i in range(coust):
    a = input()
    c = a.split(' ')
    if c[0] in sizeList:
        b.append(c)
        sizeList.remove(c[0])
for key, value in b:
    d.setdefault(key, []).append(value)
sum = 0
for i in d.values():
    for j in i:
        j = int(j)
        sum += j
print(sum)
