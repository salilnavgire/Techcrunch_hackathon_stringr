from flask import request
from flask import Flask
import os
app = Flask(__name__)
import twilio
import json
from twilio.rest import TwilioRestClient

account_sid = "ACcad7f540a848b326e081324dd55e3870"
auth_token = "2a93bc053904a37a468f91b0c3077611"
client = TwilioRestClient(account_sid, auth_token)


def message(number):
    message = client.messages.create(to="+1"+str(number), from_="+16783048629",
                                     body="You got a match!!!")

@app.route('/message/<labelname>')
def show_category(labelname):
    return message(str(labelname))

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8988))
    app.run(host='0.0.0.0', port=port)
