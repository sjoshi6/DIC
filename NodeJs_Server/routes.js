var request = require('request');

module.exports = function(app) {

app.post('/pushjson',function(req,res){

                              console.log(req.body.id);
                              res.json('');

});


}
