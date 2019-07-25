# cording : utf-8 
# 01_11_01

'''
print("이 계산기는 2개의 수를 이용한 사칙연산을 지원합니다.")

a, oper, b= 0,"",0

a=float(input("첫 번째 숫자를 입력하시오!:"))
oper=(input("연산자자를 입력하시오!(+, -, *, /):"))
b=float(input("두 번째 숫자를 입력하시오!:"))

ans=0

if oper == "+":
    ans=a+b
    print("%0.2f %s %0.2f = %0.2f"% (a,oper,b,ans))
elif oper == "-":
    ans=a-b
    print("%0.2f %s %0.2f = %0.2f"% (a,oper,b,ans))
elif oper == "*":
    ans=a*b
    print("%0.2f %s %0.2f = %0.2f"% (a,oper,b,ans))
elif oper == "/":
    ans=a/b
    print("%0.2f %s %0.2f = %0.2f"% (a,oper,b,ans))
else:
    print("'%s'는 지원하지 않는 연산자입니다." % oper)
'''

'''
#약수구하기, 소수구하기
a = int(input())

val=0
count=0

while val<a:
    val = val + 1
    if (a%val)==0:
        print("%d(은)는 %d의 약수입니다." % (val,a))
        count = count+1

if count == 2:
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." % (a,a))

'''

'''
# 대소문자 구별
char=input()

if ord("a")<=ord(char)<=ord("z"):
	print("%s 는 소문자 입니다." % char)
elif ord("A")<=ord(char)<=ord("Z"):
	print("%s 는 대문자 입니다." % char)
else:
	print("%s 는 알파벳이 아닙니다." % char)

'''

'''
#가위바위보
man1=input()
man2=input()

if (man1 == man2): print("Result : Draw")
elif (man1 == "가위") & (man2 == "보"): print("Result : Man1 Win!")
elif (man1 == "보") & (man2 == "바위"): print("Result : Man1 Win!")
elif (man1 == "바위") & (man2 == "가위"): print("Result : Man1 Win!")
elif (man2 == "가위") & (man1 == "보"): print("Result : Man2 Win!")
elif (man2 == "보") & (man1 == "바위"): print("Result : Man2 Win!")
elif (man2 == "바위") & (man1 == "가위"): print("Result : Man2 Win!")

'''
'''
#알파벳 변환

char=input()

if ord("a")<=ord(char)<=ord("z"):
	print("%s(ASCII: %d) => %c(ASCII: %d)" % (char, ord(char),ord(char)-32,ord(char)-32)  )
elif ord("A")<=ord(char)<=ord("Z"):
	print("%s(ASCII: %d) => %c(ASCII: %d)" % (char, ord(char),ord(char)+32,ord(char)+32)  )
else:
	print("%s" % char)

'''
'''
#배수구하기


val=0
while val<200: val = val + 1
    if ((val%7)==0)&((val%5)!=0):
        if val==7: print(val,end="")
        else: print(",",end=""); print(val,end="")
'''

#자리수가 모두 짝수인 수

count=0
val=99

while val<300:
    val = val + 1
    if (((val//100)%2==0)&((val//10)%2==0))&((val//1)%2==0) :
        if count==0: 
            print(val,end="");count=count+1
        else: 
            print(",",end=""); print(val,end="")
