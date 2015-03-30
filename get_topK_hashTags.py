import json
import requests
import sys

def printTopK(k):
    topk=int(k)
    response=requests.get('http://localhost:8181/tweet_hash_counter')
    data_topK=json.loads(response.text)
    asc_sorted = sorted(data_topK.iteritems(), key=lambda x:-x[1])[:topk]

    print('======================')
    print('Top '+str(topk)+' HashTags are:\n')
    for elem in asc_sorted:
         print("{0}: {1}".format(*elem))
    print('======================')


printTopK(sys.argv[1])
