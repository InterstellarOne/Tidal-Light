import re

# Read userstyle.css
with open("userstyle.css", "r", encoding="utf-8") as f:
    content = f.read()

# Extract version from @version tag
version_match = re.search(r"@version\s+([\d.]+)", content)
version = version_match.group(1) if version_match else "unknown"

# Remove everything between /* ==UserStyle== */ and /* ==/UserStyle== */
no_header_content = re.sub(r"/\* ==UserStyle== \*/.*?/\* ==/UserStyle== \*/", "", content, flags=re.DOTALL).strip()

# Replace userstyle comment with JSON metadata in neptune.css
neptune_metadata = f"""
/*
{{
  "name": "Tidal Light",
  "author": "Interstellar_1",
  "description": "A light theme for Tidal. v{version}"
}}
*/
""".strip()

neptune_content = re.sub(r"/\* ==UserStyle== \*/.*?/\* ==/UserStyle== \*/", neptune_metadata, content, flags=re.DOTALL).strip()

# Write modified files
with open("no-header.css", "w", encoding="utf-8") as f:
    f.write(no_header_content)

with open("neptune.css", "w", encoding="utf-8") as f:
    f.write(neptune_content)

print("CSS processing complete.")
