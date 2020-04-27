#!/usr/bin/env python3

from stack_092 import Stack

def number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def calculator(string):
    lis = Stack()
    char = ['n', 'r']
    operator = ['+', '-', '*', '/']

    for value in string.split():
        if number(value):
            lis.push(float(value))
        elif value in operator:
            num1 = lis.pop()
            num2 = lis.pop()
            binops = {'+': num2 + num1, '-': num2 - num1, '*': num2 * num1, '/': num2 / num1}
            lis.push(binops[value])
        else:
            num3 = lis.pop()
            uniops = {'n': -num3, 'r': num3 ** 0.5}
            lis.push(uniops[value])
    return lis.pop()
