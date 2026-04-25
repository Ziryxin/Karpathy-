import os
import sys
import traceback

os.environ["MOONSHOT_API_KEY"] = "sk-Xx6o7Phs5TlQKbh06Cz6uhEDEaCcAt0q9QW77omCAjWjHiqu"

try:
    with open("run_log.txt", "w", encoding="utf-8") as log:
        log.write("Step 1: Ingest\n")
        from app.ingest import ingest
        docs = ingest("data/raw")
        log.write(f"  读取 {len(docs)} 个文件\n")

        log.write("Step 2: Normalize\n")
        from app.normalize import normalize
        parsed = normalize(docs, "data/parsed")
        log.write(f"  处理 {len(parsed)} 个文件\n")

        log.write("Step 3: Compile\n")
        from app.compile import compile_wiki
        wiki_pages = compile_wiki("data/parsed", "data/wiki", "prompts/compile_prompt.txt")
        log.write(f"  生成 {len(wiki_pages)} 个页面\n")

        log.write("Step 4: Export\n")
        import shutil
        export_dir = "data/export"
        os.makedirs(export_dir, exist_ok=True)
        wiki_dir = "data/wiki"
        if os.path.isdir(wiki_dir):
            for fname in sorted(os.listdir(wiki_dir)):
                if fname.endswith(".md"):
                    shutil.copy2(os.path.join(wiki_dir, fname), os.path.join(export_dir, fname))
                    log.write(f"  复制: {fname}\n")
        log.write("  导出完成\n")

        log.write("Step 5: Query\n")
        from app.query import query
        questions = [
            "STM32 有哪些常用的通信协议？",
            "ADC 和 DMA 如何配合使用？",
            "GPIO 的工作模式有哪些？",
        ]
        answers = []
        for q in questions:
            log.write(f"  问: {q}\n")
            a = query(q, "data/wiki", "prompts/query_prompt.txt")
            log.write(f"  答: {a[:100]}...\n")
            answers.append((q, a))

        log.write("Step 6: Output Filing\n")
        from app.output_filing import save_answer_to_wiki
        for q, a in answers:
            path = save_answer_to_wiki(q, a, "data/wiki")
            log.write(f"  保存: {path}\n")

        log.write("Step 7: Lint\n")
        from app.lint import run_lint
        result = run_lint("data/wiki")
        log.write(f"  死链: {len(result['dead_links'])}\n")
        log.write(f"  孤立页面: {len(result['orphaned_pages'])}\n")
        log.write(f"  矛盾: {len(result['contradictions'])}\n")

        log.write("\n全部完成！\n")

except Exception as e:
    with open("run_log.txt", "a", encoding="utf-8") as log:
        log.write(f"\n错误: {e}\n")
        log.write(traceback.format_exc())
