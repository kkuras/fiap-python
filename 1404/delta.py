def delta(a, b, c):
    deltas = (b**2) - 4 * a * c
    return deltas

def x1(delta, a, b):
    xis1 = (-b + (delta ** 0.5)) / (2 * a)
    return xis1

def x2(delta, a, b):
    xis2 = (-b - (delta ** 0.5)) / (2 * a)
    return xis2

print("==menu==")

delta_a = int(input("digite o valor A: "))
delta_b = int(input("digite o valor B: "))
delta_c = int(input("digite o valor C: "))


if delta_a == 0:
    print("isso nao é equação do segundo grau")

else:
    res = delta(delta_a, delta_b, delta_c)
    print("delta é:", res)
    
    if res < 0:
        print("nao existe raiz real")

    else:
        resX1 = x1(res, delta_a, delta_b)
        resX2 = x2(res, delta_a, delta_b)

        print("X1:", resX1)
        print("X2:", resX2)