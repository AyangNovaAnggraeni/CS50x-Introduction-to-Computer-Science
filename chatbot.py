import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"])

system_prompt = "You are a helpful assistant. Answer the user's questions to the best of your ability."

user_prompt = input("What is your question? ")

chat_completion = client.chat.completions.create(
    message=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    model="gpt-4o"
)

response_text = chat_completion.choices[0].message.content

print(response_text)
