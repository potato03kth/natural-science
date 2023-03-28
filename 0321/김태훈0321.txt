# 오늘의 연습 문제를 풀어봅시다.

# 8. 자신의 학번과 이름, 나이를 키보드에서 입력한 후, 이를 출력하는 프로그램을 작성하시오.

student_Number = int(input("학번을 입력하시오.."))
student_Name = input("이름을 입력하시오..")
student_Birthday = input("생년을 입력하시오.. placehold(yyyy)")
y_o = 2023-int(student_Birthday) + 1

print(f"학번: {student_Number} 이름: {student_Name} 나이: {y_o}")
print("------------------------")

# 11. 현재 가진 돈의 총액을 유로로 바꾸려 한다, 금액을 입력하면 유로로 계산하는 프로그램 작성(단, 1유로 == 1399 원)

euro = input("얼마나 원하는지 말해주시오..")
won = int(euro) * 1399

print(f"{euro} 유로 = {won} 원")
print("-------------------------------------")

# 12. 1mi은 1609.34m 이다, 입력된 마일을 미터로 출력하라.

mi = int(input("마일 입력받습니다.."))
meter = mi * 1609.34 
print(f"{mi} 마일 = {meter} 미터")
print("--------------------------------------")