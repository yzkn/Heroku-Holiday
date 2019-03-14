import csv
import requests

uri_caocsv = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'

def download_csv():
    response = requests.get(uri_caocsv)
    response.encoding = 'SHIFT_JIS'

    f = csv.reader(response.text.strip().splitlines())
    next(f)
    count = 0
    for r in f:
        print(r)
        count+=1

    return count