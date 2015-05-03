import unicodedata
from flask import request, render_template
from flask import Flask
import os
from module import sentiment_new
app = Flask(__name__)


@app.route('/sentiment/', methods=['POST'])
def show_sentiment():
    print request.form
    return str(sentiment_new.score(request.form['data']))


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 9997))
    app.run(host='0.0.0.0', port=port)
