var fs = require("fs");
var express = require("express");
app = express.createServer();
const PORT = process.env.PORT || 3000;
app.use(express.static(__dirname + '/Web'));
app.get('/', function(req, res) {
    fs.readFile(__dirname + '/Web/index.html', 'utf8', function(err, text){
        res.send(text);
    });
});
app.listen(PORT);