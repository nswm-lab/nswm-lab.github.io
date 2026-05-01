import re

filepath = r'c:\Users\Eg4m1\Desktop\nswm-lab.github.io\_includes\pub-list.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ====== Step 1: Insert 7 new 2026 papers at end of 2026 section ======
# Current 2026 section ends with C5 (NDSS). Insert after C5's </li>
new_2026_papers = [
    ('Q. Shen, J. Li, J. Peng, Z. Xu, C. Zhao, Pan Zhou*, W. Liang, X. Jia, S. K. Das, W. Xu',
     'Keep Fresh Digital Twins in UAV-assisted IoT Networks by Exploiting Data Correlations',
     'IEEE ICDCS 2026'),
    ('Z. Sheng, G. Tie, W. Wang, Pan Zhou*, D. Liu',
     'LearnerCoMPASS: Intelligent Tutoring System with Dynamic Cognitive Diagnosis and Multi-Model Path Planning',
     'ACL 2026'),
    ('X. Zhou, W. Wang, L. Lu, J. Shi, G. Tie, X. Yongtian, L. Chen, Pan Zhou*, N. Z. Gong, L. Sun',
     'SafeAgent: Safeguarding LLM Agents via an Automated Risk Simulator',
     'ACL 2026'),
    ('Z. Yu, X. Liu, Y. Cheung, Z. Hu, W. Fan, Pan Zhou*',
     'DRFGD: Disentangled Representation-Focused Generative Defense for Attack-Tolerant Cross-Modal Hashing',
     'AAAI 2026'),
    ('Y. Li, L. Yang, W. Shen, Pan Zhou*, Y. Wan, W. Lin, D. Chen',
     'CrowdSelect: Synthetic Instruction Data Selection with Multi-LLM Wisdom',
     'EACL 2026 (Findings)'),
    ('X. Zhou, Y. Xu, G. Tie, Y. Chen, C. Hu, B. Tao, X. Zhao, X. Xiang, Pan Zhou*, L. Sun',
     'Dismantling the Illusion of Vision-Language-Action Models Competence via Explicit Distributional Shifts',
     'ICML 2026'),
    ('G. Tie, T. Luo, X. Zhou, C. Hu, Y. He, J. Wu, Y. Yao, Pan Zhou*, L. Sun',
     'Routing and Reasoned Evaluation with Large Language Models',
     'ICML 2026'),
]

# Find the end of 2026 section: </ul>\n</div>\n\n<!-- 2025 -->
marker_2026_end = '</ul>\n</div>\n\n<!-- 2025 -->'
pos = content.find(marker_2026_end)
if pos == -1:
    print("ERROR: 2026 section end marker not found")
    exit(1)

insert_html = '\n'
for authors, title, venue in new_2026_papers:
    insert_html += f'<li><span class="num">NEW.</span> {authors}. "{title}." <span class="venue">{venue}</span>.</li>\n'

content = content[:pos] + insert_html + content[pos:]
print("Inserted 7 new 2026 papers")

# ====== Step 2: Insert 2 new 2025 papers ======
# ConvoyLLM: insert after ACM MM (RoDeCon-Net)
convoy = ('L. Lu, Z. He, D. Chu, R. Wang, S. Peng, Pan Zhou',
          'ConvoyLLM: Dynamic Multi-Lane Convoy Control Using LLMs',
          'IROS 2025')
convoy_marker = 'RoDeCon-Net'
convoy_pos = content.find(convoy_marker)
if convoy_pos == -1:
    print("ERROR: ConvoyLLM insert point not found")
    exit(1)
# Find end of this <li>
li_end = content.find('</li>', convoy_pos)
insert_html_convoy = f'\n<li><span class="num">NEW.</span> {convoy[0]}. "{convoy[1]}." <span class="venue">{convoy[2]}</span>.</li>'
content = content[:li_end + 5] + insert_html_convoy + content[li_end + 5:]
print("Inserted ConvoyLLM")

# Merger-as-a-stealer: insert after "Learning from Few Samples" (EMNLP)
merger = ('L. Lu, Z. Zuo, Z. Sheng, Pan Zhou',
          'Merger-as-a-stealer: Stealing Targeted PII from Aligned LLMs with Model Merging',
          'EMNLP 2025')
merger_marker = 'Learning from Few Samples'
merger_pos = content.find(merger_marker)
if merger_pos == -1:
    print("ERROR: Merger insert point not found")
    exit(1)
li_end = content.find('</li>', merger_pos)
insert_html_merger = f'\n<li><span class="num">NEW.</span> {merger[0]}. "{merger[1]}." <span class="venue">{merger[2]}</span>.</li>'
content = content[:li_end + 5] + insert_html_merger + content[li_end + 5:]
print("Inserted Merger-as-a-stealer")

# ====== Step 3: Renumber all conference papers sequentially ======
conf_marker = '<!-- =============================== 期刊论文 =============================== -->'
conf_end = content.find(conf_marker)
conf_part = content[:conf_end]
rest_part = content[conf_end:]

# Find all <li> elements in conference section and renumber
def renumber_li(match):
    global li_counter
    li_counter += 1
    return f'<li><span class="num">C{li_counter}.</span>{match.group(1)}</li>'

li_counter = 0
conf_part = re.sub(r'<li><span class="num">[^<]*</span>(.*?)</li>', renumber_li, conf_part)

content = conf_part + rest_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# ====== Verify ======
numbers = re.findall(r'<span class="num">C(\d+)\.</span>', content)
nums = [int(x) for x in numbers]
print(f"\nConference papers: C1-C{max(nums)}, count={len(nums)}")
expected = list(range(1, max(nums)+1))
if nums == expected:
    print("All numbers continuous and correct!")
else:
    missing = set(expected) - set(nums)
    duplicates = [n for n in nums if nums.count(n) > 1]
    if missing:
        print(f"Missing: {sorted(missing)}")
    if duplicates:
        print(f"Duplicates: {sorted(set(duplicates))}")

j_numbers = re.findall(r'<span class="num">J(\d+)\.</span>', content)
j_nums = [int(x) for x in j_numbers]
print(f"Journal papers: J1-J{max(j_nums)}, count={len(j_nums)}")

# Check for any remaining NEW markers
if 'NEW.' in content:
    print("WARNING: unrenumbered NEW. markers found!")
else:
    print("No stray markers found.")
