import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

print("正在调用 Kimi API...")
response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{"role": "user", "content": "Hello, 请用一句话介绍 STM32"}],
    temperature=1,
)

print("Kimi 回复:")
print(response.choices[0].message.content)
