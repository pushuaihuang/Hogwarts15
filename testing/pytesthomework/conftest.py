#!/usr/bin/env python
#coding=utf-8
import pytest
from python.calculator import Calculator
@pytest.fixture(scope="module",autouse=True)
def start_end():
    cal = Calculator()
    #yiled前面相当于setup
    print("开始计算")
    yield cal
    #yiled后面相当于teardown
    print("结束计算")