import streamlit as st

st.set_page_config(page_title="My Valentine 💖", layout="wide")

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
    background: #ff2d55;
    color: white;
}

.no {
    background: white;
    color: #ff2d55;
}

.heart {
    position: fixed;
    font-size: 32px;
    animation: float 6s linear infinite;
    pointer-events: none;
}

@keyframes float {
    0% { transform: translateY(100vh) scale(0.6); opacity: 0; }
    50% { opacity: 1; }
    100% { transform: translateY(-10vh) scale(1.4); opacity: 0; }
}

.love-eyes {
    font-size: 100px;
    animation: shake 0.6s infinite;
}

@keyframes shake {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(10deg); }
    50% { transform: rotate(0deg); }
    75% { transform: rotate(-10deg); }
    100% { transform: rotate(0deg); }
}

.popup {
    position: fixed;
    bottom: 15%;
    background: white;
    color: #ff2d55;
    padding: 20px 30px;
    border-radius: 20px;
    font-size: 1.3em;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    animation: pop 0.4s ease;
}

@keyframes pop {
    0% { transform: scale(0.7); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}

.hidden {
    display: none;
}
</style>

<div class="center" id="main">
    <h1>💖 Hey My Love 💖</h1>
    <div class="question">
        Will you be my lifetime Valentine? ❤️
    </div>
    <div>
        <button class="yes" onclick="yesClicked()">YES 💘</button>
        <button class="no" onclick="noClicked()">NO 🙄</button>
    </div>
</div>

<div class="center hidden" id="yesScreen">
    <div class="love-eyes">😍</div>
    <h1>I knew it!!! 💖</h1>
    <h2>You are forever mine 💍</h2>
</div>

<div id="popup" class="popup hidden">
    Nice try 😏 But you’re already mine ❤️ <br>
    Now click YES like a good Valentine 💘
</div>

<script>
const hearts = ["❤️","💖","💘","💕","💞","💓"];

function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (4 + Math.random() * 3) + "s";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 7000);
}
setInterval(createHeart, 250);

function yesClicked() {
    document.getElementById("main").classList.add("hidden");
    document.getElementById("yesScreen").classList.remove("hidden");

    for (let i = 0; i < 30; i++) {
        setTimeout(createHeart, i * 100);
    }
}

function noClicked() {
    const popup = document.getElementById("popup");
    popup.classList.remove("hidden");

    setTimeout(() => {
        popup.classList.add("hidden");
    }, 2500);
}
</script>
"""

st.components.v1.html(html_code, height=900)
