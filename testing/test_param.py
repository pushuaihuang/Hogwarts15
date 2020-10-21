#!/usr/bin/env python
#coding=utf-8
import pytest
import yaml
#笛卡尔
# @pytest.mark.parametrize("b",[1,2,3])
# @pytest.mark.parametrize("a",[1,2,3])
# def test_para(a,b):
#     print(a,b)
#测试步骤驱动
from python.calculator import Calculator
def getSteps(path,cal,a,b,expect):
    with open(path) as f:
        step_data=yaml.safe_load(f)
    for step in step_data:
        if 'add' ==step:
            result=cal.mul(a,b)
        elif 'div' ==step:
            result=cal.div(a,b)
        assert expect==result
def test_steps():
    a=1
    b=1
    c=1
    getSteps('./setps/step.yaml',Calculator(),a,b,c)


