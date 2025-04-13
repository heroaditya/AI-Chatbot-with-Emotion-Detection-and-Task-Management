// Toggle Dark/Light Mode
document.getElementById('mode-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    const modeText = document.body.classList.contains('dark-mode') ? '☀️ Light Mode' : '🌙 Dark Mode';
    this.textContent = modeText;
  });
  
  // Chat Form Submission
  document.getElementById('chat-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const userInput = document.getElementById('user-input').value.trim();
    if (!userInput) return;
  
    // Append User Message
    appendMessage('user', userInput);
  
    // Clear Input
    document.getElementById('user-input').value = '';
  
    try {
      // Send message to backend
      const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
      });
  
      const result = await response.json();
      appendMessage('bot', result.response);
    } catch (error) {
      appendMessage('bot', '⚠️ Something went wrong. Please try again.');
    }
  });
  
  // Append Messages to Chat
  function appendMessage(type, text) {
    const chatContainer = document.getElementById('chat-container');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', type);
    messageDiv.innerHTML = `<p>${text}</p>`;
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
  }
  