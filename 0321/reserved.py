import keyword
kword = ''
i = 0
for kword in keyword.kwlist :
    print(f"{kword:8}",end=" ")
    if i % 7 == 0:
        print()
    i = i + 1

#여러개의 변수 선언

a, b = 1,5
print(a, int(*a), b, int(*b))
print(b,a)
a, b = b, a
print(b, a)
# 놀랍게도 파이썬에서 두 변수를 swapping 할떄 이렇게만 해도 된다
# 뭐 뭐지 포인터 어떻게 쓰는 거였더라
