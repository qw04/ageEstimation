const express = require('express');
const bodyParser = require('body-parser');
const cors = require("cors");
const fs = require("fs");
const Buffer = require('buffer').Buffer;
const app = express();
const {spawn} = require('child_process');

let array = [];

function join(array) {
	let string = "";
	array.forEach(element =>{
		string = string.concat(element)
	})
	return string
}


app.use(cors())
app.use(bodyParser.json())

app.post('/', (req, res) =>{

	console.log('post is working');
	let newString = req.body.Data
	if (newString.substr(0,4) === "stop"){
		let temp = join(array);
		// console.log();

		let boundary = newString.substr(4)
		let obj = JSON.stringify({"a": "null", "boundary": boundary});
		fs.writeFile('file.json', obj, (err) => {
			if (err) {
				throw err;
			}
		});

		var data = temp.replace(/^data:image\/\w+;base64,/, "");
		var buf = Buffer.from(data, 'base64');
		fs.writeFileSync('image.png', buf);
		array = [];
		res.send(JSON.stringify({"wow":"done"}));
	}else{
		array.push(newString);
	}
})
 


app.get('/', async (req, res)=>{

	fs.readFile('file.json', 'utf-8', (err, data) => {
			if (err) {throw err;}
			let obj = data;
			obj.a = "null";
			fs.writeFile('file.json', obj, (err) => {
			if (err) {
				throw err;
			}
	    	console.log("JSON data is saved.");
			});
		})

	
	
	const python = spawn('python', ['model.py']);
	python.on('close', (code) => {
 		console.log('model has predicted');
 	});

	// obj = read()
	let temp = "null";
	while (temp === "null"){
		// console.log(temp);
		fs.readFile('file.json', 'utf-8', (err, data) => {
			if (err) {throw err;}
			obj = data.toString();
			temp = JSON.parse(obj).a;
		})
		// console.log(temp)
		await new Promise(resolve => setTimeout(resolve, 1000));
	}
	if (temp != "null"){
		res.send(JSON.stringify(obj));
		console.log("get is working");
	}
})

app.listen(3000, ()=> { 
	console.log('app is running on port 3000')
})