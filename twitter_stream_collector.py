import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import urllib2
import urllib

Acc_Tok="3120279203-ZGGdoVNkg5ydlH4JVZHwxz4uDxB1wzOfvwCg1vZ"
Acc_Sec="YX59L7QZVHA9VcrNXsOjaKmjSptHxnG4jNpeGXjN0J6xh"
Con_Key="kC3Wmj9zPE5lv9rV56GuQgUls"
Con_sec="dfgOilCylFKjOXRwXQdu5CHDsdRJA19tJA6BM1VuyVPPd5X8MW"

class Stream_Listener(StreamListener):

    def on_data(self, data):
        url = 'http://localhost:8181/pushjson'
        data = json.loads(data)
	    value = urllib.urlencode(data)
	    f = urllib2.urlopen(url,value)
        f.close()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = Stream_Listener()
    auth = OAuthHandler(Con_Key, Con_sec)
    auth.set_access_token(Acc_Tok, Acc_Sec)

    stream = Stream(auth, l)
    stream.filter(track=['car'])
