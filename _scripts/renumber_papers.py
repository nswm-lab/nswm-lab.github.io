import re

filepath = r'c:\Users\Eg4m1\Desktop\nswm-lab.github.io\_includes\pub-list.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Rename JNEW to a temp marker to avoid collision
content = content.replace('<span class="num">JNEW.</span>', '<span class="num">J__TEMP_NEW__.</span>')

# Step 2: Shift all J-numbers >= 7 by +1 (descending)
for n in range(164, 6, -1):
    old = f'<span class="num">J{n}.</span>'
    new = f'<span class="num">J{n+1}.</span>'
    content = content.replace(old, new)

# Step 3: Replace temp marker with J7
content = content.replace('<span class="num">J__TEMP_NEW__.</span>', '<span class="num">J7.</span>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
j_numbers = re.findall(r'<span class="num">J(\d+)\.</span>', content)
j_nums = [int(x) for x in j_numbers]
print(f"Journal papers: J1-J{max(j_nums)}, count={len(j_nums)}")
expected = list(range(1, max(j_nums)+1))
if j_nums == expected:
    print("All J numbers continuous!")
else:
    missing = set(expected) - set(j_nums)
    duplicates = [n for n in j_nums if j_nums.count(n) > 1]
    if missing: print(f"Missing: {sorted(missing)}")
    if duplicates: print(f"Duplicates: {sorted(set(duplicates))}")

c_numbers = re.findall(r'<span class="num">C(\d+)\.</span>', content)
c_nums = [int(x) for x in c_numbers]
print(f"Conference papers: C1-C{max(c_nums)}, count={len(c_nums)}")
