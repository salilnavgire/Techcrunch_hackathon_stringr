import requests
import json

num_list = [150253403, 37468197, 75958638, 980616, 144982481, 12092239, 156143304, 41358123, 36633920, 18170900,
            20146318, 99730465, 5170489, 19338959, 12399304, 31900943, 471457, 4456085, 44068194,
            41753883, 117083897, 21385553, 36793675, 155502458, 84469028, 49476248, 46982479, 2399217,
            73041712, 124844721, 121641150]


def return_all_ids():
    r = requests.get('http://localhost:8998/all')
    return json.loads(r.text)


def search_userid(res):
    r = requests.get('http://localhost:8998/search/'+str(res))
    return json.loads(r.text)


def search_all_userids():
    list3 = []
    for res in num_list:
        list3.append(search_userid(res))
    return list3


def backup_ids():
    data = return_all_ids()
    ids = []
    for res in data:
        ids.append(res['_source']['id'])
    with open('userids.txt', 'w') as outfile:
        json.dump(ids, outfile)


if __name__ == '__main__':
    # print len(search_all_userids())
    backup_ids()
