import re

filepath = "c:/Users/Eg4m1/Desktop/nswm-lab.github.io/_includes/pub-list.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Split into style, journal section, conference section
style_part = content[:content.index('<!-- =============================== 期刊论文')]

journal_start = content.index('<!-- =============================== 期刊论文 =============================== -->')
journal_end = content.index('<!-- =============================== 会议论文 =============================== -->')
journal_section = content[journal_start:journal_end]

conference_start = journal_end
conference_section = content[conference_start:]

# Remove "2017 及以前" blocks from both sections
def remove_old_papers(section):
    pattern = r'<!-- 201[0-7].*?-->\s*<div class="pub-year-group">\s*<h3>2017 及以前</h3>.*?</ul>\s*</div>'
    return re.sub(pattern, '', section, flags=re.DOTALL)

journal_section = remove_old_papers(journal_section)
conference_section = remove_old_papers(conference_section)

# Renumber papers
def renumber_papers(section, prefix):
    count = 0
    def replace_num(m):
        nonlocal count
        count += 1
        return '<span class="num">' + prefix + str(count) + '.</span>'
    return re.sub(r'<span class="num">[JC]\d+\.</span>', replace_num, section), count

conference_section, c_count = renumber_papers(conference_section, 'C')
journal_section, j_count = renumber_papers(journal_section, 'J')

# Reassemble: style + conference + journal
new_content = style_part + conference_section + '\n' + journal_section

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Conference papers: " + str(c_count))
print("Journal papers: " + str(j_count))
print("Done!")
