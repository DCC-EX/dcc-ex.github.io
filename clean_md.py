#!/usr/bin/env python3
"""
Comprehensive cleaning script for DCC-EX Markdown migration.
Handles all Sphinx patterns found in the documentation.
"""

import re
from pathlib import Path

DOCS_DIR = Path("docs")

def clean_file(filepath):
    """Clean a single Markdown file."""
    content = filepath.read_text(encoding='utf-8')
    original_content = content
    changes = []

    # 1. Remove Sphinx meta directives
    content = re.sub(r':::{.meta.*?}\n.*?\n:::', '', content, flags=re.DOTALL)
    changes.append("Removed meta directives")

    # 2. Remove Sphinx toctree directives
    content = re.sub(r':::{.toctree.*?}.*?:::', '', content, flags=re.DOTALL)
    changes.append("Removed toctree directives")

    # 3. Convert Sphinx admonitions
    content = re.sub(r'.. note::\s*(.*?)(?=\n\S|\Z)', r'!!! note "\1"', content, flags=re.DOTALL)
    content = re.sub(r'.. warning::\s*(.*?)(?=\n\S|\Z)', r'!!! warning "\1"', content, flags=re.DOTALL)
    content = re.sub(r'.. tip::\s*(.*?)(?=\n\S|\Z)', r'!!! tip "\1"', content, flags=re.DOTALL)
    content = re.sub(r'.. important::\s*(.*?)(?=\n\S|\Z)', r'!!! important "\1"', content, flags=re.DOTALL)
    content = re.sub(r'.. caution::\s*(.*?)(?=\n\S|\Z)', r'!!! caution "\1"', content, flags=re.DOTALL)
    content = re.sub(r'.. danger::\s*(.*?)(?=\n\S|\Z)', r'!!! danger "\1"', content, flags=re.DOTALL)
    changes.append("Converted admonitions")

    # 4. Fix Sphinx roles like |role| (convert to bold)
    # This handles single roles like |EX-CSB1-LOGO-SMALL|
    content = re.sub(r'\|([A-Z0-9\-_]+)\|', r'**\1**', content)
    changes.append("Fixed Sphinx roles")

    # 5. Fix Sphinx cross-references
    # Pattern: `text <target>`{.interpreted-text role="doc"}
    content = re.sub(r'`([^<]+)\s*<([^>]+)>`\{\.interpreted-text role="doc"\}', r'[\1](\2.md)', content)
    # Pattern: :ref:`text <target>`
    content = re.sub(r':ref:`([^<]+)\s*<([^>]+)>`', r'[\1](\2.md)', content)
    # Pattern: :doc:`text`
    content = re.sub(r':doc:`([^`]+)`', r'[\1](\1.md)', content)
    # Pattern: {interpreted-text role="doc"} after a link
    content = re.sub(r'<([^>]+)>\{interpreted-text role="doc"\}', r'[\1](\1.md)', content)
    # Pattern: {interpreted-text role="dcc-ex-text-size-60pct"} (remove it)
    content = re.sub(r'\{\.interpreted-text role="[^"]+"\}', '', content)
    changes.append("Fixed cross-references")

    # 6. Fix Sphinx includes
    content = re.sub(r'.. include::\s*([^\s]+)\.rst', r'--8<-- "\1.md"', content)
    changes.append("Fixed includes")

    # 7. Fix Sphinx code blocks
    content = re.sub(r'.. code-block::\s*(\w+)', r'```\1', content)
    content = re.sub(r'.. code-block::', r'```', content)
    changes.append("Fixed code blocks")

    # 8. Remove Sphinx attributes like {.hidden}
    content = re.sub(r'\{[^}]+\}', '', content)
    changes.append("Removed Sphinx attributes")

    # 9. Convert Sphinx images
    content = re.sub(r'.. image::\s*([^\s]+)', r'![](\1)', content)
    content = re.sub(r'.. figure::\s*([^\s]+)', r'![](\1)', content)
    changes.append("Fixed images")

    # 10. Fix Sphinx table syntax
    # Sphinx uses ===== for table headers
    content = re.sub(r'^={10,}$', '---', content, flags=re.MULTILINE)
    # Sphinx uses ----- for table separators (convert to | for Markdown)
    # This is complex and may need manual fixes
    changes.append("Fixed table headers")

    # 11. Fix Sphinx line breaks
    # |BR| is a Sphinx role for line breaks
    content = re.sub(r'\|BR\|', '<br>', content)
    changes.append("Fixed line breaks")

    # 12. Remove Sphinx hidden toctree
    content = re.sub(r'::: {.toctree hidden="" maxdepth="[0-9]+" caption="[^"]+"}\n.*?\n:::', '', content, flags=re.DOTALL)
    changes.append("Removed hidden toctree")

    # 13. Fix Sphinx "donate-button" role
    content = re.sub(r'\|donate-button\|', '', content)
    changes.append("Removed donate button")

    # If content changed, write it back
    if content != original_content:
        filepath.write_text(content, encoding='utf-8')
        return True, changes
    return False, []

def main():
    """Process all .md files in the docs directory."""
    count = 0
    for md_file in DOCS_DIR.rglob("*.md"):
        cleaned, changes = clean_file(md_file)
        if cleaned:
            count += 1
            print(f"Cleaned: {md_file}")
    print(f"\n✅ Cleaned {count} files")

if __name__ == "__main__":
    main()