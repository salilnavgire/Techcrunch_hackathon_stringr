import soundcloud

# create a client object with your app credentials
client = soundcloud.Client(client_id='21c154c0424e721ba43428dc0b5af838')

print client

tracks = client.get('/tracks', genres='punk', license='cc-by-sa')

for res in tracks:
    print res.id
