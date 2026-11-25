
# Autonomous SOC Security Agent

An AI-powered cybersecurity investigation application built using Python, Google Gemini API, and Flask.

The project demonstrates how an AI agent can investigate suspicious login alerts, select relevant Python tools, analyze returned evidence, and generate a security investigation report.

## Project Objective

To demonstrate an AI agent that can investigate cybersecurity alerts with minimal human supervision using LLM reasoning and dynamic function calling.

## Features

- AI-powered security alert investigation.
- Dynamic tool selection using Gemini function calling.
- Simulated IP intelligence lookup.
- Login activity and failed-attempt analysis.
- Evidence-based risk assessment.
- Defensive security recommendations.
- Flask web dashboard.
- Duplicate tool-call protection.
- Bounded investigation loop.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Google Gemini API | AI reasoning and tool selection |
| Google Gen AI SDK | Gemini integration |
| Flask | Web dashboard |
| python-dotenv | Environment variable management |

## Project Structure

```text
xiarch-agent/
├── agent.py
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── tools/
    ├── __init__.py
    ├── ip_lookup.py
    └── log_analyzer.py
```

## How It Works

1. The user submits a suspicious security alert.
2. Gemini analyzes the alert and decides which tools are useful.
3. Python executes the selected investigation tools.
4. Tool results are returned to Gemini.
5. Gemini reasons over the collected evidence.
6. The final investigation report is displayed on the Flask dashboard.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shanyamkumar9430/xiarch-agent.git
cd xiarch-agent
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows, activate using:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Open `.env` and add your own Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Never upload your actual `.env` file or share your API key publicly.

### 5. Run the application

```bash
python app.py
```

Open your browser:

http://127.0.0.1:5000

## Sample Security Alert

```text
Suspicious login activity detected.

Username: admin
Source IP: 185.220.101.1
Alert: Multiple failed login attempts.
```

Submit this alert through the dashboard to test the investigation.

## Security and Limitations

- IP intelligence and login events use simulated databases.
- No live threat intelligence service is currently connected.
- The agent performs read-only investigations.
- It does not block IP addresses or modify firewall configurations.
- AI-generated risk assessments are advisory and require human review.
- The sample data does not establish that an attack was successful.
- API credentials must remain private.

## Future Improvements

- Integration with live threat intelligence APIs.
- Real security log integration.
- Additional investigation tools.
- Investigation history and report downloads.
- Human approval for defensive actions.

## Project Purpose

Developed as a practical demonstration for the Agentic AI Engineer Intern recruitment assessment at Xiarch Bharat Pvt. Ltd.

The project demonstrates LLM-based reasoning, dynamic function calling, Python tool integration, and AI-assisted cybersecurity investigation.
