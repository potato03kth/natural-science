# (실습 5111) 리스트x에 1부터 20까지 정수를 반복문을 이용하여 저장하고, 홀수값을 하나씩 출력
print("---")
print("실습 5111")

x = []

for i in range(1,21):
    x.append(i)
for i in range(len(x)):
    if(x[i]%2 == 1):
        print(x[i])
print("---")


# (실습 5112) 리스트 fruit에 "apple", "cherry", "banana"를 저장, fruit의 값과 요소길이를 하나씩 출력
print("---")
print("실습 5112")

x = ["apple", "cherry", "banana"]
for i in range(len(x)):
    print(x[i], end = " ")
    print(len(x[i]))
print("---")


# (실습512-1) 리스트 L에 1~15범위에서 홀수값만 저장하고, L의 값을 한 행에 출력
print("---")
print("실습 512-1")
L = range(1,15,2)
for i in L:
    print(i, end = " ")
print("")
print("---")


# (실습512-2) 리스트 L에 1~15범위에서 홀수값만 저장하고, L의 값을 한 행에 출력
print("---")
print("실습 512-2")
L = [chr(a+97) for a in range(26)]
for i in range(26):
    if (ord(L[i])%2 == 1):
        print(L[i], end = " ")
        print(i + 97)
print("---")


# (실습 513) 한 행에 10개의 별을 10개의 행에 출력하는 프로그램 작성
print("---")
print("실습 513")
for i in range(10):
    for j in range(11):
        print("*", end = "")
    print("")
print("---")

# 실습 513 응용1
for i in range(10):
    for j in range(i+1):
        print("*", end = "")
    print("")

# 실습 513 응용2
k = 9
for i in range(-k, 0):
    for j in range( -i ):
        print("*", end = "")
    print("")


# 실습문제 514
print("---")

n = input("입력 정수")
for i in range(1,10):
    k = int(n)*int(i)
    print(f"{n} * {i} = {k}")

print("---")


# (실습 514-1) 구구단중 입력받은 정수로 구성된 단을 출력하는 프로그램을 for문을 사용하여 작성히소. 출력문을 사용하여 아래와 같이 3열로 출력하시오
print("---")
print("실습 514-1")

n = input("정수를 입력하라")
for i in range(3):
    for j in range(3):
        order = (i*3+j+1)
        c = int(n) * order
        print(f"{n} * {order} = {c}", end = "\t")
    print("")

print("---")


# 실습문제515-1 - 라인수를 결정하여 별을 출력하는 경우
n = 6
star = 1
blank = n-star

for i in range(n):
    for a in range(n-i):
        print(" ", end = "")
    for b in range(i):
        print("**", end = "")
    print("*", end = "")
    print("")


# 실습문제515-2 - 별의 개수로 실행을 결정하는 경우
star = int(input("별 개 수 입 력, 홀수만 받습니다"))
n = int((star+1)/2)
for i in range(n):
    for a in range(n-i):
        print(" ", end = "")
    for b in range(i):
        print("**", end = "")
    print("*", end = "")
    print("")

