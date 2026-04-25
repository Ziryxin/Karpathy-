import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MOONSHOT_API_KEY"],
    base_url="https://api.moonshot.cn/v1",
)

with open("kimi_test_result.txt", "w", encoding="utf-8") as f:
    f.write("正在调用 Kimi API...\n")
    try:
        response = client.chat.completions.create(
            model="kimi-k2.5",
            messages=[{"role": "user", "content": "Hello, 请用一句话介绍 STM32"}],
            temperature=1,
        )
        result = response.choices[0].message.content
        f.write(f"Kimi 回复:\n{result}\n")
        f.write("API 连接成功！\n")
    except Exception as e:
        f.write(f"调用失败: {e}\n")
        f.write("尝试重试...\n")
        time.sleep(5)
        try:
            response = client.chat.completions.create(
                model="kimi-k2.5",
                messages=[{"role": "user", "content": "Hello"}],
                temperature=1,
            )
            result = response.choices[0].message.content
            f.write(f"重试成功，Kimi 回复:\n{result}\n")
        except Exception as e2:
            f.write(f"重试也失败: {e2}\n")
