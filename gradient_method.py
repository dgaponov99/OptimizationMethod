from scipy.optimize import minimize
import functions


# ---------------------------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------------------------


def minimization(fun, x0, e):
    f = fun.f
    grad_f = fun.grad_f
    x_k = x0
    x_km1 = [0, 0]
    first = True
    i = 0
    while first or abs(f(x_k[0], x_k[1]) - f(x_km1[0], x_km1[1])) > e:
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


minimization(functions.f1, [0, 0], 0.000001)
print()
minimization(functions.f2, [-2, 3], 0.0001)
