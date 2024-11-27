
document.getElementById('password-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const password = document.getElementById('password').value;

    fetch('/check_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ password })
    })
    .then(response => response.json())
    .then(data => {
        let resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `
            <p>Strength: ${data.strength}</p>
            ${data.feedback.map(item => `<p>${item}</p>`).join('')}
        `;
    });
});