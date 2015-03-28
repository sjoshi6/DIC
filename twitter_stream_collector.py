import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests

Acc_Tok="3120279203-ZGGdoVNkg5ydlH4JVZHwxz4uDxB1wzOfvwCg1vZ"
Acc_Sec="YX59L7QZVHA9VcrNXsOjaKmjSptHxnG4jNpeGXjN0J6xh"
Con_Key="kC3Wmj9zPE5lv9rV56GuQgUls"
Con_sec="dfgOilCylFKjOXRwXQdu5CHDsdRJA19tJA6BM1VuyVPPd5X8MW"

class Stream_Listener(StreamListener):

    def on_data(self, data):
        value=json.loads(data)
        r=requests.post('http://localhost:8181/pushjson',json=value)
        print(r.status_code)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = Stream_Listener()
    auth = OAuthHandler(Con_Key, Con_sec)
    auth.set_access_token(Acc_Tok, Acc_Sec)

    stream = Stream(auth, l)
    stream.filter(track=['#'],languages=['en'])
