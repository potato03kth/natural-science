# (실습 272-1) 리스트 ['apple', 'melon', 'berry']를 set 변수에 추가하여 출력하는 프로그램을 작성하시오.
# 입력된 kiwi가 있는지 확인하여 없으면 추가하도록 한다.
print("------")
print("(실습 272-1)")

s = set(["apple", "melon", "berry"])

if("KIwi" in s):
    print("Kiwi 는 존재")
    print(s)
else:
    s.add("Kiwi")
    print("Kiwi가 빠졌잖아")
    print(s)
print("------")

# (실습 274) 주어진 문자열을 set으로 형변환하여 각 요소의 빈도수를 딕셔너리로 저장하여 출력하는 프로그램을 작성하시오.
print("------")
print("(실습 274)")

t = "Life is too short, You need Python"
t_rep = t.replace(" ", "")

dic = {}
for i in set(t_rep):
    c = t.count(i)
    dic[i] = c

for i in dic:
    print(f"{i} : {dic.get(i)}")

print("------")