import json
import requests

response=requests.get('http://localhost:8181/tweet_hash_counter')
print(response.text)
self.printTopK(response.text,self.count,window_size_in_tweets)

def printTopK(self,k):
    topk=k
    response=requests.get('http://localhost:8181/tweet_hash_counter')
    data_topK=json.loads(response)
    asc_sorted = sorted(data_topK.iteritems(), key=lambda x:-x[1])[:topk]

    print('======================')
    print('Top '+topk+' HashTags are:\n')
    for elem in asc_sorted:
         print("{0}: {1}".format(*elem))
    print('======================')
