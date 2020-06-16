#!flask/bin/python
import json
from flask import Flask, Response, request
from pyfcm import FCMNotification

app = Flask(__name__)
push_service = FCMNotification(
    api_key='AAAApod84hI:APA91bHiTbzHHrJlMzoUcV5MaG8vDfMrQGvHs6IyjffOrMDeoNlcPMYyxr1n9gfdsL_qjVjP_88a_a3MYi0Iigsmc1fbq6EWsJKw_o8dgX5QBLzoG5g0DjgWqp4o1u1NDN_WyPWVq92y')
nth = 0


@app.route('/', methods=['GET'])
def test():
    return "test"


@app.route('/push', methods=['POST'])
def push():
    global nth
    nth += 1

    message_title = request.form.get('title')
    message_body = request.form.get('body')
    mToken = request.form.get('token')
    result = push_service.notify_single_device(registration_id=mToken, message_title=message_title,
                                               message_body=message_body)
    print(push_service.send_request_responses)
    print(result)
    return Response(json.dumps({'Output': result}), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')