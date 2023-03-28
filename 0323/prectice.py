# 실습문제를 함 풀어보자

# 다음과 같은 함수를 이용하여, 임의의 x 값을 입력하면 함숫값을 출력하도록 해보시오

import math

def func1(x):
    den = 6 * float(x)
    num = (1 - 3*(float(x) ** 2))**2
    return den/num

n = input("원하시는 입력값을 입력하십시오")

print(f"출력값은 {func1(n)}입니다."); print("-----------")


# 해외 출장을 위해 한화(KRW)를 달러(USD)로 환전하고자 한다. 1원
# 당 1달러 환율은 1,1896.08이고, 환전수수료는 1.45%이다. 환율 우대 85% 쿠폰
# 을 가지고 있을 때 1000달러를 환전하기 위해 한화가 얼마가 필요한가?

def ex(n,rate = 0,fee_rate = 0,is_prefere = 0,prefere_rate = 0):
    if(rate == 0):
        rate = 1896.08
    if(fee_rate == 0):
        fee_rate = 0.0145    
    if(is_prefere == 0):
        is_prefere = True
    if(prefere_rate == 0):
        prefere_rate = 0.85
    fee = float(n) * float(rate) * (float(fee_rate) * ((float(is_prefere)) * float(prefere_rate)))
    return float(n) * rate - fee

print("환전계산기에 오신걸 환영합니다! \n 현재 달러 to 원화 모드만 지원합니다.")
a = input("환율 우대를 받으십니까? 받으면 1, 아니면 0")

print("현재 표준 환율로만 계산 가능합니다.")

b = input("환전 원하는 금액을 달러로 입력해주세요")

print(f"달러 {b} 불을 환전하시려면 {ex(b,0,0,a,0)} 원이 필요합니다.\n 적용된 환율은 1 달러당 1896.08")