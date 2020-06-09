#!flask/bin/python
import json
from flask import Flask, Response
from pyfcm import FCMNotification

app = Flask(__name__)
# api_key='AAAAFxr6tmI:APA91bEGjpVkHoeFbVb5H6D9PtCPsmOgTml7FU0NqSWmzEPgJm1hlzTktQUr3mmhmCBLC_BH34otKd0wR_48wUQHPCS80qnqiYYd-e9o7QjYJvirLFUYXAlgn0IzfdsS-VqPeKFNMDMI'
push_service = FCMNotification(
    api_key='AAAApod84hI:APA91bHiTbzHHrJlMzoUcV5MaG8vDfMrQGvHs6IyjffOrMDeoNlcPMYyxr1n9gfdsL_qjVjP_88a_a3MYi0Iigsmc1fbq6EWsJKw_o8dgX5QBLzoG5g0DjgWqp4o1u1NDN_WyPWVq92y')
mToken = 'fUfv0pYjI_I:APA91bG88Qf9FtfMv21IOrCDoXJm8KQqPfmHz3dvn30lbwl1KT066zFhfQEtwYr5gvWPD0yvMwwi3surEAic9qb4nnH-EcqDvckw5NzkacFj8aZ4Gc-wsgquJp_jP6N-hBM6dKBssoyF'
nth = 0


@app.route('/push', methods=['GET'])
def push():
    global nth
    nth += 1
    registration_id = mToken

    message_title = "Test title"
    message_body = "Test body"
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                               message_body=message_body)
    print(push_service.send_request_responses)
    print(result)
    return Response(json.dumps({'Output': result}), mimetype='application/json', status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')