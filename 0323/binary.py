# 여러가지 진법체계 학습하자.
# 자료형에 대해 araboja


# 그거아세요? unicode (UTF-8) 덕분에 문자형을 저장하기 위해 문자 하나당 단 2byte면 충분하답니다?

a = "a"

# ! 안됨
# print(int(a)) 
#? 왜 안되냐

b = 7

print(bin(b))
print(oct(b))
print(hex(b))
print("----------")


c = 255

print(bin(c))
print(oct(c))
print(hex(c))


# 자, 그러면 저 사기같은 bin() 없이 한번 c를 2진수로 바꿔볼까?

def base_conv(n,x):
    k = []
    while(True):
        k.insert(0, x % n)
        x = (x - x%n)/n
        print(x)
        if(x == 0):
            break
    return k

print(base_conv(2,8))

# 짜잔! 이 함수를 이용해서 x 를 n 진수로 변환할 수 있다!


# 자자, 본론으로 넘어가서, 파이썬의 자료형과 논리 자료형에 대해 아라보자

# 이 while은 실행될까?
while(1):
    if(1):
        print(True) #True
        break

# 이것 또한 실행될까?
while(388295328983):
    if(1):
        print(None) #None
        break

# ㅈㄴ 지들 맘대로 실행되실게요
while("h"):
    if("이건"):
        print(int("42"))
    break





