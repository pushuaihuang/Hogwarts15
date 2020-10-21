#!/usr/bin/env python
# coding=utf-8
import pytest

from python.calculator import Calculator



@pytest.mark.add
def test_add():
    cal = Calculator()
    result = cal.add(4, 5)
    assert result == 9
