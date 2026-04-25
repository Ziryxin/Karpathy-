import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

print("正在调用 Kimi API（带重试）...")
for attempt in range(10):
    try:
        response = client.chat.completions.create(
            model="kimi-k2.5",
            messages=[{"role": "user", "content": "Hello, 请用一句话介绍 STM32"}],
            temperature=1,
        )
        print(f"Kimi 回复: {response.choices[0].message.content}")
        print("API 连接成功！")
        break
    except Exception as e:
        wait = (attempt + 1) * 5
        print(f"第 {attempt+1} 次尝试失败: {e}")
        print(f"等待 {wait} 秒后重试...")
        time.sleep(wait)
