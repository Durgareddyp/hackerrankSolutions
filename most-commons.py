from collections import Counter

if __name__ == '__main__':
    s = input()
    a = list(s)
    b = Counter(a)
    c = sorted(b.items())
    c.sort()
    c.sort(key=lambda x:x[1],reverse=True)
    d=[]
    for i in range(3):
        d.append(c[i])
    for i in d:
        for j in i:
            print(j,end=" ")
        print(end='\n')

