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

    def __init__(self):
        self.count=0

    def on_data(self, data):

        window_size_in_tweets=20
        value=json.loads(data)
        r=requests.post('http://localhost:8181/pushjson',json=value)

        self.count=self.count+1
        if(self.count%window_size_in_tweets==0):
            response=requests.get('http://localhost:8181/tweet_hash_counter')
            print(response.text)
            self.printTopK(response.text,self.count,window_size_in_tweets)

        print("Tweet count"+str(self.count))
        return True


    def on_error(self, status):
        print(status)


    def printTopK(self,response,count,window_size):
        topk=2
        data_topK=json.loads(response)
        asc_sorted = sorted(data_topK.iteritems(), key=lambda x:-x[1])[:topk]

        print('======================')
        start_tweet=count-window_size
        end_tweet=count
        print('Top Tweets between'+str(start_tweet)+'--'+str(end_tweet))
        for elem in asc_sorted:
             print("{0}: {1}".format(*elem))
        print('======================')


if __name__ == '__main__':
    l = Stream_Listener()
    auth = OAuthHandler(Con_Key, Con_sec)
    auth.set_access_token(Acc_Tok, Acc_Sec)

    stream = Stream(auth, l)
    stream.filter(track=['#'],languages=['en'])
