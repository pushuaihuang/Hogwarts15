#!/usr/bin/env python
#coding=utf-8
import allure
import yaml
import pytest
from python.calculator import Calculator

def get_adds(path,intstr,floatstr):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    # print(f'data={data}')
    add_int = data['datas'][intstr]
    add_float=data['datas'][floatstr]
    add_int_ids=data['ids']['add_int_ids']
    add_float_ids=data['ids']['add_float_ids']
    # print(add_datas)
    return [add_int,add_float,add_int_ids,add_float_ids]
path='../datas/cal.yml'
@allure.feature("加法测试")
class TestAdd:
    intstr = 'add_int'
    floatstr = 'add_float'
    @pytest.mark.parametrize('a,b,expect',get_adds(path,intstr,floatstr)[0],ids=get_adds(path,intstr,floatstr)[2])
    def test_add_int(self,a,b,expect,start_end):
        result=start_end.add(a,b)
        assert result==expect
    @pytest.mark.parametrize('a,b,expect', get_adds(path,intstr,floatstr)[1],ids=get_adds(path,intstr,floatstr)[3])
    def test_add_float(self, a, b, expect,start_end):
        result = start_end.add(a, b)
        assert result == expect
@allure.feature("乘法测试")
class TestMul:
    intstr = 'mul_int'
    floatstr = 'mul_float'
    @pytest.mark.parametrize('a,b,expect',get_adds(path,intstr,floatstr)[0])
    def test_mul_int(self,a,b,expect,start_end):
        result  = start_end.mul(a,b)
        assert result == expect
    @pytest.mark.parametrize('a,b,expect', get_adds(path, intstr, floatstr)[1])
    def test_mul_float(self, a, b, expect, start_end):
        result = start_end.mul(a, b)
        assert result == expect
@allure.feature("减法测试")
class TestSub:
    intstr = 'sub_int'
    floatstr = 'sub_float'
    @pytest.mark.parametrize('a,b,expect', get_adds(path, intstr, floatstr)[0])
    def test_sub_int(self,a,b,expect, start_end):
        result = start_end.sub(a,b)
        assert round(result,2)==expect
    @pytest.mark.parametrize('a,b,expect', get_adds(path, intstr, floatstr)[1])
    def test_sub_float(self,a,b,expect, start_end):
        result = start_end.sub(a,b)
        assert round(result,2)==expect
@allure.feature("除法测试")
class TestDiv:
    intstr = 'div_int'
    floatstr = 'div_float'
    @pytest.mark.parametrize('a,b,expect', get_adds(path, intstr, floatstr)[0])
    def test_div_int(self, a, b, expect,start_end):
        result = start_end.div(a, b)
        assert round(result,2) == expect
    @pytest.mark.parametrize('a,b,expect', get_adds(path, intstr, floatstr)[1])
    def test_div_float(self, a, b, expect,start_end):
        result = start_end.div(a, b)
        assert round(result,2) == expect
    @pytest.mark.parametrize('a,b,expect',[[1,0,1],[-1,0,-1]])
    def test_div_except(self,a, b, expect,start_end):
        with pytest.raises(ZeroDivisionError):
            start_end.div(a,b)




