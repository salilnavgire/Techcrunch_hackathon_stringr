import urllib2
import requests
import json
num_id = '2422631'
num_list = [1807424, 32215203, 9679046, 7559526, 31162695, 44967370, 2422631, 32191179, 76154343, 922374, 3966515, 59606580, 15910174, 526486, 4263931, 9763705, 1072199, 4629851, 4003901, 942279]

if __name__ == '__main__':
    #r = requests.post('http://0.0.0.0:8998/search/', {'id': num_id})
    #print r.text

    '''
    r = requests.post('http://6f91eb69.ngrok.com/search/', {'id': num_id})
    print json.loads(r.text)
    #print r
    '''


    #print json.dumps(r.text, separators=(',',':'), indent=4)
    '''
    for res in json.loads(r.text):
        print json.dumps(res, separators=(',',':'), indent=4)
    '''

    '''
    r = requests.get('http://6f91eb69.ngrok.com/search/'+num_id)
    print r.text
    '''

    list3 = []
    for res in num_list:
        print res
        r = requests.get('http://6f91eb69.ngrok.com/search/'+str(res))
        list3.append(json.loads(r.text))


    print list3
    with open('data1.txt', 'w') as outfile:
        json.dump(list3, outfile)