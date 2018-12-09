from scipy.optimize import minimize


def x_kpp(lamb, x_k, grad):
    t = grad
    return [
        x_k[0] - lamb * t[0],
        x_k[1] - lamb * t[1]
    ]


def f_x_kpp(lamb, x_k, grad, f):
    t = x_kpp(lamb, x_k, grad)
    return f(t[0], t[1])


def min_lamb(lamb0, x_k, grad, f):
    return minimize(f_x_kpp, lamb0, args=([x_k[0], x_k[1]], grad, f))


def norma_sqr(x):
    return x[0]**2 + x[1]**2
