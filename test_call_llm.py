import os
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

from app.compile import call_llm

result = call_llm("请用一句话介绍 STM32 微控制器")
with open("call_llm_test.txt", "w", encoding="utf-8") as f:
    f.write(f"结果: {result}\n")
print("done")
