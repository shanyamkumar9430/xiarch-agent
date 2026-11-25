
from flask import Flask, request, render_template_string
from contextlib import redirect_stdout
from io import StringIO

from agent import investigate_alert

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Autonomous SOC Security Agent</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #0b1120;
            color: #e5e7eb;
        }

        header {
            background: #111827;
            padding: 25px 8%;
            border-bottom: 1px solid #263247;
        }

        header h1 {
            margin: 0;
            color: #60a5fa;
            font-size: 25px;
        }

        header p {
            color: #9ca3af;
            margin-bottom: 0;
        }

        main {
            max-width: 950px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .panel {
            background: #111827;
            border: 1px solid #263247;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
        }

        h2 {
            margin-top: 0;
            color: #f9fafb;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }

        textarea {
            width: 100%;
            min-height: 160px;
            padding: 15px;
            border: 1px solid #374151;
            border-radius: 8px;
            background: #080f1e;
            color: white;
            font-size: 15px;
            resize: vertical;
        }

        button {
            margin-top: 18px;
            padding: 13px 22px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        pre {
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            line-height: 1.6;
            color: #d1d5db;
            font-size: 14px;
            background: #080f1e;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }

        .status {
            color: #86efac;
            font-size: 13px;
        }

        footer {
            text-align: center;
            color: #6b7280;
            padding: 25px;
            font-size: 13px;
        }
    </style>
</head>

<body>

<header>
    <h1>Autonomous SOC Security Agent</h1>
    <p>AI-powered security alert investigation using Gemini</p>
</header>

<main>

    <section class="panel">
        <h2>Security Alert Investigation</h2>
        <p>Enter an alert for the AI agent to investigate.</p>

        <form method="POST">

            <label for="alert">Security Alert Details</label>

            <textarea
                id="alert"
                name="alert"
                placeholder="Enter username, source IP, and suspicious activity..."
                required>{{ alert }}</textarea>

            <button type="submit">Investigate Alert</button>

        </form>
    </section>

    {% if result %}
    <section class="panel">
        <h2>Investigation Results</h2>
        <p class="status">Investigation completed or returned an error</p>
        <pre>{{ result }}</pre>
    </section>
    {% endif %}

</main>

<footer>
    Educational demonstration | Uses simulated security databases
</footer>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    alert = ""

    if request.method == "POST":

        alert = request.form.get("alert", "").strip()

        if alert:

            output = StringIO()

            try:
                # Capture the agent's investigation output.
                with redirect_stdout(output):
                    investigate_alert(alert)

                result = output.getvalue()

            except Exception as error:
                result = output.getvalue()
                result += "\nInvestigation error: " + str(error)

    return render_template_string(
        HTML_PAGE,
        alert=alert,
        result=result
    )


if __name__ == "__main__":

    print("Starting Autonomous SOC Security Dashboard...")
    print("Open http://127.0.0.1:5000 in your browser")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
