from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
messages = [
    {"role": "system", "content": "You are an intelligent an polite AI assistant"}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ['bye', 'exit']:
        print("Assistant: Goodbye")
        break 

    if not user_input.strip():
        continue

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=messages,
            temperature=0.7,
            max_tokens=50
        )

        reply = response.choices[0].message.content

        print(f"\nAssistant: {reply}\n")

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
