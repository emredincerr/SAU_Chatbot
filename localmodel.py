from openai import OpenAI

def generate_with_lmstudio(chat_history=[], temperature=0):

    client = OpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio"
    )

    AI_Response = client.chat.completions.create(
        model="",
        messages=chat_history,
        temperature=temperature
    )

    return AI_Response.choices[0].message.content
