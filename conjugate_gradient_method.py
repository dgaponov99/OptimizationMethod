import functions
from grad_methods import *


def minimization(fun, x0, e):
    f = fun.f
    grad_f = fun.grad_f
    d_k = grad_f(x0[0], x0[1])
    x_k = x0
    x_km1 = [0, 0]
    first = True
    i = 0
    while first or abs(f(x_k[0], x_k[1]) - f(x_km1[0], x_km1[1])) > e:
        first = False
        i += 1
        x_km1 = x_k
        lamb = min_lamb(0, x_k, d_k, f)['x'][0]
        x_k = x_kpp(lamb, x_k, d_k)
        if i % 2 == 0:
            d_k = grad_f(x_k[0], x_k[1])
        else:
            betta = norma_sqr(grad_f(x_k[0], x_k[1])) / norma_sqr(grad_f(x_km1[0], x_km1[1]))
            grad = grad_f(x_k[0], x_k[1])
            d_k = [
                grad[0] - betta * d_k[0],
                grad[1] - betta * d_k[1]
            ]
    print(f.__doc__, ':')
    print('x0 =', x0)
    print(i, 'iteration')
    print('answer:', f(x_k[0], x_k[1]))
    print('x_min:', x_k)


minimization(functions.f1, [0, 0], 0.0001)
print()
minimization(functions.f2, [-2, 3], 0.0001)
