from openai import OpenAI

client = OpenAI(
    api_key= "YOUR_API_KEY"
)

command = '''
YOUR_PREVIOUS_CHAT_HISTORY

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "YOUR_SYSTEM_PROMPT"},
        {"role": "user", "content": "command"}
    ]
)

print(completion.choices[0].message.content)