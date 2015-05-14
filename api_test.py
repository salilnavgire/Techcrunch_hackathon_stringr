from elasticsearch import Elasticsearch
from flask import Flask
import os
import json
app = Flask(__name__)

es = Elasticsearch()
print es


def search(usr_id):
    body2 = {"query":
             {'match':
              {"id": usr_id}
              }
             }

    body1 = {"query":
             {'match':
              {"id": '1807424'}
              }
             }

    body3 = {"query":
             {"match_all":
              {
              }
              }
             }

    print body1
    res = es.search(index='test9', doc_type='tweet', body=body2, size=100000)
    # return json.dumps(res['hits']['hits'])
    print res
    return json.dumps(res['hits']['hits'])


@app.route('/search/<labelname>')
def show_category(labelname):
    return search(str(labelname))


'''
@app.route('/search/', methods=['POST'])
def show_sentiment():
    print request.form
    print request.form['id']
    return search(request.form['id'])
'''

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8998))
    app.run(host='0.0.0.0', port=port)
