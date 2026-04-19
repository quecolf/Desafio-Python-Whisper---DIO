import os
os.environ['OPENAI_API_KEY'] = 'SUA_CHAVE'

from openai import OpenAI

client = OpenAI(api_key="SUA_CHAVE")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente que resume áudios de forma clara."
        },
        {
            "role": "user",
            "content": f"Resuma o texto:\n\n{transcription}"
        }
    ]
)

summary = response.choices[0].message.content
print(summary)