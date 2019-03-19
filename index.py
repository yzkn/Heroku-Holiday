from date_util import *
from datetime import datetime
from flask import Flask, jsonify, after_this_request
from flask_sqlalchemy import SQLAlchemy
from network_util import download_csv
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from time import mktime
from wsgiref.handlers import format_date_time
import os


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or "postgresql://postgres:Passw0rd@localhost:5432/holiday"
db = SQLAlchemy(app)

db_last_modified = datetime(2000, 1, 1, 0, 0, 0)


@app.route('/', methods=['GET'])
def index():
    message = "Hi!"
    result = {
        "Result": {
            "message": message
        }
    }

    @after_this_request
    def d_header(response):
        response.headers['Last-Modified'] = format_date_time(mktime(db_last_modified.timetuple()))
        return response
    return jsonify(ResultSet=result)


@app.route('/update', methods=['GET'])
def update():
    holidays = download_csv()
    clear_holidays()
    message = add_holidays(holidays)
    result = {
        "Result": {
            "message": message
        }
    }

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
    isHoliday = holiday_exists(dateStr)

    result = {
        "Result": {
            dateStr: isHoliday
        }
    }

    @after_this_request
    def d_header(response):
        response.headers['Last-Modified'] =  format_date_time(mktime(db_last_modified.timetuple()))
        return response
    return jsonify(ResultSet=result)


def add_holidays(holidays):
    #TODO: 例外処理
    for k,v in holidays.items():
        holiday = Holiday(k,v)
        db.session.add(holiday)
    db.session.commit()
    return ''


def clear_holidays():
    #TODO: 例外処理
    holidays = Holiday.query.all()
    for holiday in holidays:
        db.session.delete(holiday)
    db.session.commit()
    return ''


def holiday_exists(target):
    #TODO: 例外処理
    holidays_count = db.session.query(Holiday).filter_by(date=target).count()
    return holidays_count > 0


class Holiday(db.Model):
    """
    祝日
    """
    __tablename__ = "holidays"
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Unicode(8), unique=True)
    name = Column(Unicode(255), unique=False)

    def __init__(self, date, name):
        self.date = date
        self.name = name

    def __repr__(self):
        return '<Holiday %r>' % self.name

if __name__ == '__main__':
    app.run()
