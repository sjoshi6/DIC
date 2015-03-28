var request = require('request');

module.exports = function(app) {

var hash_counter={}

app.post('/pushjson',function(req,res){

                              console.log(req.body.entities.hashtags);
                              var hashtags_arr=req.body.entities.hashtags

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


}
