const express = require('express');
const bodyParser = require('body-parser');
const cors = require("cors");
const fs = require("fs");
const Buffer = require('buffer').Buffer;
const app = express();
const {spawn} = require('child_process');


let string = "";
let temp = false;

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
 


app.get('/', async (req, res)=>{

	let obj = JSON.stringify({a:"null"});
	fs.writeFile('file.json', obj, (err) => {
		if (err) {
			throw err;
		}
	    console.log("JSON data is saved.");
	});
	
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
		await new Promise(resolve => setTimeout(resolve, 500));
	}
	if (temp === 1 || temp === 0){
		console.log("get is working");
		res.send(JSON.stringify(JSON.parse(obj).a));
	}

// async function needs to have a catch block

})

app.listen(3000, ()=> { 
	console.log('app is running on port 3000')
})