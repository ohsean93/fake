'''
# 스코어 변환
def score(list1):
    list1=list(list1)
    list2=[]
    for i in range(len(list1)):
        if list1[i]=="A":
            list2+="4"
        elif list1[i]=="B":
            list2+="3"
        elif list1[i]=="C":
            list2+="2"
        elif list1[i]=="D":
            list2+="1"
    
    return list2

a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"

b=map(lambda x : int(x), score(list(a)))

print(sum(b))
        
'''

'''

#곱하기 예외 처리

def multi(list1):
    ans = 1
    try:
        a= True
        for k in list1:
            a = a&(k.isdigit())
        if a == False:
            raise ValueError("에러발생")

    except ValueError as ex:
        print(ex)
    else:
        for i in list1:
            ans = ans * i
        
        print(ans)
        
a_str="1, 2, '4', 3"
b = list(a_str.split(", "))

multi(b)
'''
'''
#필터링
a = range(1,11)

b = list(filter(lambda x: (x%2==0) , a))

print(b)
'''

'''
#제곱하기
a = range(1,11)

b = list(map(lambda x: (x**2) , a))

print(b)
'''

'''
#최대값 구하기
def max_num(str1):
    b = list(str1.split(", "))
    b=map(lambda x : int(x) , b)
    
    return max(b)

str_input="3, 5, 4, 1, 8, 10, 2"
print("max({0}) => {1}".format(str_input,max_num(str_input)))
'''

#딕션어리 형성

a = 'abcdef'
b = list(a)

for i in range(len(b)):
    if i==0:
        c={b[i]:i}

    else:
        c[b[i]] = i

for i in c:
    print("{0}: {1}".format(i,c[i]))


