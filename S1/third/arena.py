from common.helper import client, MODEL


def battle(prompt):
    msgs = [{"role": "user", "content": prompt}]

    # Model A — OpenAI's GPT
    a = client.chat.completions.create(model=MODEL1, messages=msgs)

    # Model B — Llama on Groq (same code, different brain!)
    b = client.chat.completions.create(model=MODEL2, messages=msgs)

    return a.choices[0].message.content, b.choices[0].message.content
# …now we wrap this in Gradio with two columns + thumbs up/down 👇