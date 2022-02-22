const express = require('express');
const bodyParser = require('body-parser');
const cors = require("cors");
const fs = require("fs");
const Buffer = require('buffer').Buffer;
const app = express();

a = null
let string = ";"

function join(array) {
	array.forEach(element =>{
		string.concat('element')
	})
	return string
}


app.use(cors())
app.use(bodyParser.json())

app.post('/', (req, res) =>{
	console.log('post is working');
	let string = req.body.Data

	var data = string.replace(/^data:image\/\w+;base64,/, "");
	// console.log(data)
	var buf = Buffer.from(data, 'base64');
	fs.writeFileSync('image.png', buf);
})
 
app.get('/', (req, res)=>{
	console.log('get is working')
	res.send(JSON.stringify(a))
})

app.listen(3000, ()=> { 
	console.log('app is running on port 3000')
})