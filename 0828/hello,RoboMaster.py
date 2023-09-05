'''
본 코드에는 한글로 작성된 주석이 다수 등장합니다.
프로젝트의 취지와, 향후 재사용 될 상황을 고려한 판단이니, 부디 양해부탁드리며,
지금 이 코드가 제대로된 python distribution 및 SDK 위에서 작성되지 않았기 때문에, 어떠한 순간에서든 한글 주석 및 한글 변수들이 占쏙옙 들로 바뀔 수 있다는점 양해부탁드립니다.

in this codes, you will see the many of comments that writed with korean(hangul) to make the code easier to read and understand
bytheway, because of the IDE and excute invirenment, this codes can easily crack(good luck to UTF-8)
if you find the cracked code, dont panic, keep calm and carry on.
'''

'''
사실 좀 바빠서 만질 기회도 별로 없었지만, 파이썬을 써볼 수 있을거라고 기대했던 나에게 앱 내에 구현된 엉성한 파이썬 IDE는 굉장한 실망포인트였음
난 당연히 SDK가 깔려있거나, 파이썬 코드를 불러올 수 있을 줄 알았지. 그런데 짜잔! 그냥 스크래치를 CLI로 구현해놓은 거였습니다!
하고 할 수 있는게 아무것도 없다는걸 깨닫고 무기력한 며칠을 보내다가, 여기 작동하는 python이 꽤나 멀쩡한 놈이란걸 깨달은게 오늘 새벽 7시였음
그래서 이 코드나 몇몇개 코드로 상상하던걸 구현할 수 있을지 각을 볼 예정.
'''

'''
만지는중...
working on progress...
'''

# 파이썬 내부 패키지가 성공적으로 import 됨
import math as m 
import random as rd

# 하지만 파이썬 외부 패키지는 불러올 수 없음
import numpy as np

# 파이썬의 문법 또한 정상적으로 작동함! 굉장히 긍정적인 소식임!!!!!!!!!!
for i in range(10):
    print(f"you {i}diot")

# 몇 가지 로보마스터 s1과 상호작용 하기 위해 적용된 instance, enum 등을 활용해보겠음


def GetRandomValue() :
    randomYaw = rd.randrange(1,10) # 정수 1~10 범위의 난수를 생성하여 선언한 변수에 할당함
    randomYaw = randomYaw * 20
    return randomYaw

def Halt(i):
    # HALT in i seconds
    return

def SetGimbalYawValue(yaw):
    #모가지 각도를 yaw로 설정하는 내용
    gimbal_ctrl.yaw_ctrl(yaw)
    return

def main():

    for i in range(10):
        Halt(1)
        모가지각도 = GetRandomValue()
        SetGimbalYawValue(모가지각도)
        print(f"현재까지 {i+1}초 기다렸으며, 현재의 모가지 각도는 {모가지각도}입니다")
        SetGimbalYawValue(DEFAULT)

        return

main()

