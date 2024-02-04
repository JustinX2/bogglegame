document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('submit-form');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const wordInput = document.getElementById('word-input');
        const word = wordInput.value;

        try {
            const response = await axios.get('/check-word', { params: { word: word } });
            document.getElementById('result').innerText = response.data.result;
        } catch (error) {
            console.error('Error checking word:', error);
        }
    });
});
