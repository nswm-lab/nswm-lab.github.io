#!/usr/bin/env python3
"""Move ConvoyLLM demo section from outside paper-card to inside."""

with open("c:/Users/Eg4m1/Desktop/nswm-lab.github.io/_pages/about.md", "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.split('\n')

# Print context lines to verify
print("Lines 2146-2154 (0-indexed: 2145-2153):")
for i in range(2145, 2154):
    print(f"  [{i}] '{lines[i]}'")

print("\nLines 2243-2250:")
for i in range(2243, 2251):
    print(f"  [{i}] '{lines[i]}'")

# Key indices (0-indexed):
# 2148: "    </div>"  - closes lab-badvla-content (4 spaces)
# 2149: "  </div>"    - closes lab-badvla-paper-card (2 spaces)
# 2150: ""            - blank
# 2151: "  <!-- Video Demo..." - demo starts OUTSIDE paper-card
# 2245: "  </div>"    - closes convoy-demo-full div
# 2246: "</div>"      - closes lab-section

content_close_idx = 2148      # closes content
paper_card_close_idx = 2149   # closes paper-card
demo_comment_idx = 2151       # demo starts
demo_end_idx = 2245           # closes convoy-demo-full
section_close_idx = 2246       # closes lab-section

# Build new lines:
# 0 .. content_close_idx  (0 to 2148 inclusive)  -- up to and including content close
# then: blank + demo section (from demo_comment_idx to demo_end_idx inclusive)
# then: blank + paper-card close (line 2149)  
# then: section close (line 2246)
# then: everything after section close

new_lines = []

# Up to and including content close (index 2148)
for i in range(content_close_idx + 1):
    new_lines.append(lines[i])

# Blank line
new_lines.append('')

# Demo section content (indices 2152 to 2245 - the actual div content)
# But we also need to update the comment on line 2151
demo_comment_new = lines[demo_comment_idx].replace('(outside paper-card for full width)', '')
new_lines.append(demo_comment_new)
for i in range(demo_comment_idx + 1, demo_end_idx + 1):
    new_lines.append(lines[i])

# Blank line
new_lines.append('')

# Paper-card close (original line 2149)
new_lines.append('  </div>')

# Section close (original line 2246)
new_lines.append('</div>')

# Everything after section close (lines 2247+)
for i in range(section_close_idx + 1, len(lines)):
    new_lines.append(lines[i])

# Write back
new_content = '\n'.join(new_lines)
with open("c:/Users/Eg4m1/Desktop/nswm-lab.github.io/_pages/about.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"\nDone!")
print(f"Original: {len(lines)} lines, New: {len(new_lines)} lines")
print(f"Original length: {len(content)}, New length: {len(new_content)}")

# Verify structure
print("\nNew lines 2146-2156:")
for i in range(2146, 2156):
    print(f"  [{i}] '{new_lines[i]}'")
print("\nNew lines around section close:")
for i in range(len(new_lines)-6, len(new_lines)):
    if i >= 0:
        print(f"  [{i}] '{new_lines[i]}'")
