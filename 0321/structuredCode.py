# 구조적 코드론
# case 구조와 else - if 구조의 차이
# (실습 154) 점수를 받고 점수에 따라 등급을 출력하는 프로그램을 작성하시오
    # case
score = int(input("점수를 입력받습니다.."))
grade = (score - score % 10) / 10
print(grade)

# 문제가 있는데, 내 파이썬이 버전이 딸려서 match - case 문을 사용할 수 없다!!!
# match grade:
#     case 6:
#         print("부족")
#     case 7:
#         print("그럭 저럭")
#     case 8:
#         print("꽤 잘함")
#     case 9:
#         print("매우잘함")
#     case 10:
#         print("만점")
#     case default:
#         print("NaN")


