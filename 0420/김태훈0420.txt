# (실습 411) 임의의 두 문자열을 입력하여 첫 번쨰 문자열의 알파벳 순서가 빠르면 True, 그렇지 않으면 False를 출력하는 프로그램 작성
print("실습 411")

a = input("영어 문자 하나 입력")
b = input("하나 더 입력")

if(a[0] < b[0]):
    print("True")
else:
    print("False")

print("---")


# (실습 412) 리스트 [0], 집합{0}, 정수 -1, 실수 0.01의 참, 거짓을 판단하는 프로그램을 작성
print("실습 412")

a = [0]
b = {0}
c = -1
d = 0.01

if(a):
    print("True")
else:
    print("False")

if(b):
    print("True")
else:
    print("False")

if(c):
    print("True")
else:
    print("False")

if(d):
    print("True")
else:
    print("False")

print("---")


# (실습413) 입력한 수가 짝수이면서 5의 배수인가?
print("실습 413")

n = int(input("숫자 입력하라우"))
if((n%2 == 0) and (n%5 == 0)):
    print(f"와! 니가 입력한 {n}은 짝수이며 5의 배수이다!")
else:
    print("병신! 넌 짝수이며 5의 배수인 수를 입력하지 못했다! 이 무기력한놈")

print("---")

# (실습 413 추가문제) 2의 배수이고 5의배수인 수중 3의 배수 리스트로 출력

print("실습 413 추가문제")

k = []
q = []

for i in range(1000):
    if((i%2 == 0) and (i%5 == 0) and i != 0):
        k.append(i)

for i in range(len(k)):
    if(k[i]%3 == 0):
        q.append(k[i])

print(k)
print(q)


print("---")

# (실습 422) 어떤 학생의 용돈이 10만원인데 성적이 80점 이상이면 15만원을 준다고 한다. 이를 프로그램하라
print("실습 422")

point = int(input("점 수 입 력 솔 직 하 게"))
n = 0
if(point>=80 and point<=100):
    n = 150000
elif(point>100):
    n = 0
    print("뭐하냐? 니 점수는 토익점수냐?")
    print("그짓부렁을 꺼내면 용돈이 없어진단다")
else:
    n = 100000
print(f"니 용돈{n}원")

print("---")


# 둘 중 큰 수 출 력
print("실습 4131")
a = input("a int 입력")
b = input("b int 입력")

if(a>b):
    print(a)
elif(a<b):
    print(b)
else:
    print("용호상박 자강두천")

print("---")


# (실습 4233) 어떤 사람이 마트에서 물건을 구입하였다, 구입 통액이 9만 이상이면 물건값은 5프로 할인, 아니면 2프로 할인이다
print("실습 4233")

dc = 0
a = int(input("구입금액 입력"))

if(a>=50000 and 90000 > a):
    dc = 3
elif(a>=90000):
    dc = 5
else:
    dc = 2
a = a*(1-dc*0.01)
print(f"당신은 {dc}%를 할인받아 {a}를 받습니다")


print("---")


# (실습 4233-2) 학번을 입력받았다, 5번쨰 값이 학과코드이면 판별하여 1:공대, 2:인문대, 3:예술대, 4:경영대를 출력하는 프로그램 작성(match-case)사용
print("실습 4233-2")

a = input("학번입력")
a = int(a[4])
# 놀랍게도 나의 Python이 3.10 버전이 아니라 match-case 구문 기능이 없다.
# 그런 고로 대신 딕셔너리로 주먹구구 구연해내었다

if(a == 1):
    print("공대")
elif(a == 2):
    print("인문대")
elif(a == 3):
    print("예술대")
elif(a == 4):
    print("경영대")
else:
    print("그런 대는 없다")
# match a:
#     case    
print("---")


# (실습 4241) 어느 박물관의 입장료는 나이에 따라 다음 표와 같이 달라진다고 가정하자.
# 나이를 키보드에서 입력한다고 가저하고, 나이에 따른 입장료를 출력하는 프로그램을 작성하시오.
print("실습 4241")

a = int(input("나이 입력"))

if(a<=7):
    fee = 0
elif(a<=19):
    fee = 300
elif(a<=64):
    fee = 500
elif(a>=65):
    fee = 0
print(f"입장료는 {fee}이다 이 {a}살 인간아")
print("---")


# (실습 4242) 학점을 입력하면 A,B,C,D 등급을 판정하는 프로그램을 작성하라.
print("실습 4242")

a = float(input("학점입력"))
level ="A"
if(a<2.0):
    level = "D"
elif(a<3.0):
    level = "C"
elif(a<4.0):
    level = "B"
elif(a>=4.0):
    level = "A"
print(f"학점 {a}은 {level}다")


print("---")


# 실습문제 청소년 확인

day = input("생년(YYYY)")
if(len(day) != 4):
    print("눈 똑바로 뜨고 제대로 입력해라")
else:
    age = 2023 - int(day)
    if(age >= 15 and age < 20):
        print("애새끼")
    else:
        print("슈퍼 세금내는자 클럽에 오신걸 환영합니다")


# 주머니에 돈이 있으면 가만히 있고 없으면 카드를 꺼내라
a = ["paper", "cellphone", "money"]
if ("money" in a):
    pass
else:
    print("아 이게 돈이 없네 카드 on")


# 논리적인 오류 판별
number = input("주민등록번호(yymmdd - n)")
ismale = number[7]

if ismale in ("1", "3"):
    print("남자")
elif ismale in ("2", "4"):
    print("여자")
else:
    print("병신")



# 실습문제 - 주차료 계산
t = int(input("주차시간(min)"))
is_light = int(input("경차임 ? (1/0)"))
fee = 0

if(t<=10):
    fee = 0
else:
    fee = 500
    t = t - 30
    if(t>0):
        fee = fee + int(t/10) *200
    t = t + 30

if(is_light):
    fee = fee/2
fee = format(fee, ",")
t = format(t, ",")
# print(format(num, ','))
print(f"you parking here in {t}minutes")
print(f"your parking fee is {fee}won")
