#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator
import pytest


def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5)

    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4, 5, 6)
    assert result == 15


def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 4950


def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(10, 3)

    assert result == 7


def test_mult_two_numbers():
    calculator = SimpleCalculator()
    result =  calculator.mult(6, 4)
    assert result == 24


def test_mul_many_numbers():
    numbers = range(1,10)
    
    calculator = SimpleCalculator()
    result = calculator.mult(*numbers)

    assert result == 362880


def test_div_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.div(13, 2)

    assert result == 6.5


def test_div_by_zero():
    calculator = SimpleCalculator()
    
    result = calculator.div(13, 0)

    assert result == float('inf')


def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mult(3, 0)


def test_avg():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98])
    
    assert result == 29.5


def test_avg():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98])
    
    assert result == 29.25


def test_avg_ul():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ul=90)
    
    assert result == pytest.approx(6.33333)

def test_avg_ll():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ll=10)

    assert result == pytest.approx(55)


def test_avg_upper_threshold_is_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ul=98)

    assert result == 29.25


def test_avg_lower_threshold_is_included():
    calculator = SimpleCalculator()

    result = calculator.avg([2, 5, 12, 98], ll=2)

    assert result == 29.25


def test_avg_empty_lst():
    calculator = SimpleCalculator()

    result = calculator.avg([])

    assert result == 0


def test_avg_manages_empty_list_after_outlier_removal():
    calculator = SimpleCalculator()

    result = calculator.avg([12, 98], ll=15, ul=90)

    assert result == 0


def test_avg_manages_zero_value_lower_outlier():
    calculator = SimpleCalculator()

    result = calculator.avg([-1, 0, 1], ll=0)

    assert result == 0.5

def test_avg_manages_zero_value_higher_outlier():
    calculator = SimpleCalculator()

    result = calculator.avg([-1, 0, 1], ul=0)

    assert result == -0.5


def test_avg_accepts_generators():
    calculator = SimpleCalculator()
    result = calculator.avg(i for i in [2, 5, 12, 98])
    assert result == 29.25