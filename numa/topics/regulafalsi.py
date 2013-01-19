# -*- coding: utf-8 -*-

"""
Metoda Regula falsi.
"""

from sympy import Abs
from numa.utils import float_input, expr_input, eval_expr


def regulafalsi(a, b, fn, e):
    """
    S vyuzitim metody Regula falsi vypocita koren funkcie fn
    na intervale <a,b>.
    """

    assert a < b, 'Cislo b musi byt vacsie ako cislo a'
    assert e > 0, 'Presnost e musi byt vacsia ako nula'

    f = lambda x: eval_expr(fn, x=x)
    x = a

    while True:
        x1 = a - ((b - a) / (f(b) - f(a)) * f(a))

        if f(x1) == 0:
            return x1
        elif f(a) * f(x1) < 0:
            b = x1
        else:
            a = x1

        if Abs(x1 - x) <= e:
            return x1

        x = x1


if __name__ == '__main__':
    a = float_input('Zadajte cislo a')
    b = float_input('Zadajte cislo b')
    fn = expr_input('Zadajte funkciu fn')
    e = float_input('Zadajte presnost e', default=0.01)

    print regulafalsi(a, b, fn, e)