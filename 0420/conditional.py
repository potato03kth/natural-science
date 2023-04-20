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