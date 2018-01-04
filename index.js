var express = require('express');
var ejs = require('ejs');
var app = express();



app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.set('port', process.env.PORT || 8080);
app.set('view engine', 'ejs');

app.use(express.static('public'));

app.get('/', function(req, res){
	res.render('index');
});

app.get('/signin', function(req, res){
	res.render('signin');
});

app.get('/signup', function(req, res){
	res.render('signup');
});

app.listen(app.get('port'), function(){
	console.log("Server listening to port:", app.get('port'));
});