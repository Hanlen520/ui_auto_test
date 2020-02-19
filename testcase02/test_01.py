# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 16:27
# @Author  : mrwuzs
# @Email   : mrwuzs@outlook.com
# @File    : test_01.py
# @Software: PyCharm
import pytest

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    assert False

@pytest.mark.dependency()
def test_b():
    pass

@pytest.mark.dependency(depends=["test_a"])
def test_c():
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass

@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    pass
