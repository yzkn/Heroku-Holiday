from date_util import *
from datetime import datetime
from flask import Flask, jsonify, after_this_request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from network_util import download_csv
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from time import mktime
from wsgiref.handlers import format_date_time
import os
import sys
import traceback

db_last_modified = datetime(2000, 1, 1, 0, 0, 0)

try:
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "postgresql://postgres:Passw0rd@localhost:5432/holiday"
    db = SQLAlchemy(app)
    CORS(app)
except Exception as e:
    t, v, tb = sys.exc_info()
    print(traceback.format_exception(t,v,tb))
    print(traceback.format_tb(e.__traceback__))


@app.route('/', methods=['GET'])
def index():
    @after_this_request
    def d_header(response):
        response.headers['Last-Modified'] = format_date_time(mktime(db_last_modified.timetuple()))
        return response
    return jsonify(ResultSet=read_holidays())


@app.route('/update', methods=['GET'])
def update():
    holidays = download_csv()
    message = {}
    if len(holidays)>0:
        cleared = clear_holidays()
        if cleared:
            message = add_holidays(holidays)
        else:
            message['message'] = 'DB Not Cleared'
    else:
        message['message'] = 'CSV Not Downloaded'

    @after_this_request
    def d_header(response):
        db_last_modified = datetime.now()
        response.headers['Last-Modified'] =  format_date_time(mktime(db_last_modified.timetuple()))
        return response
    return jsonify(ResultSet=message)


@app.route('/<date>', methods=['GET'])
def isHoliday(date):
    dateStr = normalize_datestring(date)
    if ''==dateStr:
        dateStr = datetime.now().strftime('%Y%m%d')
    result = {
        dateStr: holiday_exists(dateStr)
    }

    @after_this_request
    def d_header(response):
        response.headers['Last-Modified'] =  format_date_time(mktime(db_last_modified.timetuple()))
        return response
    return jsonify(ResultSet=result)


def add_holidays(holidays):
    result = {}
    try:
        for k,v in holidays.items():
            holiday = Holiday(k,v)
            db.session.add(holiday)
            result[k] = v
        db.session.commit()
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
    return result


def clear_holidays():
    try:
        holidays = Holiday.query.all()
        for holiday in holidays:
            db.session.delete(holiday)
        db.session.commit()
        return True
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
    return False


def holiday_exists(target):
    try:
        holidays_count = db.session.query(Holiday).filter_by(date=target).count()
        return holidays_count > 0
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
        return False


def read_holidays():
    result = {}
    try:
        holidays = Holiday.query.all()
        for holiday in holidays:
            result[holiday.date] = holiday.name
    except Exception as e:
        t, v, tb = sys.exc_info()
        print(traceback.format_exception(t,v,tb))
        print(traceback.format_tb(e.__traceback__))
    return result


class Holiday(db.Model):
    """
    祝日
    """
    __tablename__ = "holidays"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Unicode(8), unique=True, nullable=False)
    name = Column(Unicode(255), unique=False, nullable=False)

    def __init__(self, date, name):
        self.date = date
        self.name = name

    def __repr__(self):
        return '<Holiday {}:{}>'.format(self.date, self.name)

if __name__ == '__main__':
    app.run()
