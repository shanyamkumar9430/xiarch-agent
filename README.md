
# Autonomous SOC Security Agent

An AI-powered cybersecurity investigation project built using Python, Google Gemini API, and Flask.

The application demonstrates how an AI agent can investigate suspicious login alerts by reasoning about the alert, selecting suitable tools, analyzing evidence, and generating a security report.

## Project Objective

The objective is to develop an autonomous AI agent that can investigate cybersecurity alerts with minimal human supervision.

The agent uses Gemini function calling to select and execute Python investigation tools dynamically.

## Features

- AI-based security alert investigation.
- Dynamic tool selection using Gemini function calling.
- Simulated IP address intelligence lookup.
- Login activity analysis.
- Evidence-based risk assessment.
- Security recommendations.
- Flask web dashboard.
- Duplicate tool-call protection.
- Limited investigation steps to avoid endless execution.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Google Gemini API | AI reasoning and tool selection |
| Google Gen AI SDK | Gemini integration |
| Flask | Web dashboard |
| python-dotenv | API key management |

## Project Structure

```text
xiarch-agent/
|
|-- agent.py
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- tools/
    |-- __init__.py
    |-- ip_lookup.py
    |-- log_analyzer.py
```

## How It Works

1. A user submits a suspicious security alert.
2. Gemini analyzes the alert and decides which tools are useful.
3. Python executes the selected investigation tools.
4. Tool results are returned to Gemini.
5. Gemini analyzes the collected evidence.
6. The final investigation report appears on the dashboard.

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd xiarch-agent
```

Replace the placeholder with the actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project directory and add:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own API key.

Never upload the `.env` file or share your API key publicly.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Sample Security Alert

```text
Suspicious login activity detected.

Username: admin
Source IP: 185.220.101.1
Alert: Multiple failed login attempts.
```

Submit this alert through the dashboard to test the investigation.

## Security and Limitations

- IP intelligence and login events currently use simulated databases.
- The project does not connect to live threat intelligence services.
- The agent performs read-only investigations.
- It does not block IP addresses or modify security configurations.
- AI-generated risk assessments are recommendations and require human review.
- API credentials must remain private.

## Future Improvements

- Integration with live threat intelligence APIs.
- Real security log integration.
- Additional investigation tools.
- Investigation history and report downloads.
- Human approval for defensive actions.

## Project Purpose

Developed as a practical demonstration for the Agentic AI Engineer Intern recruitment assessment at Xiarch Bharat Pvt. Ltd.

The project demonstrates autonomous AI reasoning, function calling, Python tool integration, and cybersecurity investigation.
