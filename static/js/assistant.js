// ===============================
// ELEMENTS
// ===============================

const chatToggle = document.getElementById("chat-toggle");
const chatWindow = document.getElementById("chat-window");
const closeChat = document.getElementById("close-chat");

const sendBtn = document.getElementById("send-btn");
const chatInput = document.getElementById("chat-input");
const chatMessages = document.getElementById("chat-messages");


// ===============================
// OPEN CHAT
// ===============================

chatToggle.onclick = function () {

    chatWindow.style.display = "flex";

};


// ===============================
// CLOSE CHAT
// ===============================

closeChat.onclick = function () {

    chatWindow.style.display = "none";

};


// ===============================
// SEND MESSAGE
// ===============================

function sendMessage() {

    const message = chatInput.value.trim();

    if (message === "") return;


    // ---------------------------
    // USER MESSAGE
    // ---------------------------

    const userMessage = document.createElement("div");

    userMessage.className = "user-message";

    userMessage.innerHTML = message;

    chatMessages.appendChild(userMessage);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    chatInput.value = "";


    // ---------------------------
    // TYPING ANIMATION
    // ---------------------------

    const typing = document.createElement("div");

    typing.className = "bot-message";

    typing.innerHTML = "🤖 Typing...";

    chatMessages.appendChild(typing);

    chatMessages.scrollTop = chatMessages.scrollHeight;


    // ---------------------------
    // SEND TO FLASK
    // ---------------------------

    fetch("/assistant_chat", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            message: message

        })

    })

    .then(response => response.json())

    .then(data => {

        setTimeout(() => {

            typing.remove();

            const botMessage = document.createElement("div");

            botMessage.className = "bot-message";

            botMessage.innerHTML = data.reply;

            chatMessages.appendChild(botMessage);

            chatMessages.scrollTop = chatMessages.scrollHeight;

        }, 1000);

    })

    .catch(error => {

        typing.remove();

        const botMessage = document.createElement("div");

        botMessage.className = "bot-message";

        botMessage.innerHTML =

            "⚠ Sorry! Something went wrong.";

        chatMessages.appendChild(botMessage);

        console.log(error);

    });

}


// ===============================
// BUTTON CLICK
// ===============================

sendBtn.addEventListener("click", sendMessage);


// ===============================
// PRESS ENTER
// ===============================

chatInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});


// ===============================
// QUICK QUESTION CARDS
// ===============================

const questionCards = document.querySelectorAll(".question-card");

questionCards.forEach(card => {

    card.addEventListener("click", function () {

        chatWindow.style.display = "flex";

        chatInput.value = this.innerText;

        sendMessage();

    });

});