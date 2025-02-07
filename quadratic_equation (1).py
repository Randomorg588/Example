# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:38:56 2024

@author: Олеся
"""



def square_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x, x
    else:
        print('Действительных корней нет')
        return None, None

a1 = square_quadratic(1, 2, 1)
b2 = square_quadratic(1, 4, 3)
c3 = square_quadratic(1, 2, 16)
print(a1)
print(b2)
print(c3)


 