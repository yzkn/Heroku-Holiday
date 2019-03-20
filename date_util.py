from datetime import datetime


since_year = 69

def remove_slash_from_datestring(date):
    if date is not None:
        if date != '':
            if date.find('/') > -1:
                dateparts = date.split('/')
                if 3 == len(dateparts):
                    return '%04d%02d%02d' % (int(dateparts[0]),int(dateparts[1]),int(dateparts[2]))
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
            if date.find('/') > -1:
                if 3 == len(date.split('/')):
                    # yyyy/mm/dd
                    darr = date.split('/')
                    result = '%04d%02d%02d' % (int(darr[0]) , int(darr[1]) , int(darr[2]))
            elif date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yyyy-mm-dd
                    darr = date.split('-')
                    result = '%04d%02d%02d' % (int(darr[0]) , int(darr[1]) , int(darr[2]))
        if 8 == len(date):
            if date.find('/') > -1:
                if 3 == len(date.split('/')):
                    # yy/mm/dd
                    darr = date.split('/')
                    p_year = ''
                    if int(darr[0]) > since_year:
                        p_year = 1900 + int(darr[0])
                    else:
                        p_year = 2000 + int(darr[0])
                    result = '%04d%02d%02d' % (int(p_year) , int(darr[1]) , int(darr[2]))
            elif date.find('-') > -1:
                if 3 == len(date.split('-')):
                    # yy/mm/dd
                    darr = date.split('-')
                    p_year = ''
                    if int(darr[0]) > since_year:
                        p_year = 1900 + int(darr[0])
                    else:
                        p_year = 2000 + int(darr[0])
                    result = '%04d%02d%02d' % (int(p_year) , int(darr[1]) , int(darr[2]))
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
                result = '%04d%04d' % (int(p_year) , int(mmdd))
        elif 5 == len(date):
            if date.find('/') > -1:
                if 2 == len(date.split('/')):
                    # mm/dd
                    darr = date.split('/')
                    s_year = datetime.now().strftime('%Y')
                    result = '%04d%02d%02d' % (int(s_year) , int(darr[0]) , int(darr[1]))
            elif date.find('-') > -1:
                if 2 == len(date.split('-')):
                    # mm-dd
                    darr = date.split('-')
                    s_year = datetime.now().strftime('%Y')
                    result = '%04d%02d%02d' % (int(s_year) , int(darr[0]) , int(darr[1]))
        elif 4 == len(date):
            if date.isdecimal():
                # mmdd
                s_year = datetime.now().strftime('%Y')
                result = '%04d%04d' % (int(s_year) , int(date))
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
            result = '%04d%04d' % (p_year , mmdd)
        elif 4 == len(str(date)) or 3 == len(str(date)):
            # mmdd
            s_year = datetime.now().strftime('%Y')
            result = '%04d%04d' % (int(s_year) , date)
    if ''!=result:
        return str(result)
    else:
        return ''
