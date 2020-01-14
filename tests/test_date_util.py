#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

from date_util import normalize_datestring
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


def test_normalize_datestring_str_yyyymmdd():
    assert normalize_datestring('20190101') == '20190101'


def test_normalize_datestring_str_yymmdd():
    assert normalize_datestring('190101') == '20190101'


def test_normalize_datestring_str_mmdd():
    assert normalize_datestring('0101') == '20190101'


def test_normalize_datestring_str_yyyymmdd_s():
    assert normalize_datestring('2019/01/01') == '20190101'


def test_normalize_datestring_str_yyyymmdd_h():
    assert normalize_datestring('2019-01-01') == '20190101'


def test_normalize_datestring_str_yymmdd_s():
    assert normalize_datestring('19/01/01') == '20190101'


def test_normalize_datestring_str_yymmdd_h():
    assert normalize_datestring('19-01-01') == '20190101'


def test_normalize_datestring_str_mmdd_s():
    assert normalize_datestring('01/01') == '20190101'


def test_normalize_datestring_str_mmdd_h():
    assert normalize_datestring('01-01') == '20190101'


def test_normalize_datestring_int_yyyymmdd():
    assert normalize_datestring(20190101) == '20190101'


def test_normalize_datestring_int_yymmdd():
    assert normalize_datestring(190101) == '20190101'


def test_normalize_datestring_int_mmdd():
    assert normalize_datestring(101) == '20190101'
