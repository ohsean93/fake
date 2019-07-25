
'''
#예제
for i in range(1,12,2):
    print("{0:^11}".format("*"*i))
'''

'''
# 합격 불합격
score=(88,30,61,55,95)

for i in range(0,5,1):
    if score[int(i)]>=60:
        print("{0}번 학생은 {1}점으로 합격입니다.".format(i+1,score[int(i)]))
    else:
        print("{0}번 학생은 {1}점으로 불합격입니다.".format(i+1,score[int(i)]))
'''

'''
#for문으로 1~100 출력
for i in range(1,101,1):
    print(i)
'''

'''
sum = 0
score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

while True:
    a = score.pop()
    if a >= 80:
        sum = sum + a
    if len(score)==0:
        break

print(sum)
'''

'''
num=input()

print("0 1 2 3 4 5 6 7 8 9")

score = [0,0,0,0,0,0,0,0,0,0]
b = len(num)
num = int(num)

for j in range(1 , b+1 , 1):
    a = num%10
    num = num//10
    for i in range(0 , 10 , 1):
        if a == i:
            score[i] += 1

for k in range(0 , 9 , 1):
	print(score[k], end=" ")

print(score[9], end="")
'''

a=int(input())
i=0
binum=0

while True:
    binum += a%2 * (10**i)
    a = a//2
    i += 1
    if a==0:
        break

print(binum)