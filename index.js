var fs = require("fs")
var jsonl = require("jsonl")

fs.createReadStream("C:\\Users\\izaganami\\Data_proj\\implant.json")
  .pipe(jsonl())
  .pipe(fs.createWriteStream("C:\\Users\\izaganami\\Data_proj\\implantout.json"))
