def merge_the_tools(string, k):
    # your code goes here
    a = round(len(string) / k)
    b = [string[i:i + k] for i in range(0, len(string), k)]
    for i in b:
        c = []
        d = list(i)
        [c.append(i) for i in d if i not in c]
        for i in c:
            print(i, end='')
        print(end='\n')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)