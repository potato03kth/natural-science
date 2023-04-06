import math

# (실습 242) 리스트 변수에 1,2,3,4,5를 저장하고, 처음과 마지막 원소를 출력하는 프로그램을 작성하시오.
a = [1,2,3,4,5]

a_ini = a[0]
a_fin = a[-1]

print("실습(242)")
print(a_ini)
print(a_fin)
print("---------")


# (실습 242-1) 리스트 변수에 5개의 값을 저장하여 뒤의 3개만 출력되도록 하시오.
a = [1,3,5,7,9]
print("실습(242-1)")
print(a[-3:])
print("---------")


# (실습 242-2) 문자열 변수에 "I live in korea" 값을 저장하고 단어로 된 리스트와 각각 문자로 된 리스트를 만들어서 출력되도록 하시오.
print("실습(242-2)")
str_a = "I live in korea"

j = 0
k = []
print(str_a.split())

# for i in range(0, len(str_a)):
#     if((str_a[i] == " ")):
#         k.append(str_a[j:i])
#         j = i
#     elif(str_a[i] == str_a[-1]):
#         k.append(str_a[j:i+1])
#         j = i
for i in range(0, len(str_a)):
    k.append(str_a[i])
print(k)

# remove the blank
k2 = []
for i in range(0, len(str_a)):
    if (str_a[i] != " "):
        k2.append(str_a[i])

print(k2)

# print(a)


print("---------")

# (실습 242-3) 리스트 변수에 1,2,3,4,5를 저장하고, 3번쨰와 5번쨰 원소에 임의로 원소를 추가하고 짝수번째 요소들만 합계를 출력하는 알고리즘과 프로그램을 작성하시오.
print("실습(242-3)")

a = [1,2,3,4,5]
a.insert(2, 6)
a.insert(4, 2)
b = a[::2]
print(b)
k = 0
for i in range(0, len(b)):
    k += b[i] 
print(k)

print("---------")

# (실습 242-4) 리스트 변수에 5개의 값을 저장하고, 3개의 값을 가진 리스트를 추가하고 추가된 값만 출력되도록 하십시오.
print("실습(242-4)")

a = [1,6,4,2,7]
a.append([1,11,111])
for i in range(0,len(a)):
    if str(type(a[i])) == "<class 'list'>":
        print(a[i])
        break

print("---------")

# (실습 243-1) 리스트 ['b', 'a', 't', 'g']를 변수에 저장하고, 사용자가 입력한 임의의 문자를 추가한 후 정렬하여 출력하는 프로그램을 작성하시오.
print("실습(243-1)")

a = ['b', 'a', 't', 'g']
a.append(input("임의 문자 하나"))
print(a)
b = sorted(a)
print(b)
print("---------")

# (실습 243-2) 5개의 영문단어를 사용자가 입력하여 리스트에 추가한 후 출력하는 프로그램을 작성하고 내림차순으로 정렬하시오.
print("실습(243 -2)")

a = input("임의 길이 5 문자열, 변환한다 내가 알아서")
k = []
for i in range(0, len(a)):
    k.append(a[i])
print(k)
b = sorted(a)
print(b)
print("---------")