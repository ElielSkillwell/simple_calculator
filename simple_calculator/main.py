# -*- coding: utf-8 -*-
import operator
from functools import reduce

class SimpleCalculator:
    def add(self, *args):
        return sum(args)
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, *args):
        if not all(args):
            raise ValueError
        return reduce(operator.mul, args)
    
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
        
    def avg(self, num_lst, ul=None, ll=None):
        count = 0
        total = 0

        for number in num_lst:
            if ll is not None and number < ll:
                continue
            if ul is not None and number > ul:
                continue
            count += 1
            total += number
        if count == 0:
            return 0
        
        return total / count
