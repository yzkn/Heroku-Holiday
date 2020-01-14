#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

from date_util import *
import csv
import re
import requests
import sys
import traceback
import urllib

uri_caocsv = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'


def download_csv():
    result = {}
    if uri_exists(uri_caocsv):
        try:
            response = requests.get(uri_caocsv)
            response.encoding = 'SHIFT_JIS'
            f = csv.reader(response.text.strip().splitlines())
            next(f)
            count = 0
            for r in f:
                key = remove_slash_from_datestring(r[0])
                result[key] = r[1]
                print(key + ': ' + r[1])
                count += 1
        except Exception as e:
            t, v, tb = sys.exc_info()
            print(traceback.format_exception(t, v, tb))
            print(traceback.format_tb(e.__traceback__))
    return result


def uri_exists(url):
    try:
        if re.match(r"^https?:\/\/", url):
            try:
                res = urllib.request.urlopen(url)
                res.close()
                return True
            except urllib.error.HTTPError as e:
                return False
            except urllib.error.URLError as e:
                return False
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t, v, tb))
        print(traceback.format_tb(e.__traceback__))
        return False
