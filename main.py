"""
Karpathy 风格长上下文知识库系统 - 主入口
流程: Ingest → Normalize → Compile → Export → Query → Output Filing → Lint
"""

import os
import shutil
from app.ingest import ingest
from app.normalize import normalize
from app.compile import compile_wiki
from app.query import query
from app.output_filing import save_answer_to_wiki
from app.lint import run_lint


def export_wiki(wiki_dir: str = "data/wiki", export_dir: str = "data/export"):
    """将 wiki 目录中的文件复制到 export 目录"""
    os.makedirs(export_dir, exist_ok=True)
    count = 0
    if os.path.isdir(wiki_dir):
        for fname in sorted(os.listdir(wiki_dir)):
            if not fname.endswith(".md"):
                continue
            src = os.path.join(wiki_dir, fname)
            dst = os.path.join(export_dir, fname)
            shutil.copy2(src, dst)
            print(f"  [Export] 复制: {fname}")
            count += 1
    print(f"  [Export] 导出完成，文件保存在 {export_dir}")


def main():
    print()
    print("=" * 60)
    print("  Karpathy 风格长上下文知识库系统")
    print("=" * 60)

    # Stage 1: Ingest
    print("\n [Step 1] Ingest（数据导入）")
    print(" " + "-" * 40)
    docs = ingest("data/raw")

    # Stage 2: Normalize
    print("\n [Step 2] Normalize（标准化）")
    print(" " + "-" * 40)
    parsed = normalize(docs, "data/parsed")

    # Stage 3: Compile
    print("\n [Step 3] Compile（编译 Wiki）")
    print(" " + "-" * 40)
    wiki_pages = compile_wiki("data/parsed", "data/wiki", "prompts/compile_prompt.txt")

    # Stage 4: Export
    print("\n [Step 4] Export（导出）")
    print(" " + "-" * 40)
    export_wiki("data/wiki", "data/export")

    # Stage 5: Query
    print("\n [Step 5] Query（问答演示）")
    print(" " + "-" * 40)
    demo_questions = [
        "STM32 有哪些常用的通信协议？",  
        "ADC 和 DMA 如何配合使用？",
        "GPIO 的工作模式有哪些？",
    ]
    answers = []
    for q in demo_questions:
        print(f"\n 问: {q}")
        a = query(q, "data/wiki", "prompts/query_prompt.txt")
        print(f" 答: {a}\n")
        answers.append((q, a))

    # Stage 6: Output Filing
    print("\n [Step 6] Output Filing（保存问答结果）")
    print(" " + "-" * 40)
    for q, a in answers:
        save_answer_to_wiki(q, a, "data/wiki")

    # Stage 7: Lint
    print("\n [Step 7] Lint（健康检查）")
    print(" " + "-" * 40)
    run_lint("data/wiki")

    # 完成
    wiki_abs = os.path.abspath("data/wiki")
    export_abs = os.path.abspath("data/export")
    print("\n" + "=" * 60)
    print("  流程完成！")
    print(f"  Wiki 文件: {wiki_abs}")
    print(f"  导出文件: {export_abs}")
    print("  可使用 Obsidian 打开 data/wiki/ 目录查看")
    print("=" * 60)


if __name__ == "__main__":
    main()
