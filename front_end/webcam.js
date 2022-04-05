var videoElement = document.querySelector('video');
var videoSelect = document.querySelector('select#videoSource');

// videoSelect.onchange = getStream;
// const constraints = {
//     video: {kind: 'videoinput'}
//   };

// navigator.mediaDevices.getUserMedia(constraints).then(stream => videoElement.srcObject = stream)

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
let boundary = document.querySelector("#boundaryDropDown");

function split(str, size) {
  const numChunks = Math.ceil(str.length / size)
  const chunks = new Array(numChunks)

  for (let i = 0, o = 0; i < numChunks; ++i, o += size) {
    chunks[i] = str.substr(o, size)
  }

  return chunks
}


click_button.addEventListener('click', function() {
    canvas.getContext('2d').drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/png');
    // console.log(image_data_url)
    
    canvas.getContext('2d').fillStyle = 'black';
    canvas.getContext('2d').fillRect(0, 0, canvas.width, canvas.height);
    let selected_boundary = boundary.value;
    if (selected_boundary == "None"){
      alert("wrong boundary")
    }else{
      let array = split(image_data_url, 65000);
      // let array = [image_data_url]
      array.push("stop"+selected_boundary)
      // console.log(array.length)



      array.forEach(element => {fetch('http://localhost:3000', {
        method: 'POST',
        body: JSON.stringify({"Data": element}),
        headers: {'Content-Type': 'application/json'},
        }).then((dat) => { return dat.json()})
          .then((stuff) => {
            if (stuff.wow === "done"){
            fetch('http://localhost:3000')
            .then(res => {return res.json()})
            .then(dat => {
              let temp = JSON.parse(dat).a;
              if (temp === 1){
                result.innerText = "result: "+ "over the age boundary";
              }else if(temp === 0){
                result.innerText = "result: "+ "under the age boundary";
              }else{
                result.innerText = "result: "+ temp;
              }
            })
            .catch(err => {console.error('Error: ', err)})
            }
          })    
          // 
        
        })

      result.innerText = "result: processing";
    }
    //wait till the keyword arrives
    //then fetch post arrives on the backend too slow
    
    
    // take data from promise and update website

    })
