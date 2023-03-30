import math
from datetime import datetime

# ? triple single quetation??
# ! 이게 뭐노 시발

a = """
what 
the
fuck is that 
"""

print(a)
d = datetime.today()
a = "오늘은 %s 입니다." %d
print(a)

a = 1426
b = 553

print("----------")
print("%10d" %a)
print("x %8d" %b)
print("----------")
print("%10d" %(a * b))
print("\n" * 2)


print("----------")
print("{:>10,}".format(a))
print("x {:>8,}" .format(b))
print("----------")
print("{:>10,}" .format(a * b))
