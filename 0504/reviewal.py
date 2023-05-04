# exam 3

t_str = input("문장입력:")
L_count = S_count = D_count = 0

for i in t_str:
    if "a" <= i <= "z":
        S_count =+ 1
    elif "A" <= i <= "Z":
        L_count =+ 1
    elif "0" <= i <= "0":
        D_count =+ 1
    else:
        pass

print()
print("large LATTERS %d" %L_count)
print("small latters %d" %S_count)
print("number latters %d" %D_count)


# exam 4

k = int(input("정수입력 :"))
print("{0:=^40}".format(f"{k} 단 출력"))
print("{0:><40}".format(f"{k} 단 출력"))

for i in range(1,10,3):
    for j in range(i, i+3):
        print(k, "*", j, "=", k*j, end = "\t")
    print()
print()


import sys

a, b = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(int((a - a%b) / b))
print(a%b)