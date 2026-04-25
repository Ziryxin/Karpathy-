import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

with open("kimi_result.txt", "w", encoding="utf-8") as f:
    f.write("正在调用 Kimi API（带重试）...\n")
    for attempt in range(10):
        try:
            response = client.chat.completions.create(
                model="kimi-k2.5",
                messages=[{"role": "user", "content": "Hello, 请用一句话介绍 STM32"}],
                temperature=1,
            )
            result = response.choices[0].message.content
            f.write(f"Kimi 回复: {result}\n")
            f.write("API 连接成功！\n")
            break
        except Exception as e:
            wait = (attempt + 1) * 5
            f.write(f"第 {attempt+1} 次尝试失败: {e}\n")
            f.write(f"等待 {wait} 秒后重试...\n")
            f.flush()
            time.sleep(wait)
