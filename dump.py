with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "Roads & Connectivity" in line:
        # Print 5 lines before and 20 lines after
        start = max(0, i - 5)
        end = min(len(lines), i + 20)
        with open("dump.txt", "w", encoding="utf-8") as out:
            out.writelines(lines[start:end])
        print("Dumped to dump.txt")
        break
