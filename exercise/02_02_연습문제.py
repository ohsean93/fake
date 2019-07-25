"""
# 함수 지정

# 총점 구하는 함수
def all_sum(input_score):
    total = 0

    for i in input_score:
        try:
            total += float(i)
        except:
            print("점수는 숫자로 입력하세요!")

    ans = total

    return ans


# 평균 구하는 함수
def mean(input_score):
    total = 0

    for i in input_score:
        try:
            total += float(i)
        except:
            print("점수는 숫자로 입력하세요!")

    ans = total / len(input_score)

    return ans


# 문제풀이
scores = [(90, 80), (85, 75), (90, 100)]

for i in range(0, len(scores)):
    print("{0}번 학생의 총점은 {1}점이고, 평균은 {2}입니다.".format(i+1, all_sum(scores[i]), mean(scores[i])))
"""

'''
#문제 풀이
del_alpha = tuple('aeiouAEIOU')
print(del_alpha)

str_or = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')
str_del = str_or

for i in del_alpha:
    str_del = [x for x in str_del if x != i]

for j in range(len(str_del)):
    print("{0}".format(str_del[j]),end="")
'''
'''
list_total=[]

for i in range(2, 10):
    list_dan=[]
    for j in range(1, 10):
        if (i*j) % 3 != 0 and (i*j) % 7 != 0:
            list_dan.append(i*j)
    list_total.append(list_dan)

print(list_total)
'''

'''
def mean(input_score):
    total = 0

    for i in input_score:
        try:
            total += float(i)
        except:
            print("점수는 숫자로 입력하세요!")

    ans = total / len(input_score)

    return ans

a = range(5)
scores = [int(input()) for x in a]


print("입력된 값 {0}의 평균은 {1}입니다.".format(scores, mean(scores)))
'''
'''
input_num = int(input())
num = range(1, input_num+1)

div_num=[]
for i in num:
    if input_num % i == 0:
        div_num.append(i)
print(div_num)

input_num = int(input())
num = range(1, input_num+1)

div_num = [int(x) for x in num if input_num % x == 0]

print(div_num)
'''

'''
num_list = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
even_num = [int(x) for x in num_list if x % 2 == 0]
print(even_num)
'''

'''
#피보나치 수열 - 행렬이용
range_fibo = range(1,10)

def matrix_multi(matrix, num):
    if num == 1:
        return matrix
    else:
        ans_matrix = matrix
        for k in range(1, int(num)):
            mid_ans_matrix = ans_matrix
            ans_matrix = []
            for i in [0, 1]:
                low=[]
                for j in [0, 1]:
                    num = 0
                    for k in [0, 1]:
                        num += (mid_ans_matrix[i][k] * matrix[k][j])

                    low.append(num)
                ans_matrix.append(low)
    return ans_matrix

def fibo(num):
    ans = matrix_multi([[1,1], [1,0]], num)[1][0]
    return ans

fibo_list = [int(fibo(x)) for x in range_fibo]

print(fibo_list)
'''
'''
num_list = range(1, 21)
power_num = [x**2 for x in num_list if x % 3 != 0 or x % 5 != 0]

print(power_num)
'''
'''
num = input()

def all_sum(input_score):
    total = 0

    for i in input_score:
        try:
            total += int(i)
        except:
            print("숫자를 입력하세요!")

    ans = total

    return ans

print(all_sum(list(num)))
'''

'''
#사전식 배열
print(hex(ord("가")))
print(hex(ord("나")))

dicBase = (('가', '깋'), ('나', '닣'), ('다', '딯'), ('라', '맇'), ('마', '밓'), ('바', '빟'), ('사', '싷'),

           ('아', '잏'), ('자', '짛'), ('차', '칳'), ('카', '킿'), ('타', '팋'), ('파', '핗'), ('하', '힣'))

inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다',

             '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',

             '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이', '뜨겁다']
sorted_inputWord = sorted(inputWord)

OutputWord=[]
for i in range(len(dicBase)):
    dic_word = [x for x in sorted_inputWord if ord(dicBase[i][0]) <= ord(x[0]) and ord(dicBase[i][1]) >= ord(x[0])]
    OutputWord.append(dic_word)

print(OutputWord)

'''

'''
str_or = input()
ans_list = [int(x) for x in str_or.split(", ")]
ans_tuple = tuple(ans_list)

print(ans_list)
print(ans_tuple)
'''

'''
#원둘례 구하기
import math

def round_c(r):
    ans = r * 2 * math.pi
    return ans


str_or = input()
list_r = str_or.split(", ")

list_r_int = [int(x) for x in list_r]

for i in range(0, len(list_r_int)):
    if i == len(list_r_int)-1:
        a = round_c(list_r_int[i])
        print("%.2f" % a)

    else:
        a = round_c(list_r_int[i])
        print("%.2f" % a, end = ", ")

'''


'''
#행열 샐성
str_or = input()
size = str_or.split(", ")

ans_matrix = []
for i in range(int(size[0])):
    line = []
    for j in range(int(size[1])):
        line.append(i*j)
    ans_matrix.append(line)

print(ans_matrix)
'''

'''
str_or = input()
words = str_or.split(", ")
words = sorted(words)

for i in range(len(words)):
    if i == len(words)-1:
        print(words[i])
    else:
        print(words[i], end = ", ")
'''
'''
str_or = input()
num_str = str_or.split(", ")
num = [int(x) for x in num_str]

odd = []

for i in range(len(num)):
    if num[i] % 2 == 1:
        odd.append(num[i])

for i in range(len(odd)):
    if i == len(odd)-1:
        print(odd[i])
    else:
        print(odd[i], end = ", ")
        
'''

'''
# 리스트 한줄로 출력
def print_list(list1):
    for i in range(len(list1)):
        if i == len(list1) - 1:
            print(list1[i])
        else:
            print(list1[i], end=", ")
'''
'''
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
d = len(tuple1)//2
tuple2 = tuple1[0:d]
tuple3 = tuple1[d:]

print(tuple2)
print(tuple3)
'''

'''
a = [5, 6, 77, 45, 22, 12, 24]
index = range(len(a))
b = [a[x] for x in index if x != 0 and x != 5 and x != 4]
print(b)
'''


'''
#행열 샐성
size = [2,3,4]

ans_matrix = []
for i in range(int(size[0])):
    floor = []
    for j in range(int(size[1])):
        line = []
        for k in range(int(size[2])):
            line.append(0)
        floor.append(line)
    ans_matrix.append(floor)

print(ans_matrix)
'''

'''
#교집합 구하기
def cup_of_set(list1,list2):
    cup_list=[]

    for i in list1:
        cup_num = 0

        for j in list2:
            if i == j:
                cup_num = 1

        if cup_num == 1:
            cup_list.append(i)

    return cup_list

a = [1,3,6,78,35,55]
b = [12,24,35,24,88,120,155]

print(cup_of_set(a, b))
'''

#중복제거
def list_set(a):
    len_list = len(a)
    b = [a[0]]

    for i in range(1, len(a), 1):
        c = 0

        for j in range(0, i, 1):
            if a[i] == a[j]:
                c = 1
                break

        if c != 1:
            b = b + [a[i]]

    return b

a = [12,24,35,24,88,120,155,88,120,155]

b = list_set(a)

print(b)