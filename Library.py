from typing import Optional, Union
import sympy as sp
import numpy as np
import pylab as plt
import re
import sqlite3 as sql
import random as r


class Methods:
    def __init__(self,
                 func: str,
                 symbol: str = 'x',
                 ):

        """Class for applying various numerical methods for a given function.

                :param func:
                    The function that you wish to use. Given as a string and then converted to a sympy expression.

                :param symbol:
                    This is the symbol that the derivative will be taken with respect to and what will be
                    substituted when evaluating the expression. If nothing is given then 'x' will be used.

                """

        self._raw_func = func.lower()
        self._func = sp.sympify(func.lower())
        self._symbol = sp.symbols(symbol.lower())
        self._diff = sp.diff(self._func, self._symbol)
        self._igl = sp.integrate(self._func, self._symbol)

    @property
    def func(self):
        return self._func

    @property
    def diff(self):
        return self._diff

    @property
    def igl(self):
        return f'{self._igl} + C'

    @func.setter
    def func(self, value):
        self._func = value
        self._diff = sp.diff(value, self._symbol)
        self._igl = sp.integrate(value, self._symbol)

    '''@staticmethod
    def type_checker(*args):
        for x in range(len(args)):
            if not isinstance():
                raise TypeError(f"Argument {} must be of type {}.")'''

    def newton(self,
               x0: float
               ):
        f = self._func
        df = self._diff
        t = self._symbol
        xs = [x0, float(x0 - f.subs(t, x0)/df.subs(t, x0))]
        while abs(xs[-1] - xs[-2]) > 1 * 10 ** -6:
            xs.append(xs[-1] - f.subs(t, xs[-1]) / df.subs(t, xs[-1]))
        return f'Result: {xs[-1]}   No. of Iterations: {len(xs) - 1}\n{xs}'

    def secant(self,
               x0: float,
               x1: float,
               ):
        f = self._func
        t = self._symbol
        xs = [x0, x1, float((x1*f.subs(t, x0)-x0*f.subs(t, x1))/(f.subs(t, x0)-f.subs(t, x1)))]
        while abs(xs[-1] - xs[-2]) > 10 ** -10:
            xs.append(
                (xs[-1] * f.subs(t, xs[-2]) - xs[-2] * f.subs(t, xs[-1])) / (f.subs(t, xs[-2]) - f.subs(t, xs[-1]))
            )
        return xs[-1], len(xs) - 2

    def bisection(self,
                  a: float,
                  b: float,
                  ):
        f = self._func
        t = self._symbol
        while True:
            c = (a+b)/2
            if abs(f.subs(t, c)) < 10**-6:
                return f'Solution: {c}'
            elif f.subs(t, a)*f.subs(t, c) < 0:
                b = c
            else:
                a = c
            print(a, b, f.subs(t, a))

    def numerical_derivative(self,
                             x0: float,
                             h: float):
        t = self._symbol
        return (self._func.subs(t, x0 + h) - self._func.subs(t, x0 - h))/(2 * h)

    def trapezoidal(self, a, b, n):
        xs = np.linspace(a, b, n)
        fs = list(map(lambda x: self._func.subs(self._symbol, x), xs))
        h = xs[1]-xs[0]
        return sum(fs) * h - (fs[0] - fs[-1])*h/2

    def graph(self,
              start: float,
              stop: float,
              step: int,
              xaxis: str = 'x values',
              yaxis: str = 'y values',
              show: bool = True
              ):

        """Gives an exact plot of the given function

            :param start: Starting point. Must be less than stopping point.

            :param stop: Stopping point. Must be greater than starting point.

            :param step: The number of points. Must be an integer.

            :param xaxis: Label for x-axis.

            :param yaxis: Label for y-axis.

            :param show: Pass False to be able to plot multiple functions on the same graph.
        """

        if start > stop:
            raise ValueError('Start param must be greater than stop param.')

        xs = list(np.linspace(start=start, stop=stop, num=int(np.floor(step))))
        print(xs)
        ys = []
        for x in xs:
            ys.append(self._func.subs(self._symbol, x))
        plt.plot(xs, ys)
        plt.xlabel(xaxis)
        plt.ylabel(yaxis)
        plt.axvline()
        plt.axhline()
        if show:
            plt.show()

def lagrange(x: float,
             xx: Union[list, np.ndarray],
             yy: Union[list, np.ndarray]
             ):
    def intermediate(i, x0, xs):
        return np.prod(list((x0 - xs[j]) / (xs[i] - xs[j]) for j in range(len(xs)) if i != j))
    return sum(intermediate(i, x, xx) * yy[i] for i in range(len(yy)))
