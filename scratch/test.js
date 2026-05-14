const url = 'https://script.google.com/macros/s/AKfycbwpWPcO5rDCNAR37nuftSFDTdowAMFff0ULhbUvm_8107L_agTUj1rmcOpU2y_wKnX-/exec';
fetch(url, {
    method: 'POST',
    headers: {'Content-Type': 'text/plain;charset=utf-8'},
    body: JSON.stringify({name: 'Test', rating: 5, text: 'Test', date: '14. 5. 2026'})
})
.then(res => res.text())
.then(text => console.log('Response:', text))
.catch(err => console.error('Error:', err));
