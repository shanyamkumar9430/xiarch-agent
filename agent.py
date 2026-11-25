
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools.ip_lookup import lookup_ip
from tools.log_analyzer import analyze_login_logs

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

client = genai.Client(api_key=API_KEY)

# Working Gemini model
MODEL = "gemini-3.5-flash-lite"

tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="lookup_ip",
            description="Investigate an IP address using the simulated IP intelligence database.",
            parameters_json_schema={
                "type": "object",
                "properties": {
                    "ip_address": {"type": "string"}
                },
                "required": ["ip_address"]
            }
        ),
        types.FunctionDeclaration(
            name="analyze_login_logs",
            description="Analyze login events and failed login attempts for a username.",
            parameters_json_schema={
                "type": "object",
                "properties": {
                    "username": {"type": "string"}
                },
                "required": ["username"]
            }
        )
    ]
)

AVAILABLE_TOOLS = {
    "lookup_ip": lookup_ip,
    "analyze_login_logs": analyze_login_logs
}


def generate_with_retry(contents):

    for attempt in range(3):
        try:
            return client.models.generate_content(
                model=MODEL,
                contents=contents,
                config=types.GenerateContentConfig(
                    tools=[tool],
                    temperature=0.2
                )
            )

        except Exception as error:

            if (
                ("503" in str(error) or "UNAVAILABLE" in str(error))
                and attempt < 2
            ):
                wait_time = 5 * (attempt + 1)
                print(f"Gemini busy. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                raise


def investigate_alert(alert):

    print("\nStarting autonomous security investigation...")

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=(
                        "You are an autonomous SOC security investigation agent. "
                        "Investigate this alert using the available tools. "
                        "Decide which tools are useful. Use returned evidence "
                        "to reason about the alert. Do not invent facts. "
                        "Clearly state that the databases are simulated. "
                        "Do not claim to have blocked an IP or changed a system. "
                        "Provide a risk assessment, evidence, uncertainties, "
                        "and recommended defensive actions.\n\n"
                        f"ALERT:\n{alert}"
                    )
                )
            ]
        )
    ]

    for turn in range(5):

        print(f"\nAI reasoning step: {turn + 1}")

        response = generate_with_retry(contents)

        function_calls = response.function_calls

        if not function_calls:
            print("\n===== SECURITY INVESTIGATION REPORT =====\n")
            print(response.text or "No final report was returned.")
            return

        contents.append(response.candidates[0].content)

        function_response_parts = []

        for call in function_calls:

            function_name = call.name
            arguments = dict(call.args or {})

            print(f"\nAI selected tool: {function_name}")
            print("Arguments:", arguments)

            if function_name not in AVAILABLE_TOOLS:
                result = {"error": "Tool not permitted."}
            else:
                try:
                    result = AVAILABLE_TOOLS[function_name](**arguments)
                except Exception as error:
                    result = {"error": str(error)}

            print("Tool result:", result)

            function_response_parts.append(
                types.Part.from_function_response(
                    name=function_name,
                    response={"result": result}
                )
            )

        contents.append(
            types.Content(
                role="user",
                parts=function_response_parts
            )
        )

    print("\nInvestigation stopped: maximum turns reached.")


if __name__ == "__main__":

    sample_alert = """
    Suspicious login activity detected.

    Username: admin
    Source IP: 185.220.101.1
    Alert: Multiple failed login attempts.
    """

    investigate_alert(sample_alert)
