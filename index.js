var fs = require("fs")
var jsonl = require("jsonl")

fs.createReadStream("C:\\Users\\izaganami\\Data_proj\\resid.json")
  .pipe(jsonl())
  .pipe(fs.createWriteStream("C:\\Users\\izaganami\\Data_proj\\residout.json"))
