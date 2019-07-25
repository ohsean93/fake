'''
fruit = ['   apple    ', 'banana', '  melon']


def pop_space(a):
    a = list(a)
    b = ""
    for i in range(0, len(a)):
        if a[i] != ' ':
            b += a[i]
    return b


c = {pop_space(x): len(pop_space(x)) for x in fruit}

print(c)
'''

'''
num = range(1, int(input())+1)
dict1 = {x: x ** 2 for x in num}
print(dict1)
'''

'''
str1 = list(input())
letters = 0
digits = 0

for i in str1:
    if ord("0") <= ord(i) <= ord("9"):
        digits += 1
    elif ord("a") <= ord(i) <= ord("z"):
        letters += 1
    elif ord("A") <= ord(i) <= ord("Z"):
        letters += 1

print("LETTERS {0}".format(letters))
print("DIGITS {0}".format(digits))
'''
'''
beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}

beer_after = {item[0] : item[1] * 1.05 for item in beer.items()}

print(beer_after)
'''

str1 = list(input())
counts = {}
for i in str1:
    counts[i] = str1.count(i)

for j in counts.items():
    print("{0},{1}".format(j[0], j[1]))

