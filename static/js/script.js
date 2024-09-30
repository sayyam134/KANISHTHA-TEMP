document.getElementById("generateMusicBtn").addEventListener("click", () => {
    const text = document.getElementById("inputText").value;

    // Send the text to the back-end API
    fetch('/generate-music', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.downloadUrl) {
            document.getElementById("responseMessage").innerHTML = `<a href="${data.downloadUrl}" download>Download the generated music here</a>`;
        } else {
            document.getElementById("responseMessage").textContent = "Error generating music!";
        }
    })
    .catch(error => {
        document.getElementById("responseMessage").textContent = "Error generating music!";
        console.error('Error:', error);
    });
});
