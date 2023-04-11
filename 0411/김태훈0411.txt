# (실습 252) 튜플 변수에서 마지막 원소를 제외하고 출력하시오.
print("-----")
print("실습 252")

tp_1 = (1,2,3,"a","b","c")
tp_2 = (1,4,(1,2,3,4),5)
print(tp_2[2])

print(tp_1[:-1])
print("-----")

# (실습 253) 문자열을 입력받아서 각 문자로 된 튜플로 변환하여 출력하시오.
print("-----")
print("실습 253")

a = input("여기에 문자열 입력.")

def string_to_tuple(s):
    return tuple(s)

t = string_to_tuple(a)
print(t)

print("-----")


# (실습 261) 딕셔너리 변수에서 적절한 값을 저장하여 다음과 같이 출력되도록 하시오.

print("-----")
print("실습 261")

dt = { 1:"HGD", 2:"LSS", 3:"KMS"}
print(dt)

print("-----")

# (실습 262) 위의 딕셔너리 변수에서 첫 번째와 마지막 원소의 값을 출력하는 프로그램을 작성하시오.
print("-----")
print("실습 262")

dt = { 1:"HGD", 2:"LSS", 3:"KMS"}
a = []

for i in dt.keys():
    a.append(dt[i])
print(a[0], end = " ")
print(a[-1])
    

print("-----")

# (실습 263) 위의 (실습 261)의 딕셔너리 변수에서 모든 키와 값을 리스트로 출력하는 프로그램을 작성하시오.
print("-----")
print("실습 263")

a_key = []
a_value = []

for i in dt.keys():
    a_key.append(i)
    a_value.append(dt[i]) 
print(a_key, end = "\n"); print(a_value)

print("-----")

# (실습 264-1) 정수를 입력받고 딕셔너리 키값으로 구성하고자 한다. \n 
# 입력받은 정수까지로 된 key, value는 키값의 제곱값이 되도록 구성하여 출력하라.
# (실습 264-2) 5번의 정수를 입력받고 딕셔너리 키값으로 구성한다. \n
# 입력받은 정수가 key, 키값의 제곱값이 value가 되도록 구성하여 출력
print("-----")
print("실습 264")

d = {}
n = input("여기에 정수 입력")
for i in range(0,int(n)):
    d[i] = i ** 2
print(d)

d = {}
n = []
for i in range(0,5):
    if(i != 4):
        n.append(int(input(f"여기에 정수를 {5-i} 번 입력")))
    else:
        n.append(int(input("마지막 정수 입력")))
# print(n)
for i in range(0, len(n)):
    d[n[i]] = n[i] ** 2
print(d)

print("-----")


# (실습 265) 문자열의 문자 빈도수를 계산하고자 한다. 딕셔너리 키값으로 문자를value로 개수를 구성하고자 한다. 공백제거 문자 총 갯수
print("-----")
print("실습 252")

str = "Life is too short, You need Python"
dt = {}

# * initial regist on dt 
for i in range(0, len(str)):
    dt[str[i]] = 0

# * count number if it in dt 
for i in range(0, len(str)):
    if(str[i] in dt.keys()):
        dt[str[i]] = dt.get(str[i]) + 1
print(dt)


k = 0
for i in dt.keys():
    k += dt.get(i)
k = k - dt.get(" ")
print(k)





print("-----")








