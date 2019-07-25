'''
#회문 판별
word = input()

b=""
word_len = len(word)

for i in range(0 , word_len , 1):
    b += word[word_len-i-1]

print(b)

if word==b:
    print("입력하신 단어는 회문(Palindrome)입니다.")
'''

'''
#가위바위보
name_man1=input()
name_man2=input()
rcp_man1=input()
rcp_man2=input()

def rcp(man1,man2):

    if (man1 == man2): return("비겼습니다!")
    elif (man1 == "가위") & (man2 == "보"): return("가위가 이겼습니다!")
    elif (man1 == "보") & (man2 == "바위"): return("보가 이겼습니다!")
    elif (man1 == "바위") & (man2 == "가위"): return("바위가 이겼습니다!")
    elif (man2 == "가위") & (man1 == "보"): return("가위가 이겼습니다!")
    elif (man2 == "보") & (man1 == "바위"): return("보가 이겼습니다!")
    elif (man2 == "바위") & (man1 == "가위"): return("바위가 이겼습니다!")


print("{0}".format(rcp(rcp_man1,rcp_man2)))
'''

'''
#소수구하기

def prime(num):

    val=0
    count=0

    while val<a:
        val = val + 1
        if (a%val)==0:
            count = count+1

    if count == 2:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")

a = int(input())

prime(a)
'''

'''
#피고나치 수열
def pigo(num):
    a=[1,1]
    if num == 1:
        print([1])
    elif num == 2:
        print(a)
    else:
        num=int(num)
        for i in range(3,num+1,1):
            b = (int(a[i-2])+int(a[i-3]))
            a.append(b)
        print(a)

n=int(input())

pigo(n)
'''

'''
#list의 중복제거
def list_set(a):
    len_list = len(a)
    b=[a[0]]
    
    for i in range(1 , len(a) , 1):
        c=0

        for j in range(0 , i , 1):
            if a[i]==a[j]:
                c=1
        
        if c!=1 :
            b=b+[a[i]]



    return(b)

list1=[1, 2, 3, 4, 3, 2, 1]
list2=list_set(list1)

print(list1)
print(list2)
'''

'''
#숫자 찾기

def find_num(list1,num1):
    
    c=0

    for i in list1:
        if i == num1:
            c=1

    if c == 1:
        print("%s => True" % num1)
    else :
        print("%s => False" % num1)

a=[2, 4, 6, 8, 10]

print(a)
find_num(a,5)
find_num(a,10)

'''

'''
def double(num1):
    a =  int(num1)**2
    return a

a = input()

b = a.split(", ")

for i in range(0,len(b),1):
    print("square({0}) => {1}".format(b[i],double(b[i])))

'''

'''
def longer_word(a,b):
    if len(a)>=len(b):
        return a
    else:
        return b

    

a = input()

b = a.split(", ")

print(longer_word(b[0],b[1]))

'''


def countdown(num1):
    if int(num1)<=0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        i = int(num1)
        while i >= 0:
            print(i)
            i -= 1

countdown(0)
countdown(10)