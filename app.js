var express  = require('express');
var connect = require('connect');
var app      = express();
var port     = process.env.PORT || 8181;

// Configuration
app.use(connect.logger('dev'));
app.use(connect.json());
app.use(connect.urlencoded());

var routedata = require('./routes.js')
routedata(app);

var server=app.listen(port, function () {

	  var host = server.address().address
	  var port = server.address().port

   	console.log('Example app listening at http://%s:%s', host, port)
});
