from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Valentine 💖</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            overflow: hidden;
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: #fff;
        }

        h1 {
            font-size: 3em;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }

        .question {
            margin-top: 20px;
            font-size: 2em;
            font-weight: bold;
        }

        .heart {
            position: absolute;
            font-size: 24px;
            animation: floatUp 6s linear infinite;
        }

        @keyframes floatUp {
            0% {
                transform: translateY(100vh) scale(0.5);
                opacity: 0;
            }
            50% {
                opacity: 1;
            }
            100% {
                transform: translateY(-10vh) scale(1.2);
                opacity: 0;
            }
        }

        .quote {
            position: absolute;
            bottom: 20%;
            font-size: 1.5em;
            opacity: 0;
            animation: fadeQuote 6s infinite;
        }

        @keyframes fadeQuote {
            0% { opacity: 0; }
            20% { opacity: 1; }
            80% { opacity: 1; }
            100% { opacity: 0; }
        }
    </style>
</head>
<body>

<div>
    <h1>💘 My Love 💘</h1>
    <div class="question">Will you be my Valentine for a lifetime? ❤️</div>
</div>

<div id="quote" class="quote"></div>

<script>
    const hearts = ["❤️","💖","💘","💕","💞","💓"];
    const quotes = [
        "You are my today and all of my tomorrows 💕",
        "Every love story is beautiful, but ours is my favorite 💖",
        "I choose you. And I’ll choose you every single day ❤️",
        "Forever is a long time, but I wouldn’t mind spending it with you 💘"
    ];

    function createHeart() {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerText = hearts[Math.floor(Math.random() * hearts.length)];
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (4 + Math.random() * 4) + "s";
        document.body.appendChild(heart);

        setTimeout(() => heart.remove(), 8000);
    }

    setInterval(createHeart, 300);

    let quoteIndex = 0;
    const quoteDiv = document.getElementById("quote");

    function showQuote() {
        quoteDiv.innerText = quotes[quoteIndex];
        quoteIndex = (quoteIndex + 1) % quotes.length;
    }

    setInterval(showQuote, 6000);
    showQuote();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)