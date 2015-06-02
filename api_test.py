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

    '''
    body1 = {"query":
             {'match':
              {"id": '1807424'}
              }
             }
    '''

    res = es.search(index='test12', doc_type='json', body=body2, size=100000)
    print res
    return json.dumps(res['hits']['hits'])


def search_all():
    body3 = {"query":
             {"match_all":
              {
              }
              }
             }

    res = es.search(index='test12', doc_type='json', body=body3, size=100000)
    print res
    return json.dumps(res['hits']['hits'])


@app.route('/search/<labelname>')
def return_user(labelname):
    return search(str(labelname))


@app.route('/all')
def all_user():
    return search_all()


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 8998))
    app.run(host='0.0.0.0', port=port)
