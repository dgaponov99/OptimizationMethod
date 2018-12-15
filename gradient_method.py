import functions
from grad_methods import *
import math


def minimization(fun, x0, e):
    f = fun.f
    grad_f = fun.grad_f
    x_k = x0
    first = True
    i = 0
    while first or norma_sqr(grad_f(x_k[0], x_k[1])) > e:
        first = False
        i += 1
        grad = grad_f(x_k[0], x_k[1])
        lamb = min_lamb(0, x_k, grad, f)['x'][0]
        x_k = x_kpp(lamb, x_k, grad)
    print(f.__doc__, ':')
    print('x0 =', x0)
    print(i, 'iteration')
    print('gradient:', norma_sqr(grad_f(x_k[0], x_k[1])))
    print('answer:', f(x_k[0], x_k[1]))
    print('x_min:', x_k)


minimization(functions.f1, [0, 0], 0.0001)
print()
minimization(functions.f2, [10, -10], 0.0001)
