import functions


def get_points(v_1):
    u = ((1, 0), (0, 1))
    h_2 = 0.00025 if v_1[0] == 0 else 0.05
    v_2 = [v_1[0] + h_2 * u[0][0], v_1[1] + h_2 * u[0][1]]
    h_3 = 0.00025 if v_1[1] == 0 else 0.05
    v_3 = [v_2[0] + h_3 * u[1][0], v_2[1] + h_3 * u[1][1]]
    return [v_1, v_2, v_3]


def sort_points(f, points):
    tops = [f(points[0][0], points[0][1]), f(points[1][0], points[1][1]), f(points[2][0], points[2][1])]
    sorted_tops = sorted(tops)
    sorted_points = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            if sorted_tops[i] == tops[j]:
                sorted_points[i] = points[j]
    return sorted_points


def get_mid(points):
    b = points[0]
    g = points[1]
    return [
        0.5 * (b[0] + g[0]),
        0.5 * (b[1] + g[1])
    ]


def reflection(mid, w, alpha=1):
    return [
        mid[0] + alpha * (mid[0] - w[0]),
        mid[1] + alpha * (mid[1] - w[1])
    ]


def expansion(mid, x_r, gamma=2):
    return [
        mid[0] + gamma * (x_r[0] - mid[0]),
        mid[1] + gamma * (x_r[1] - mid[1])
    ]


def contract(mid, w, betta=0.5):
    return [
        mid[0] + betta * (w[0] - mid[0]),
        mid[1] + betta * (w[1] - mid[1])
    ]


def shrink(f, points, delta=0.5):
    b = points[0]
    new_points = [
        b,
        [
            b[0] + delta * (points[1][0] - b[0]),
            b[1] + delta * (points[1][1] - b[1])
        ],
        [
            b[0] + delta * (points[2][0] - b[0]),
            b[1] + delta * (points[2][1] - b[1])
        ]
    ]
    return sort_points(f, new_points)


def square(points):
    a1 = points[0]
    a2 = points[1]
    a3 = points[2]
    return 0.5 * abs((a1[0] * a2[1] + a2[0] * a3[1] + a3[0] * a1[1]) -
                     (a1[1] * a2[0] + a2[1] * a3[0] + a3[1] * a1[0]))


def minimization(fun, x0, iter=50, e=0.0001, alpha=1, betta=0.5, gamma=2, delta=0.5):
    f = fun.f
    points = get_points(x0)
    points = sort_points(f, points)
    i = 0
    while i < iter or square(points) > e:
        i += 1
        b = points[0]
        g = points[1]
        w = points[2]
        mid = get_mid(points)
        x_r = reflection(mid, w, alpha)
        if f(x_r[0], x_r[1]) < f(g[0], g[1]):
            w = x_r
            x_e = expansion(mid, x_r, gamma)
            if f(x_e[0], x_e[1]) < f(b[0], b[1]):
                w = x_e
        else:
            x_c = contract(mid, w, betta)
            if f(x_c[0], x_c[1]) < f(g[0], g[1]):
                w = x_c
            else:
                w_points = sort_points(f, [x_r, x_c, g])
                b_of_w = w_points[1]
                if f(b_of_w[0], b_of_w[1]) < f(w[0], w[1]):
                    w = b_of_w
                else:
                    points = shrink(f, points, delta)
                    points = sort_points(f, points)
                    continue
        points = sort_points(f, [b, g, w])
    x = points[0]
    print(f.__doc__, ':')
    print('x0 =', x0)
    print(i, 'iteration')
    print('square:', square(points))
    print('answer:', f(x[0], x[1]))
    print('x_min:', x)


minimization(functions.f1, [100, 50])
print()
minimization(functions.f2, [5, 5])
