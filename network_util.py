import csv
import requests
from date_util import *

uri_caocsv = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'

def download_csv():
    result = {}
    response = requests.get(uri_caocsv)
    response.encoding = 'SHIFT_JIS'
    f = csv.reader(response.text.strip().splitlines())
    next(f)
    count = 0
    for r in f:
        key = remove_slash_from_datestring(r[0])
        result[key] = r[1]
        count+=1
    return result
