import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

for attempt in range(10):
    try:
        response = client.chat.completions.create(
            model="kimi-k2.5",
            messages=[{"role": "user", "content": "Hello"}],
            temperature=1,
        )
        with open("api_test.txt", "w", encoding="utf-8") as f:
            f.write(f"成功: {response.choices[0].message.content}\n")
        break
    except Exception as e:
        time.sleep((attempt + 1) * 5)
