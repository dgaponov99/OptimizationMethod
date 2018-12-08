import numpy as np
import functions


def x_kpp(grad_f, grad2_f, x_k):
    gf_t = grad_f(x_k[0], x_k[1])
    gf2_t = grad2_f(x_k[0], x_k[1])
    x_k_matrix = np.matrix([[x_k[0]], [x_k[1]]])
    x_kp1_matrix = x_k_matrix - np.dot(np.linalg.inv(gf2_t), np.matrix([[gf_t[0]], [gf_t[1]]]))
    return [x_kp1_matrix[(0, 0)], x_kp1_matrix[(1, 0)]]


def minimization(fun, x0, e):
    f = fun.f
    grad_f = fun.grad_f
    grad2_f = fun.grad2_f
    x_k = x0
    x_km1 = [0, 0]
    first = True
    i = 0
    while first or abs(f(x_k[0], x_k[1]) - f(x_km1[0], x_km1[1])) > e:
        i += 1
        first = False
        x_km1 = x_k
        x_k = x_kpp(grad_f, grad2_f, x_k)
    print(f.__doc__, ':')
    print('x0 =', x0)
    print(i, 'iteration')
    print('answer:', f(x_k[0], x_k[1]))
    print('x_min:', x_k)


minimization(functions.f1, [20, -10], 0.000001)
print()
minimization(functions.f2, [20, 20], 0.0001)

