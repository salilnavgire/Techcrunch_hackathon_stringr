from __future__ import division
import requests
import soundcloud
import operator
from collections import Counter
from collections import defaultdict
import numpy as np
from elasticsearch import Elasticsearch
es = Elasticsearch()


'''
Register on https://developers.soundcloud.com for a new app and get a client_id
'''
client_id = '20302b73d7cf5fc7251ccb197953dc02'


def client_login(client_id):
    '''
    Soundcloud clint login
    '''
    client = soundcloud.Client(client_id=client_id)
    return client


def search_tracks(genre):
    '''
    Search top tracks in a genre
    '''
    tracks = client.get('/tracks')
    return tracks


def get_uri(tracks):
    trackid = []
    user = []
    uri = []
    for res in tracks:
        trackid.append(res.id)
        user.append(res.user)
        uri.append(res.user['uri'])
    return trackid, user, uri


def get_user_info(uri):
    '''
    Get user information based on track url
    '''
    user_info = []
    for res in Counter(uri).keys():
        user_info.append(client.get('/resolve', url=res))
    return user_info


def get_user_url(user_info):
    users = defaultdict(list)
    for res in user_info:
        attrs = vars(res)['obj']
        users[attrs['id']].append(attrs['website'])
    return users


def sentiment(data):
    '''
    Get sentiment score from the sentiment api
    '''
    r = requests.post('http://localhost:9997/sentiment/', {'data': data})
    return r.text


def get_sentiment(ids):
    '''
    Get average Sentiment score for a artist based on aggregate comments on
    each of their tracks
    '''
    sen = []
    track_info = client.get('/tracks', user_id=ids)
    some_dict = defaultdict()
    for res in track_info:
        track_sen = []
        attrs = vars(res)
        com_id = attrs['obj']['id']
        comment_info = client.get('/tracks/'+str(com_id)+'/comments/', )
        commen = 0
        for res in comment_info:
            commen += 1
            attrsssss = vars(res)['obj']
            something = float(sentiment(attrsssss['body']))
            sen.append(something)
            track_sen.append(something)
        some_dict[attrs['obj']['permalink_url']] = (sum(track_sen) /
                                                    (np.maximum(len(sen), 1.0)))*(commen)
    # print sum(sen)/(np.maximum(len(sen), 1.0))
    sorted_x = sorted(some_dict.items(), key=operator.itemgetter(1))[::-1]
    # print sorted_x[:3]
    return sum(sen)/(np.maximum(len(sen), 1.0)), sorted_x[:3]


def index_users(user_info):
    '''
    Calculate score for each artist based on ensemble of average Sentiment score,
    playlist_count and followers_count.
    Each artist data is stored in Elasticsearch index
    '''
    count = 0
    for res in user_info:
        print res
        attrs = vars(res)['obj']
        print attrs['id']
        count += 1
        avg_sen, sorted_x = get_sentiment(attrs['id'])

        base = attrs
        print ((((avg_sen*0.9)/5)+((np.maximum(base['playlist_count'], 1)/20)*0.12)
               + ((base['followers_count']/2000000)*0.11))*100)
        try:
            body_query = {
                'id': attrs['id'],
                'username': attrs['username'],
                'full_name': attrs['full_name'],
                'country': attrs['country'],
                'city': attrs['city'],
                'track_count': attrs['track_count'],
                'playlist_count': attrs['playlist_count'],
                'followers_count': attrs['followers_count'],
                'public_favorite_count': attrs['public_favorites_count'],
                'avg_sentiment': avg_sen,
                'score': ((((avg_sen*0.9)/5)+((np.maximum(base['playlist_count'],
                           1)/20)*0.12)
                           + ((base['followers_count']/2000000)*0.11))*100),
                'links': sorted_x
                    }
        except KeyError:
            pass
        except IndexError:
            pass
        print body_query

        es.index(index="test12", doc_type='json', id=count, body=body_query)


if __name__ == '__main__':
    client = client_login(client_id)
    tracks = search_tracks('rock')
    trackid, user, uri = get_uri(tracks)
    user_info = get_user_info(uri)
    users = get_user_url(user_info)
    # avg_sen = get_sentiment('2422631')
    # print avg_sen
    index_users(user_info)
