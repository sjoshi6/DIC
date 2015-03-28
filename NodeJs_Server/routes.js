var request = require('request');

module.exports = function(app) {

app.post('/pushjson',function(req,res){

                              console.log(req.body.entities.hashtags);
                              var hashtags_arr=req.body.entities.hashtags

                              hashtags_arr.forEach(function(data_json){
                                console.log(data_json.text)
                              });
                              
                              res.json('');

});


}
