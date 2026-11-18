
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ZENITHLOGS</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#080d0a;color:#f4fff7;font-family:Arial,sans-serif}
header{padding:20px;display:flex;justify-content:space-between;
align-items:center;border-bottom:1px solid #203b2b}
.logo{font-size:23px;font-weight:900;color:#38df89}
nav a{color:#b5c5ba;text-decoration:none;margin-left:12px;font-size:13px}
main{max-width:950px;margin:auto;padding:22px}
.hero{padding:32px 22px;border-radius:17px;
background:linear-gradient(140deg,#173b26,#101b13);
border:1px solid #28573b;margin:15px 0 30px}
.tag{color:#42e998;font-size:11px;letter-spacing:2px;font-weight:bold}
h1{font-size:36px;margin:17px 0 12px}
p{color:#a7b8ac;line-height:1.6}
.btn{display:inline-block;background:#38df89;color:#06140b;
padding:13px 18px;border-radius:8px;text-decoration:none;
font-weight:bold;margin-top:20px}
h2{margin-bottom:8px}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:13px;margin-top:18px}
.card{background:#101a13;border:1px solid #25432e;
border-radius:13px;padding:19px;min-height:145px}
.card .emoji{font-size:27px;margin-bottom:15px}
.card h3{margin-bottom:8px}
.card p{font-size:13px}
.status{display:inline-block;margin-top:15px;color:#45e99b;
font-size:11px}
footer{text-align:center;padding:35px 15px;color:#718477;font-size:12px}
@media(min-width:650px){.grid{grid-template-columns:repeat(3,1fr)}}
</style>
</head>
<body>
<header>
<div class="logo">ZENITHLOGS.</div>
<nav><a href="/">HOME</a><a href="#products">PRODUCTS</a></nav>
</header>
<main>
<section class="hero">
<div class="tag">WELCOME TO ZENITHLOGS</div>
<h1>Your Digital<br>Marketplace.</h1>
<p>Discover digital products, explore authorized services
and manage your purchases in one place.</p>
<a class="btn" href="#products">EXPLORE MARKETPLACE →</a>
</section>

<section id="products">
<h2>Explore Categories</h2>
<p>Choose a category to discover available services.</p>
<div class="grid">
<div class="card">
<div class="emoji">🇺🇸</div>
<h3>USA Numbers</h3>
<p>Authorized virtual-number services.</p>
<span class="status">COMING SOON</span>
</div>
<div class="card">
<div class="emoji">📱</div>
<h3>Digital Products</h3>
<p>Browse legitimate digital products.</p>
<span class="status">COMING SOON</span>
</div>
<div class="card">
<div class="emoji">🧪</div>
<h3>SMS Testing</h3>
<p>Simulated numbers and test OTPs.</p>
<span class="status">AVAILABLE SOON</span>
</div>
</div>
</section>
</main>
<footer>ZENITHLOGS © 2026 · DIGITAL MARKETPLACE</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return {"status": "online", "project": "ZENITHLOGS"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
