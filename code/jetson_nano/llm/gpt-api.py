from openai import OpenAI

client = OpenAI(
    api_key="YOUR API KEY",
    base_url="https://api.chatanywhere.tech/v1"
)


def gpt_35_api(messages: list):
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)


def gpt_35_api_stream(messages: list):
    stream = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

if __name__ == '__main__':
    messages = [{'role': 'user','content': ''},]
    gpt_35_api_stream(messages)