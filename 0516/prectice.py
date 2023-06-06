# (연습문제4) 500부터 1000 사이의 정수 중에서 소수의 개수를 출력하는 프로그램을 작성하시오
a = 500
b = 1000
p = []
for i in range(a+1,b+1,2):
    for j in range(2, i+1):
        if(i%j == 0):
            break   
    if(i == j):
        p.append(i)
print(p)
print(len(p))

# (과제 : 가위바위보)
import random
rcp = ["가위", "바위", "보"]
cc=[0,0,0]
rd = int(input("몇판 싸우쉴?"))
for i in range(rd):
    my = int(input("가위 == 1, 바위 == 2, 보 == 3"))
    if(my != 1 and my != 2 and my != 3):
        print("입력을 잘못했다 휴먼")
    c = random.randint(1, 3)
    if(c == 1):
        print("승")
        print(f"컴퓨터는 {rcp[my-2]}를 냈다, 너는 {rcp[my-1]}을 내고 이기다 게임")
        cc[0] += 1
    elif(c == 2):
        print("패")
        print(f"컴퓨터는 {rcp[my%3]}를 냈다, 너는 {rcp[my-1]}을 내고 지다 게임")
        cc[1] += 1
    else:
        print("무승부")
        print(f"컴퓨터는 {rcp[my-1]}를 냈다, 너는 {rcp[my-1]}을 내고 비기다 게임")
        cc[2] += 1
print(f"당신은 {rd}판을 싸워 {cc[0]}승 {cc[2]}무 {cc[1]}패의 쾌거를 이루었다")


# (실습문제)

n = 10; sq = []; c = 0
for i in range(1,100):
    sq.append(i)
random.shuffle(sq)
del(sq[n:])
sq.sort()
for i in range(len(sq)):
    c += sq[i]
print(f"{sq}, 누계 : {c}")


# (실습 6211) 별을 한 행에 10개 출력하는 프로시저 star()를 작성하고 실행하시오

def star():
    for i in range(10):
        print("*", end = "")
    print("")
def star_w_n(n = 10):
    for i in range(n):
        print("*", end = "")
    print("")

star()
star_w_n(30)

# (실습 6212) greet()를 조금 수정하여 인사와 함께 상대방의 이름을 출력하는 프로시저 greetName()를 작성하시오. 단, 함수를 호출할 때 이름을 인자로 전달한다ㅣ

def greetName(name):
    print(f"How are you? {name}")

greetName("yeah")

# (실습 6213) 이름을 키보드로 입력하고, 이 이름을 greetName(name)의 인자로 전달하도록 프로그램을 수2정핫오

name = input("이름입력")
def greetName(name):
    print(f"How are you? {name}")

greetName(name)

# 실습(6221) 키보드에서 입력한 두 실수 a, b으 합을 반환하는 add2(a, b) 함수를 만들고, 다음과 같이 실행되도록 프로그램을 작성하송.

def add2(a, b):
    return a+b
a = float(input("실수 입력 1"))
b = float(input("실수 입력 2"))
print(add2(a, b))

# 실습(6221 - 1) 저걸 두수의 합과 곱을 튜플로 반환하도록 만들어라

def add2(a, b):
    s = (a+b, a*b)
    return s
a = float(input("실수 입력 1"))
b = float(input("실수 입력 2"))
print(f" 합 = {add2(a, b)[0]}, 곱 = {add2(a, b)[1]}")
