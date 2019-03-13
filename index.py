from flask import Flask, jsonify, after_this_request
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

app = Flask(__name__)

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

    message = "Updated!"
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
    return jsonify(ResultSet=result)

@app.route('/<date>', methods=['GET'])
def isHoliday(date):
    dateStr = '2019-01-01' #TODO: 日付をyyyymmddに正規化

    #TODO: yyyymmddが祝日か判定
    isHoliday = True

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

if __name__ == '__main__':
    app.run()
