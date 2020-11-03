#!/usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
#coding=utf-8
import allure
import yaml
import pytest
from python.calculator import Calculator
# 解析测试数据
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
@pytest.mark.run(order=1)
@allure.feature("加法测试")
@allure.title("加法case")
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
@pytest.mark.run(order=4)
@allure.feature("乘法测试")
@allure.title("乘法case")
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
@pytest.mark.run(order=3)
@allure.feature("减法测试")
@allure.title("减法case")
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
@pytest.mark.run(order=2)
@allure.feature("除法测试")
@allure.title("除法case")
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




