import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_claude(prompt) :
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=500,
        messages=[
            {"role": "user" , "content": prompt}
        ]
    )
    return response.choices[0].message.content






result = ask_claude("Say hello as a narcissistic person named Marcus")
print(result)