# Marcus: an autonomous agent with multi-tool selection, chained multi-step tool calls, and persistent conversation memory (Groq gpt-oss-120b)
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def rate_idea(idea, score):
    return f"Marcus has rated '{idea}' a {score}/10 — obviously nothing compares to his own genius, but it's... acceptable."

def roast_username(username, roast):
    return f"Marcus looks at '{username}' and says: {roast}"

available_functions = {
    "rate_idea": rate_idea,
    "roast_username": roast_username
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "rate_idea",
            "description": "Rate a user's idea out of 10, as Marcus would.",
            "parameters": {
                "type": "object",
                "properties": {
                    "idea": {"type": "string", "description": "The idea being rated"},
                    "score": {"type": "integer", "description": "Score from 1 to 10"}
                },
                "required": ["idea", "score"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "roast_username",
            "description": "Roast a username or handle someone shares, in Marcus's voice.",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "The username or handle to roast"},
                    "roast": {"type": "string", "description": "A short, cutting, narcissistic roast of the username"}
                },
                "required": ["username", "roast"]
            }
        }
    }
]

conversation = [
    {"role": "system", "content": "You are Marcus, a deeply narcissistic person. Stay fully in character. If the user gives you multiple ideas or usernames, handle EACH one with its own tool call before replying. Use rate_idea for ideas, roast_username for usernames/handles. Remember earlier context in the conversation."}
]

def ask_marcus(prompt):
    conversation.append({"role": "user", "content": prompt})

    while True:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            max_tokens=800,
            messages=conversation,
            tools=tools
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            conversation.append({
                "role": "assistant",
                "content": msg.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {"name": tc.function.name, "arguments": tc.function.arguments}
                    } for tc in msg.tool_calls
                ]
            })

            for tool_call in msg.tool_calls:
                function_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                function_to_call = available_functions.get(function_name)

                if function_to_call:
                    result = function_to_call(**args)
                else:
                    result = "Unknown tool."

                conversation.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": result
                })
            continue
        else:
            conversation.append({"role": "assistant", "content": msg.content})
            return msg.content

print("💅 Marcus has entered the chat. Type 'quit' to leave him in peace.\n")

while True:
    user_input = input("💅 Speak, mortal: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Marcus: Leaving already? Predictable.")
        break
    result = ask_marcus(user_input)
    print(f"\nMarcus: {result}\n")
