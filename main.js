var http = require('http'),
    fs = require('fs'),
    path = require('path');
const PORT = process.env.PORT || 3000;
var express = require('express');
var app = express();
p=__dirname
console.log(p)
var server = http.createServer(app);


app.use(express.static(__dirname + '/Web'));
app.get('/', function(req, res) {
    fs.readFile(__dirname + '/Web/index.html', 'utf8', function(err, text){
        res.send(text);
    });
});
app.listen(PORT);