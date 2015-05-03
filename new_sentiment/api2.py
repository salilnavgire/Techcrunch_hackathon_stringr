from flask import request
from flask import Flask
import os
import unicodedata
from module import sentiment_new
app = Flask(__name__)


@app.route('/sentiment/<labelname>')
def show_sentiment(labelname):
    return str(sentiment_new.score(labelname))



if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8998))
    app.run(host='0.0.0.0',port=port)
    #print categorize.categorize_product('boots and shoes')
    #print str(integrate.get_sentiment('good'))
