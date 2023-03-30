import math
from datetime import datetime

# (실습 223-1) 임의의 문자열을 입력하여 변수에 저장한 후, 첫 번째와 마지막 문자를 제외하고 출력하는 프로그램을 작성하시오.

# * 임의의 문자열 a

a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"

# * 입력된 문자열(in_str)을 배열로 변환한 후, 배열의 n번째 값을 del 하는 함수  
def deleter(in_str, n):
    k = []
    for i in range(0, len(in_str)):
        k.append(in_str[i])
    del k[n]
    result = "" .join(a for a in k)
    return result

# * deleter를 두번 실행하여 앞 그리고 뒤 를 삭제하였다.
print(deleter(deleter(a, -1),0))

# ! 이렇게 slicing으로 과제를 해결할 수도 있다

# * 맨 앞과 맨 뒤를 제외한 범위 설정
print(a[1:-1])
# print(str(deleter(a, 0)))


# (실습 233-2) "Be ambitious, challenge yourself with dreams, it will come true." 주어진 문자열에서 "a"가 나타나는 빈도를 계산하고 문자열내의 인덱스 위치를 출력하는 프로그램을 작성하시오
# ToDo 단, index() 나 find() 함수를 이용하라

a = "Be ambitious, challenge yourself with dreams, it will come true."

print(f'\"a\"의 갯수는 {a.find("a")}')
print(f'첫번째 "a"의 위치는 {a.find("a",0)}')
print(f'두번째 "a"의 위치는 {a.find("a", a.find("a") + 1)}')
print(f'세번째 "a"의 위치는 {a.find("a", a.find("a", a.find("a") + 1)+1)}')
# * 각 .find()의 index attribute 자리에 이전 a의 index 다음 자리를 넣어줬다. 




# (실습 234) 임의의 문자열을 입력으로 받았을 때, 앞뒤 문장 공백은 제거하고, 첫 글자만 대문자로 바꿔서 출력하는 프로그램을 작성하시오. 그리고 공백의 개수를 출력하시오.

s = input("예문을 입력하라우, 입력한 예문은 잘 잘라서 대문자화할거유")
c = int(s.find(" ") )
c -= 1

print(s.strip().capitalize(), c)





# 실습문제 홍길동의 나이 계산하기


td = datetime.today()
tdYear = td.year
print(td)
print(tdYear)
name = input("키미노 나마에와?: ")
pid = input("주민등록번호 내놔라 (881120-1068234) : ")


def age_detector(pid):
    parity = pid[-7]
    if(parity == "1" or parity == "2"):
        year = "19" + pid[:2]
    elif(parity == "3" or parity == "4"):
        year = "20" + pid[:2]
    else:
        print("fuckyou")
        return 0000
    
    return int(year)
age = tdYear - age_detector(pid) + 1

# print( name"의 나이는 ", age, "세 이다.")
print(f"{name}씨의 생년은 {age_detector(pid)}이네요. \n 계산에 따르면 당신의 나이는{age} 입니다. ")