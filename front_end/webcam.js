var video = document.querySelector("#videoElement");

// if (navigator.mediaDevices.getUserMedia) {
//   navigator.mediaDevices.getUserMedia({ video: true })

//       .then(function (stream) {
//       video.srcObject = stream;
//     }).catch(function (err0r) {
//       alert("Something went wrong, reload webpage!");
//     });
// }


navigator.mediaDevices.enumerateDevices()
.then(function(devices) {
  array = [];
  devices.forEach(function(device) {
    if (device.kind === "videoinput"){
      array.push([device.deviceId,device.label]);
    };
    console.log(array);
  }
  )
}).catch(function(err) {
  alert(err.name + ": " + err.message);
});