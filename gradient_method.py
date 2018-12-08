from scipy.optimize import minimize
import math


def f1(x1, x2):
    """function 1"""
    return 100 * (x2 - x1 ** 2) ** 2 + 5 * (1 - x1) ** 2


def grad_f1(x1, x2):
    return [-400 * x1 * (x2 - x1 ** 2) - 10 * (1 - x1), 200 * (x2 - x1 ** 2)]


def f2(x1, x2):
    """function 2"""
    return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2


def grad_f2(x1, x2):
    return [
        4 * x1 * (x1 ** 2 + x2 - 11) + 2 * (x1 + x2 ** 2 - 7),
        2 * (x1 ** 2 + x2 - 11) + 4 * x2 * (x1 + x2 ** 2 - 7)
    ]


def x_kpp(lamb, x_k, grad_f):
    t = grad_f(x_k[0], x_k[1])
    return [
        x_k[0] - lamb * t[0],
        x_k[1] - lamb * t[1]
    ]


def f1_x_kpp(lamb, x_k, grad_f, f):
    t = x_kpp(lamb, x_k, grad_f)
    return f(t[0], t[1])


def min_lamb(lamb0, x_k, grad_f, f):
    return minimize(f1_x_kpp, lamb0, args=([x_k[0], x_k[1]], grad_f, f))


def norma(x_k, x_kp1):
    return math.sqrt((x_k[0] - x_kp1[0]) ** 2 + (x_k[1] - x_kp1[1]) ** 2)


# norma(x_k, x_km1) > E1 or
def minimization(f, grad_f, x0, e2):
    x_k = x0
    x_km1 = [0, 0]
    first = True
    i = 0
    while first or abs(f(x_k[0], x_k[1]) - f(x_km1[0], x_km1[1])) > e2:
        first = False
        i += 1
        x_km1 = x_k
        lamb = min_lamb(0, x_k, grad_f, f)['x'][0]
        x_k = x_kpp(lamb, x_k, grad_f)
        # print(f(x_k[0], x_k[1]))
    print(f.__doc__, ':')
    print('x0 =', x0)
    print(i, 'iteration')
    print('answer:', f(x_k[0], x_k[1]))
    print('x_min:', x_k)


minimization(f1, grad_f1, [0, 0], 0.0001)
print()
minimization(f2, grad_f2, [2, 2], 0.0001)
