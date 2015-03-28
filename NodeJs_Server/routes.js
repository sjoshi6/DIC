var request = require('request');

module.exports = function(app) {

app.post('/pushjson',function(req,res){

                              console.log(req.body.entities)
                              console.log(req.body.entities['hashtags']);
                              res.json('');

});


}
