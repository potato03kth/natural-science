# 시퀸스 자료형들에 대해 알아보자.

a_string = "goodbye, world"
b_list = [1,2,3,4,5,6,7,8]
c_tuple = (1,2,3,4,5)

print(a_string)
print(b_list)
print(c_tuple)
print("--------")

print(a_string[0], a_string[-1])
print(b_list[0], b_list[-1])
print(c_tuple[0], c_tuple[-1])


for i in range(0, len(a_string)):
    print(a_string[i], end=" ")
print()

if (~("1" in a_string)):
    a_string = a_string + "11"
print(a_string)