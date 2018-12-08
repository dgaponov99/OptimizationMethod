class f1:

    @staticmethod
    def f(x1, x2):
        """function 1"""
        return 100 * (x2 - x1 ** 2) ** 2 + 5 * (1 - x1) ** 2

    @staticmethod
    def grad_f(x1, x2):
        return [-400 * x1 * (x2 - x1 ** 2) - 10 * (1 - x1), 200 * (x2 - x1 ** 2)]

    @staticmethod
    def grad2_f(x1, x2):
        return [[-400 * (x2 - 3 * x1 ** 2) + 10, -400 * x1],
                [-400 * x1, 200]]


class f2:

    @staticmethod
    def f(x1, x2):
        """function 2"""
        return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2

    @staticmethod
    def grad_f(x1, x2):
        return [
            4 * x1 * (x1 ** 2 + x2 - 11) + 2 * (x1 + x2 ** 2 - 7),
            2 * (x1 ** 2 + x2 - 11) + 4 * x2 * (x1 + x2 ** 2 - 7)
        ]

    @staticmethod
    def grad2_f(x1, x2):
        return [
            [4 * (3 * x1 ** 2 + x2 - 11) + 2, 4 * (x1 + x2)],
            [4 * (x1 + x2), 2 + 4 * (x1 + 3 * x2 ** 2 - 7)]
        ]
