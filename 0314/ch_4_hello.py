# 주석을 다는 방법은 이렇다
# 연습용 프로그램 코딩 해보자


a = 10
b = 100

#print(add, minus, multiply, duplycate,) ; print("\n", "-----------", "\n")

if(a>b):
    print("a가 b 보다 큰디요?")
else:
    print("a가 b 보다 크진 않네유 \n 그런데,")
    if(a == b):
        print("그렇다고 a 가 b 보다 작진 않네유")
    else:
        print("a 가 b 보다 작아유")

print("-------------"); print("\n")
add = a + b
minus = a - b
multiply = a * b
duplycate = a / b
power = a ** b

# 출력문단
print("사칙연산과 그 친구들을 해볼까요")
print( a, "에", b, "를 더하면,", add, "입니다")
print( a, "에", b, "를 빼면,", minus, "입니다")
print( a, "에", b, "를 곱하면,", multiply, "입니다")
print( a, "에", b, "를 나누면,", duplycate, "입니다")
print( a, "에", b, "를 제곱하면,", "%.1e"%power, "입니다")

# 자동 형변환에 대해 알아보자.
print("파이썬은 형을 자동으로 변환한다.")

print("문자열은", print(type("문자열")), "형이다")

