"""
a = input()
b = 1
for i in range(0, len(a)):
    if a[i] != a[len(a) - i-1]:
        b = 0
        break

print(a)

if b == 1:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
"""

'''
a = list(input().split(" "))
a.reverse()
b = ""
for i in range(0, len(a)):
    b += a[i]
    if i != len(a)-1:
        b += " "
print(b)

'''
'''
url1 = input()
(protocol, ex_url1) = url1.split(":")
ex_url1 = ex_url1.lstrip('/')
(host, others) = ex_url1.split("/")

print('protocol: {0}'.format(protocol))
print('host: {0}'.format(host))
print('others: {0}'.format(others))
'''
'''
b = 0

while b == 0:
    str1 = input()
    if len(str1) == 0:
        b = 1

    str2 = str1.upper()
    print(str2)
'''

'''
str1 = input()
list1 = str1.split(" ")
set1 = set(list1)
list2 = list(set1)

# 리스트 한줄로 출력
def print_list(list1):
    for i in range(len(list1)):
        if i == len(list1) - 1:
            print(list1[i])
        else:
            print(list1[i], end=", ")

print_list(sorted(list2))
'''

str1 = input()
str2 = ""
for i in range(0, (len(str1)+1) // 2):
    str2 += str1[2 * i]

print(str2)
