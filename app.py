from flask import Flask, render_template_string, request
import html

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>XSS Lab</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #0f172a; color: #f8fafc; }
        .container { max-width: 600px; margin: auto; background: #1e293b; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        input[type="text"] { width: 70%; padding: 10px; margin-right: 10px; background: #0f172a; border: 1px solid #475569; color: white; border-radius: 4px; }
        button { padding: 10px 20px; background: #3b82f6; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #2563eb; }
        .result { margin-top: 20px; padding: 15px; background: #334155; border-radius: 4px; }
        a { color: #60a5fa; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h2>XSS Testing Laboratory</h2>
        <p>Current Mode: <strong>{{ mode }}</strong></p>
        <p><a href="/vulnerable">Switch to Vulnerable</a> | <a href="/protected">Switch to Protected</a></p>
        
        <form method="POST">
            <input type="text" name="payload" placeholder="Enter payload, e.g. &lt;script&gt;alert(1)&lt;/script&gt;" required>
            <button type="submit">Submit</button>
        </form>

        {% if payload is not none %}
        <div class="result">
            <h3>Result Output:</h3>
            <div>{{ output_payload | safe }}</div>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template_string(HTML_TEMPLATE, mode="Home", payload=None, output_payload="")

@app.route("/vulnerable", methods=["GET", "POST"])
def vulnerable():
    payload = None
    output_payload = ""
    if request.method == "POST":
        payload = request.form.get("payload", "")
        output_payload = payload
    return render_template_string(HTML_TEMPLATE, mode="Vulnerable (Unfiltered)", payload=payload, output_payload=output_payload)

@app.route("/protected", methods=["GET", "POST"])
def protected():
    payload = None
    output_payload = ""
    if request.method == "POST":
        payload = request.form.get("payload", "")
        output_payload = html.escape(payload)
    return render_template_string(HTML_TEMPLATE, mode="Protected (Sanitized)", payload=payload, output_payload=output_payload)

if __name__ == "__main__":
    app.run(debug=True, port=5000)