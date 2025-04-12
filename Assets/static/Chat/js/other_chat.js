document.addEventListener("DOMContentLoaded", () => {
  // Initialize Firebase
  const firebaseConfig = JSON.parse(
    document.getElementById("firebase-config").textContent
  );
  firebase.initializeApp(firebaseConfig);
  const database = firebase.database();
  const messagesRef = database.ref("messages/general_chat"); // Replace 'general_chat' with your chat ID

  const messageInput = document.getElementById("message-input");
  const sendButton = document.getElementById("send-button");
  const chatMessagesDiv = document.getElementById("chat-messages");
  const userId = "{{ user_id }}"; // Get the user ID from the Django context

  sendButton.addEventListener("click", sendMessage);
  messageInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

  // Function to send a message
  function sendMessage() {
    const messageText = messageInput.value.trim();
    if (messageText) {
      const newMessage = {
        sender_uid: userId,
        text: messageText,
        timestamp: firebase.database.ServerValue.TIMESTAMP,
      };
      messagesRef.push(newMessage);
      messageInput.value = "";
    }
  }

  // Function to listen for new messages
  messagesRef.on("child_added", (snapshot) => {
    const message = snapshot.val();
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    if (message.sender_uid === userId) {
      messageDiv.classList.add("sent");
      messageDiv.textContent = `You: ${message.text}`;
    } else {
      messageDiv.classList.add("received");
      messageDiv.textContent = `Other: ${message.text}`;
    }
    chatMessagesDiv.appendChild(messageDiv);
    chatMessagesDiv.scrollTop = chatMessagesDiv.scrollHeight; // Scroll to the bottom
  });
});
