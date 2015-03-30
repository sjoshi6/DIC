var request = require('request');

module.exports = function(app) {

var hash_counter={}
var slidingwindow=[]

app.post('/pushjson',function(req,res){

                              //extract the hashtag array from message
                              console.log(req.body.entities.hashtags);
                              var hashtags_arr=req.body.entities.hashtags

                              //untill window reaches windowsize=50 simply add elements to slider window.
                              if(slidingwindow.length <=50)
                              {
                                slidingwindow.push(hashtags_arr)
                              }
                              else
                              {
                                //as soon as the window crosses window size. Remove first element
                                var popped_list = slidingwindow.shift()

                                console.log('popped list')
                                console.log(popped_list)
                                //iterate over all the hashtags in popped element and decrement the hashcount
                                popped_list.forEach(function(data){
                                  hash_counter[data.text] = hash_counter[data.text] - 1
                                });
                                // Add the element at the end of slider window
                                slidingwindow.push(hashtags_arr)

                              }

                                hashtags_arr.forEach(function(data_json){
                                console.log(data_json.text)
                                var tweet_hash_text=data_json.text

                                if(hash_counter[tweet_hash_text])
                                {
                                    hash_counter[tweet_hash_text] = hash_counter[tweet_hash_text] + 1
                                }
                                else
                                {
                                  hash_counter[tweet_hash_text] = 1
                                }

                              });

                              console.log(hash_counter);

                              res.json('');

});

app.get('/tweet_hash_counter',function(req,res){
          //Reply back the current hashmap
          var json_reply = hash_counter;
          res.json(json_reply);
})

}
