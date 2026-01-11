const form = document.getElementById('chat-form');
const input = document.getElementById('input');
const messages = document.getElementById('messages');


form.onsubmit = async (e) => {
e.preventDefault();


const text = input.value;
input.value = '';


messages.innerHTML += `<div class="user">${text}</div>`;
const bot = document.createElement('div');
bot.className = 'bot';
messages.appendChild(bot);


try {
const res = await fetch('/chat', {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ message: text })
});


if (!res.ok) {
throw new Error(`Server error: ${res.statusText}`);
}


const reader = res.body.getReader();
const decoder = new TextDecoder();


while (true) {
const { value, done } = await reader.read();
if (done) break;
const chunk = decoder.decode(value);
const match = chunk.match(/"token":"(.*?)"/);
if (match) bot.textContent += match[1];
}
} catch (error) {
bot.textContent = "Error: Unable to reach the model server. Please try again later.";
console.error("Fetch error:", error);
}
};