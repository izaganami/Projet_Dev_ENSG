var http = require('http'),
    fs = require('fs'),
    path = require('path'),
    filePath = path.join(__dirname, 'Web/index.html');

var glob = require("glob")

glob("**/*.html", function (er, files) {
    console.log(files)
})

fs.readFile(filePath, {encoding: 'utf-8'}, function (err, html) {
    if (err) {

        console.log('something bad');
        console.log(err)

    }
    http.createServer(function(request, response) {
        response.writeHeader(200, {"Content-Type": "text/html"});
        response.write(html);
        response.end();
    }).listen(8000);
});