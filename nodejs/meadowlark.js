/**
 * http://usejsdoc.org/
 */
var express = require("express");
var app = express();

app.set('port',process.env.PORT || 3000);

app.use(function(req,res){
	res.type('Text()')
}