l1 = float(input("lado 1:"))
l2 = float(input("lado 2:"))
l3 = float(input("lado 3:"))
if (l1 > 0 and l2 > 0 and l3 > 0):
    if ((l1 + l2 > l3) and (l2 + l3 > l1) and (l3 + l1 > l2)):
    else:
        print("não é um triângulo")
if (l1 != l2 and l1 != l3 and l2 != l3):
    print("triângulo isócelis")
else:
    if (l1 != l2 or l3 and l2 != l3):
        print("triângulo excaleno")
    else:
    if (l1 == l2 == l3): print("triângulo equilátero")
