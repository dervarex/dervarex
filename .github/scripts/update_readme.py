import json, os, re

with open("stats.json") as f:
    data = json.load(f)

# Total hours and languages
total = data.get("totalHours", 0)
languages = data.get("languages", [])

lines = [f"**Total: {total}h**\n"]
for lang in languages[:5]:
    lines.append(f"- {lang['name']}: {lang['hours']}h")

block = "\n".join(lines)

with open("README.md") as f:
    readme = f.read()

readme = re.sub(
    r"<!--START_SECTION:ziit-->.*?<!--END_SECTION:ziit-->",
    f"<!--START_SECTION:ziit-->\n{block}\n<!--END_SECTION:ziit-->",
    readme,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(readme)