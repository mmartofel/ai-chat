// AI Chat Application
const messagesDiv = document.getElementById('messages');
const form = document.getElementById('chat-form');
const input = document.getElementById('input');

/**
 * Add a message to the chat display
 * @param {string} content - The message content
 * @param {string} sender - The sender ('user', 'bot', or 'error')
 * @param {boolean} isMarkdown - Whether to render as markdown
 */
function addMessage(content, sender, isMarkdown = false) {
  const messageDiv = document.createElement('div');
  messageDiv.className = sender;
  
  if (isMarkdown) {
    messageDiv.innerHTML = marked.parse(content);
  } else {
    messageDiv.textContent = content;
  }
  
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

/**
 * Handle form submission and send message to server
 */
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const userMessage = input.value.trim();
  
  if (!userMessage) return;

  addMessage(userMessage, 'user');
  input.value = '';

  // Stream response from server
  const eventSource = new EventSource(`/chat?message=${encodeURIComponent(userMessage)}`);
  let botMessageContent = '';
  let botMessageDiv = null;
  let errorOccurred = false;

  eventSource.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      
      if (data.error) {
        // Only show error if no content has been received yet
        if (!botMessageContent) {
          addMessage(`Error: ${data.error}`, 'error');
          errorOccurred = true;
        }
        eventSource.close();
      } else if (data.message && data.message.content) {
        // Clear error flag once content starts streaming
        errorOccurred = false;
        botMessageContent += data.message.content;
        
        if (!botMessageDiv) {
          botMessageDiv = document.createElement('div');
          botMessageDiv.className = 'bot';
          messagesDiv.appendChild(botMessageDiv);
        }
        
        botMessageDiv.innerHTML = marked.parse(botMessageContent);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
      } else if (data.done) {
        botMessageContent = '';
        botMessageDiv = null;
        eventSource.close();
      }
    } catch (e) {
      if (!botMessageContent) {
        addMessage('Error: Invalid response from server.', 'error');
        errorOccurred = true;
      }
      eventSource.close();
    }
  };

  eventSource.onerror = () => {
    if (!errorOccurred && !botMessageContent) {
      addMessage('Error: Unable to connect to the server. Please try again later.', 'error');
    }
    eventSource.close();
  };
});