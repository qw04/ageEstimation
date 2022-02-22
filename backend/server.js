const express = require('express');
const bodyParser = require('body-parser');
const cors = require("cors");

const app = express();

// app.use(express.json())

app.use(cors())




app.use(bodyParser.json())
app.post('/', (req, res) =>{
	console.log(req.body);
})

app.get('/', (req, res)=>{
	console.log('get is working')
	res.send(JSON.stringify("get is working"))
})

app.listen(3000, ()=> {
	console.log('app is running on port 3000')
})