// var fs = require("fs");

// var obj = JSON.parse(fs.readFile("./demo.json", "utf8"));

// console.log(obj);
// import * as fs from "fs";

require([fs.readFile("demo.json")], function (foo) {
  console.log(foo);
});
