var fs = require("fs")
var jsonl = require("jsonl")

fs.createReadStream("C:\\Users\\youne\\Projet_Dev_ENSG\\data.txt")
  .pipe(jsonl())
  .pipe(fs.createWriteStream("C:\\Users\\youne\\Projet_Dev_ENSG\\data.json"))
