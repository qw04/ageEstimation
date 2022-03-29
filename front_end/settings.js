boundaryRequest = document.querySelector('#boundaryRequest');
for (var i = 1; i <= 110; i++) {
  const option = document.createElement('option');
  option.value = i;
  option.text = i;
  boundaryRequest.appendChild(option);
}
