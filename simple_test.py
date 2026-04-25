print("Hello from Python")
import os
print(f"Python version: {os.sys.version}")
print("Setting API key...")
os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"
print("API key set.")

try:
    from openai import OpenAI
    print("OpenAI module imported.")
except ImportError as e:
    print(f"Cannot import OpenAI: {e}")

try:
    client = OpenAI(
        api_key=os.environ["MOONSHOT_API_KEY"],
        base_url="https://api.moonshot.cn/v1",
    )
    print("Client created.")
    response = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": "Hi"}],
        temperature=1,
    )
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f"Error: {e}")
