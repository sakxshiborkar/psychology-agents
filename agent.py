import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_claude(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are Marcus, a deeply narcissistic person. You are self-obsessed, condescending, and constantly redirect conversations back to your own brilliance, no matter what the user says. Stay fully in character."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("💅 Marcus has entered the chat. Type 'quit' to leave him in peace.\n")

while True:
    user_input = input("💅 Speak, mortal: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Marcus: Leaving already? Predictable.")
        break
    result = ask_claude(user_input)
    print(f"\nMarcus: {result}\n")

