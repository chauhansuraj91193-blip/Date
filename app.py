import streamlit as st

st.set_page_config(page_title="Kehkasha 💖", layout="wide")

html_code = """
<style>
body {
    margin: 0;
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

.center {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    text-align: center;
    position: relative;
    z-index: 2;
}

h1 {
    font-size: 3.2em;
    text-shadow: 2px 2px 15px rgba(0,0,0,0.3);
}

.question {
    font-size: 2em;
    margin-bottom: 30px;
}

button {
    padding: 15px 40px;
    font-size: 1.2em;
    border-radius: 30px;
    border: none;
    cursor: pointer;
    margin: 10px;
}

.yes {
    background: #ff1e56;
    color: white;
}

.no {
    background: white;
    color: #ff1e56;
}

/* ❤️ HEART ANIMATION */
.heart {
    position: fixed;
    bottom: -50px;
    font-size: 42px;
    color: red;
    animation: floatUp 6s linear forwards;
    pointer-events: none;
    z-index: 1;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) scale(0.8);
        opacity: 0;
    }
    20% { opacity: 1; }
    100% {
        transform: translateY(-120vh) scale(1.6);
        opacity: 0;
    }
}

/* 😍 Love eyes */
.love-eyes {
    font-size: 110px;
    animation: shake 0.6s infinite;
}

@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(10deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(-10deg); }
    100% { transform: rotate(0deg); }
}

/* Popup */
.popup {
    position: fixed;
    bottom: 15%;
    background: white;
    color: #ff1e56;
    padding: 20px 30px;
    border-radius: 20px;
    font-size: 1.3em;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    animation: pop 0.4s ease;
    z-index: 3;
    text-align: center;
}

@keyframes pop {
    0% { transform: scale(0.7); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

.hidden {
    display: none;
}

/* 🎉 Confetti */
.confetti {
    position: fixed;
    width: 10px;
    height: 10px;
    animation: confetti-fall 4s linear forwards;
    z-index: 3;
}

@keyframes confetti-fall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
}
</style>

<div class="center" id="main">
    <h1>💖 Kehkasha 💖</h1>
    <div class="question">
      ❤️ Will you be my forever Valentine? ❤️
    </div>
    <div>
        <button class="yes" onclick="yesClicked()">YES 💘</button>
        <button class="no" onclick="noClicked()">NO 🙄</button>
    </div>
</div>

<div class="center hidden" id="yesScreen">
    <div class="love-eyes">😍</div>
    <h1>Yayyy Kehkasha!!! 🎉💖</h1>
    <h2>Forever & Always 💍</h2>
</div>

<div id="popup" class="popup hidden">
    Nice try 😏 But you’re already mine ❤️ <br>
    Now click YES like a good Valentine 💘
</div>

<script>
const heartEmoji = "❤️";

/* Create 10–12 hearts from bottom */
function createHeartBatch() {
    const count = 10 + Math.floor(Math.random() * 3); // 10–12 hearts
    for (let i = 0; i < count; i++) {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = heartEmoji;
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (4 + Math.random() * 3) + "s";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 7000);
    }
}

/* Continuous hearts */
setInterval(createHeartBatch, 3000);

/* Confetti */
function createConfetti() {
    const confetti = document.createElement("div");
    confetti.className = "confetti";
    confetti.style.left = Math.random() * 100 + "vw";
    confetti.style.backgroundColor =
        ["#ff1e56","#ffd700","#00eaff","#ffffff"][Math.floor(Math.random()*4)];
    document.body.appendChild(confetti);
    setTimeout(() => confetti.remove(), 4000);
}

function yesClicked() {
    document.getElementById("main").classList.add("hidden");
    document.getElementById("yesScreen").classList.remove("hidden");

    for (let i = 0; i < 40; i++) {
        setTimeout(createHeartBatch, i * 150);
        setTimeout(createConfetti, i * 100);
    }
}

function noClicked() {
    const popup = document.getElementById("popup");
    popup.classList.remove("hidden");
    setTimeout(() => popup.classList.add("hidden"), 2500);
}
</script>
"""

st.components.v1.html(html_code, height=950)
