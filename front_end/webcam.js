var videoElement = document.querySelector('video');
var videoSelect = document.querySelector('select#videoSource');

videoSelect.onchange = getStream;

getStream().then(getDevices).then(gotDevices);

function getDevices() {
  return navigator.mediaDevices.enumerateDevices();
}

function gotDevices(deviceInfos) {
  window.deviceInfos = deviceInfos; // make available to console
  // console.log('Available input and output devices:', deviceInfos);
  for (const deviceInfo of deviceInfos) {
    const option = document.createElement('option');
    option.value = deviceInfo.deviceId;
    if (deviceInfo.kind === 'videoinput') {
      option.text = deviceInfo.label || `Camera ${videoSelect.length + 1}`;
      videoSelect.appendChild(option);
    }
  }
}

function getStream() {
  if (window.stream) {
    window.stream.getTracks().forEach(track => {
      track.stop();
    });
  }
  const videoSource = videoSelect.value;
  const constraints = {
    video: {deviceId: videoSource ? {exact: videoSource} : undefined}
  };
  return navigator.mediaDevices.getUserMedia(constraints).
    then(gotStream).catch(handleError);
}

function gotStream(stream) {
  window.stream = stream; // make stream available to console
  videoSelect.selectedIndex = [...videoSelect.options].
    findIndex(option => option.text === stream.getVideoTracks()[0].label);
  videoElement.srcObject = stream;
}

function handleError(error) {
  console.error('Error: ', error);
}

let click_button = document.querySelector("#click-photo");
let canvas = document.querySelector("#canvas");
let video = document.querySelector("video");

function split(str, size) {
  const numChunks = Math.ceil(str.length / size)
  const chunks = new Array(numChunks)

  for (let i = 0, o = 0; i < numChunks; ++i, o += size) {
    chunks[i] = str.substr(o, size)
  }

  return chunks
}

function upload(array){
  array.forEach(element => {fetch('http://localhost:3000', {
          method: 'POST',
          body: JSON.stringify({"Data": element}),
          headers: {'Content-Type': 'application/json'},
          }).catch(error => {console.error('Error:', error)})
    })
}


click_button.addEventListener('click', function() {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpg');
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    let array = split(image_data_url, 20000);
    // let array = [image_data_url]
    array.push("stop")
    // console.log(array.length)
    upload(array)

    let result = document.querySelector("#resultText");
    result.innerText = "result: thinking";
    
    //wait till the keyword arrives
    //then fetch post arrives on the backend too slow
    fetch('http://localhost:3000').then(res => {console.log(res.json())}).catch(err => {console.error('Error: ', err)})
    // result.innerText = "result: " + res.json()
    // take data from promise and update website




  })