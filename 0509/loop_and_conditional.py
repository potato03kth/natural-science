
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

