const express = require('express');
const bodyParser = require('body-parser');
const cors = require("cors");

const app = express();

// app.use(express.json())

app.use(cors())
app.use(bodyParser.json())

let a = null;
let dataRecieved = [];
let count = 0;
let temp = []

function convert(string){
	
}

app.post('/', (req, res) =>{
	console.log('post is working');
	let string = req.body.Data
	let image = convert(string)
})

app.get('/', (req, res)=>{
	console.log('get is working')
	res.send(JSON.stringify(a))
})

app.listen(3000, ()=> { 
	console.log('app is running on port 3000')
})