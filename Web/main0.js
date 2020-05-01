var http = require('http'),
    fs = require('fs'),
    path = require('path'),
    filePath = path.join(__dirname, 'Web/index.html'),
    express=require('express');
const PORT = process.env.PORT || 3000;
console.log("Port:"+ PORT)
var glob = require("glob")

glob("**/*.html", function (er, files) {
    console.log(files)
})



var app = require('http').createServer(createServer);
console.log(__dirname);
app.use(express.static(__dirname));
var url = require('url');

function createServer(req, res) {
    var path = url.parse(req.url).pathname;
    var fsCallback = function(error, data) {
        if(error) throw error;

        res.writeHead(200);
        res.write(data);
        res.end();
    }

    switch(path) {
        case '/Page_1.html':
            doc = fs.readFile(__dirname + '/Web/Page_1.html', fsCallback);
        break;
        default:
            doc = fs.readFile(__dirname + '/Web/index.html', fsCallback);
        break;
    }
}

app.listen(PORT);

/**
fs.readFile(filePath, {encoding: 'utf-8'}, function (err, html) {
    if (err) {

        console.log('something bad');
        console.log(err)

    }
    http.createServer(function(request, response) {
        response.writeHeader(200, {"Content-Type": "text/html"});
        response.write(html);
        response.end();

    }).listen(PORT);
});**/env.PORT || 3000;