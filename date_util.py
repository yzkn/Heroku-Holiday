#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

from datetime import datetime
import sys


since_year = 69


def remove_slash_from_datestring(date):
    if date is not None:
        if date != '':
            if date.find('/') > -1:
                dateparts = date.split('/')
                if 3 == len(dateparts):
                    return '%04d%02d%02d' % (int(dateparts[0]), int(dateparts[1]), int(dateparts[2]))
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''


def normalize_datestring(date):
    """
    桁数・含まれている記号で条件分岐してyyyymmddに正規化
    """
    result = ''
    if type(date) is str:
        if 10 == len(date):
            if date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yyyy-mm-dd
                    darr = date.split('-')
                    result = '%04d%02d%02d' % (
                        int(darr[0]), int(darr[1]), int(darr[2]))
        elif 8 == len(date):
            if date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yy-mm-dd
                    darr = date.split('-')
                    p_year = ''
                    if int(darr[0]) > since_year:
                        p_year = 1900 + int(darr[0])
                    else:
                        p_year = 2000 + int(darr[0])
                    result = '%04d%02d%02d' % (
                        int(p_year), int(darr[1]), int(darr[2]))
            elif date.isdecimal():
                # yyyymmdd
                result = date
        elif 6 == len(date):
            if date.isdecimal():
                # yymmdd
                yy = date[0:2]
                mmdd = date[2:9]
                p_year = ''
                if int(yy) > since_year:
                    p_year = 1900 + int(yy)
                else:
                    p_year = 2000 + int(yy)
                result = '%04d%04d' % (int(p_year), int(mmdd))
        elif 5 == len(date):
            if date.find('-') > -1:
                if 2 == len(date.split('-')):
                    # mm-dd
                    darr = date.split('-')
                    s_year = datetime.now().strftime('%Y')
                    result = '%04d%02d%02d' % (
                        int(s_year), int(darr[0]), int(darr[1]))
        elif 4 == len(date):
            if date.isdecimal():
                # mmdd
                s_year = datetime.now().strftime('%Y')
                result = '%04d%04d' % (int(s_year), int(date))
    elif type(date) is int:
        if 8 == len(str(date)):
            # yyyymmdd
            result = '%08d' % date
        elif 6 == len(str(date)):
            # yymmdd
            p_year = ''
            yy = date // 10000
            mmdd = date % 10000
            if int(yy) > since_year:
                p_year = 1900 + int(yy)
            else:
                p_year = 2000 + int(yy)
            result = '%04d%04d' % (p_year, mmdd)
        elif 4 == len(str(date)) or 3 == len(str(date)):
            # mmdd
            s_year = datetime.now().strftime('%Y')
            result = '%04d%04d' % (int(s_year), date)
    if '' != result:
        return str(result)
    else:
        return ''


def normalize_filterstring(date):
    """
    桁数で条件分岐して前方一致検索用に正規化
    """
    print('normalize_filterstring({})'.format(date))
    result = ''
    if type(date) is str:
        if 10 == len(date):
            if date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yyyy-mm-dd
                    darr = date.split('-')
                    result = '%04d%02d%02d' % (
                        int(darr[0]), int(darr[1]), int(darr[2]))
        elif 8 == len(date):
            if date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yy-mm-dd
                    darr = date.split('-')
                    p_year = ''
                    if int(darr[0]) > since_year:
                        p_year = 1900 + int(darr[0])
                    else:
                        p_year = 2000 + int(darr[0])
                    result = '%04d%02d%02d' % (
                        int(p_year), int(darr[1]), int(darr[2]))
            elif date.isdecimal():
                # yyyymmdd
                result = '%08d' % (int(date))
        elif 7 == len(date):
            if date.find('-') > -1:
                if 2 == len(date.split('-')):
                    # yyyy-mm
                    darr = date.split('-')
                    result = '%04d%02d' % (int(darr[0]), int(darr[1]))
        elif 6 == len(date):
            if date.isdecimal():
                # yyyymm
                result = '%06d' % (int(date))
        elif 5 == len(date):
            if date.find('-') > -1:
                if 2 == len(date.split('-')):
                    # yy-mm
                    darr = date.split('-')
                    p_year = ''
                    if int(darr[0]) > since_year:
                        p_year = 1900 + int(darr[0])
                    else:
                        p_year = 2000 + int(darr[0])
                    result = '%04d%02d' % (int(p_year), int(darr[1]))
        elif 4 == len(date):
            if date.isdecimal():
                # yyyy
                print(date)
                result = '%04d' % (int(date))
        elif 2 == len(date):
            if date.isdecimal():
                # yy
                p_year = ''
                print(date)
                if int(date) > since_year:
                    p_year = 1900 + int(date)
                else:
                    p_year = 2000 + int(date)
                print('p_year: '+p_year)
                result = '%04d' % (int(p_year))
    elif type(date) is int:
        if 8 == len(str(date)):
            # yyyymmdd
            result = '%08d' % int(date)
        elif 6 == len(str(date)):
            # yyyymm
            result = '%06d' % (int(date))
        elif 4 == len(str(date)) or 3 == len(str(date)):
            # yyyy
            result = '%04d' % (int(date))
    if result:
        print('normalize_filterstring({}) result: {}'.format(date, result))
        return str(result)
    else:
        return ''
