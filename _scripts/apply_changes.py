"""
Apply all modifications to about.md in a single script:
1. Add ConvoyLLM CSS (from broken file)
2. Add carousel CSS
3. Add carousel HTML + JS in BadVLA section
4. Extract "更多代表性成果" from BadVLA section
5. Add ConvoyLLM section (from broken file)
6. Insert "更多代表性成果" as independent section
7. Adjust section numbers
"""

import re

# Read original file
with open('_pages/about.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Read broken file for ConvoyLLM content
with open('_pages/about.md.broken', 'r', encoding='utf-8') as f:
    broken_lines = f.readlines()

# Extract ConvoyLLM CSS from broken file (lines 844-951, 0-indexed: 843-950)
convoy_css = broken_lines[843:951]
convoy_css_text = ''.join(convoy_css)

# Extract ConvoyLLM section HTML from broken file (lines 2226-2463, 0-indexed: 2225-2462)
convoy_html = broken_lines[2225:2463]
convoy_html_text = ''.join(convoy_html)

# Extract "更多代表性成果" content from original file
# In original: lines 1769 (0-indexed: 1768) to 1912 (0-indexed: 1911)
# Let's find exact boundaries
papers_start_idx = None
papers_end_idx = None

for i, line in enumerate(lines):
    if 'More Representative Papers' in line:
        papers_start_idx = i
    if papers_start_idx is not None and '<!-- ══════════════════════════════════════════════' in line:
        papers_end_idx = i
        break

print(f"Papers section: lines {papers_start_idx+1} to {papers_end_idx} (exclusive)")

# Extract just the content (papers-grid with all cards) - not the wrapper divs
# Find the lab-papers-intro and lab-papers-grid content
papers_intro_line = None
papers_grid_start = None
papers_grid_end = None

for i in range(papers_start_idx, papers_end_idx):
    if 'lab-papers-intro' in lines[i]:
        papers_intro_line = i
    if 'lab-papers-grid' in lines[i]:
        papers_grid_start = i

# Find the closing of lab-papers-grid (matching </div>)
# We need to count nesting - lab-papers-grid opens at papers_grid_start
# The content goes until the matching </div> for lab-papers-section
# Let's just grab from lab-papers-intro to the closing </div> of lab-papers-section
depth = 0
for i in range(papers_start_idx, papers_end_idx):
    if '<div' in lines[i]:
        depth += lines[i].count('<div')
    if '</div>' in lines[i]:
        depth -= lines[i].count('</div>')
    # When we return to depth 0 after starting, that's our end
    if depth == 0 and i > papers_start_idx:
        papers_grid_end = i + 1  # inclusive
        break

print(f"Papers grid: lines {papers_grid_start+1} to {papers_grid_end}")

# ========== CAROUSEL CSS ==========
carousel_css = """
/* ─── BADVLA RESULTS CAROUSEL ─── */
.lab-results-carousel-wrap {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 2px solid #e2e8f0;
}
.lab-results-title {
  font-size: 0.95rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.lab-results-carousel {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-md);
  background: #f8fafc;
  border: 1px solid #e2e8f0;
}
.lab-results-track {
  display: flex;
  transition: transform 0.45s cubic-bezier(0.25, 0.8, 0.25, 1);
  will-change: transform;
}
.lab-results-slide {
  min-width: 100%;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  box-sizing: border-box;
}
.lab-results-slide img {
  max-width: 100%;
  height: auto;
  border-radius: var(--radius-sm);
  box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  display: block;
}
.lab-results-caption {
  margin-top: 0.8rem;
  font-size: 0.78rem;
  color: #475569;
  line-height: 1.6;
  text-align: center;
  max-width: 700px;
}
/* Navigation arrows */
.lab-results-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: rgba(255,255,255,0.92);
  color: #0f172a;
  font-size: 1.3rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
  transition: all 0.2s;
  z-index: 2;
  line-height: 1;
}
.lab-results-nav:hover {
  background: #fff;
  box-shadow: 0 4px 16px rgba(0,0,0,0.18);
  color: #0d9488;
}
.lab-results-nav.prev { left: 10px; }
.lab-results-nav.next { right: 10px; }
/* Dots */
.lab-results-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 0.9rem;
}
.lab-results-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #cbd5e1;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  padding: 0;
}
.lab-results-dot:hover {
  background: #94a3b8;
}
.lab-results-dot.active {
  background: #0d9488;
  width: 24px;
  border-radius: 4px;
}
/* Touch hint for mobile */
@media (max-width: 768px) {
  .lab-results-slide { padding: 1rem 0.5rem; }
  .lab-results-nav { width: 30px; height: 30px; font-size: 1.1rem; }
  .lab-results-nav.prev { left: 6px; }
  .lab-results-nav.next { right: 6px; }
}
"""

# ========== CAROUSEL HTML + JS ==========
carousel_html_js = """
      <!-- Experiment Results Carousel -->
      <div class="lab-results-carousel-wrap">
        <div class="lab-results-title">&#x1f4ca; 实验结果</div>
        <div class="lab-results-carousel" id="badvla-carousel">
          <div class="lab-results-track">
            <!-- Slide 1: Performance Table -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/tabel1.png" alt="BadVLA ASR Performance on LIBERO Benchmarks" loading="lazy" />
              <div class="lab-results-caption">主实验结果：不同触发类型（Block, Mug, Stick）在 LIBERO 基准上的攻击成功率 (ASR)，与基线投毒方法对比</div>
            </div>
            <!-- Slide 2: Cosine Similarity -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/x5.png" alt="Cosine Similarity between Clean and Triggered Features" loading="lazy" />
              <div class="lab-results-caption">特征相似度分析：Stage I 优化前后，clean 与 triggered 特征的余弦相似度显著下降，表明触发器引发了强烈的表征偏移</div>
            </div>
            <!-- Slide 3: Trajectory 1 -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/x4.png" alt="Trajectory Comparison 1" loading="lazy" />
              <div class="lab-results-caption">轨迹对比 1：正常行为 vs. 触发器激活后的操作轨迹偏移</div>
            </div>
            <!-- Slide 4: Trajectory 2 -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/x6.png" alt="Trajectory Comparison 2" loading="lazy" />
              <div class="lab-results-caption">轨迹对比 2：不同任务场景下的后门攻击效果展示</div>
            </div>
            <!-- Slide 5: Trajectory 3 -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/x7.png" alt="Trajectory Comparison 3" loading="lazy" />
              <div class="lab-results-caption">轨迹对比 3：目标条件操纵（Goal Condition Manipulation）下的轨迹偏移</div>
            </div>
            <!-- Slide 6: Trajectory 4 -->
            <div class="lab-results-slide">
              <img src="/images/badvla/results/x8.png" alt="Trajectory Comparison 4" loading="lazy" />
              <div class="lab-results-caption">轨迹对比 4：空间条件操纵（Spatial Condition Manipulation）下的轨迹偏移</div>
            </div>
          </div>
          <button class="lab-results-nav prev" aria-label="Previous">&#8249;</button>
          <button class="lab-results-nav next" aria-label="Next">&#8250;</button>
        </div>
        <div class="lab-results-dots">
          <span class="lab-results-dot active" data-index="0"></span>
          <span class="lab-results-dot" data-index="1"></span>
          <span class="lab-results-dot" data-index="2"></span>
          <span class="lab-results-dot" data-index="3"></span>
          <span class="lab-results-dot" data-index="4"></span>
          <span class="lab-results-dot" data-index="5"></span>
        </div>
      </div>

      <script>
      (function() {
        var carousel = document.getElementById('badvla-carousel');
        if (!carousel) return;
        var track = carousel.querySelector('.lab-results-track');
        var dots = carousel.parentElement.querySelectorAll('.lab-results-dot');
        var prevBtn = carousel.querySelector('.lab-results-nav.prev');
        var nextBtn = carousel.querySelector('.lab-results-nav.next');
        var slides = carousel.querySelectorAll('.lab-results-slide');
        var current = 0;
        var total = slides.length;

        function goTo(index) {
          if (index < 0) index = total - 1;
          if (index >= total) index = 0;
          current = index;
          track.style.transform = 'translateX(-' + (current * 100) + '%)';
          dots.forEach(function(d, i) {
            d.classList.toggle('active', i === current);
          });
        }

        prevBtn.addEventListener('click', function() { goTo(current - 1); });
        nextBtn.addEventListener('click', function() { goTo(current + 1); });
        dots.forEach(function(dot) {
          dot.addEventListener('click', function() {
            goTo(parseInt(this.getAttribute('data-index')));
          });
        });

        var startX = 0, isDragging = false;
        carousel.addEventListener('touchstart', function(e) {
          startX = e.touches[0].clientX;
          isDragging = true;
        }, { passive: true });
        carousel.addEventListener('touchend', function(e) {
          if (!isDragging) return;
          isDragging = false;
          var diff = startX - e.changedTouches[0].clientX;
          if (Math.abs(diff) > 50) {
            diff > 0 ? goTo(current + 1) : goTo(current - 1);
          }
        }, { passive: true });
      })();
      </script>
"""

# ========== MORE PAPERS SECTION (defined later after papers_content_text is available) ==========
# (see below)

# ========== NOW BUILD THE NEW FILE ==========

# Find insertion points in original file
# 1. Insert convoy CSS + carousel CSS before "/* ─── MORE PAPERS GRID ─── */" (line ~843, 0-indexed 842)
css_insert_idx = None
for i, line in enumerate(lines):
    if 'MORE PAPERS GRID' in line and '───' in line:
        css_insert_idx = i
        break

print(f"CSS insert point: line {css_insert_idx+1}")

# 2. Find where the last BadVLA demo video grid closes (before "More Representative Papers")
# In original file, line 1768 is "<!-- More Representative Papers -->"
# The demo grid ends just before that
demo_end_idx = papers_start_idx - 1  # line before the comment
# Skip blank lines
while demo_end_idx > 0 and lines[demo_end_idx].strip() == '':
    demo_end_idx -= 1

print(f"Demo end: line {demo_end_idx+1}")

# 3. Remove "More Representative Papers" from BadVLA section
# From papers_start_idx to papers_grid_end (inclusive of closing </div> for lab-papers-section)
# Actually we need to find the line range more carefully
# The papers section starts at papers_start_idx (the comment line)
# and ends when lab-papers-section closes
# In original file the structure is:
#   <!-- More Representative Papers -->
#   <div class="lab-papers-section">
#     <div class="lab-papers-section-title">...</div>
#     <div class="lab-papers-intro">...</div>
#     <div class="lab-papers-grid">
#       ...paper cards...
#     </div>
#   </div>
# The line after the closing </div> of lab-papers-section should be blank or closing content div

# Let's find exact end by tracking the lab-papers-section div
# Only count divs INSIDE lab-papers-section, not the outer ones
depth = 0
section_opened = False
papers_section_end = None
for i in range(papers_start_idx, len(lines)):
    l = lines[i]
    if '<div class="lab-papers-section">' in l:
        section_opened = True
        depth = 0  # the lab-papers-section div itself counts as 1 open
        continue  # skip counting on this line since we set depth manually
    if section_opened:
        depth += l.count('<div') - l.count('</div>')
        if depth < 0:
            # This closing </div> closes lab-papers-section itself
            papers_section_end = i + 1  # exclusive
            break

print(f"Papers section removal range: lines {papers_start_idx+1} to {papers_section_end}")

# Extract papers content (intro + grid with cards)
# We want from lab-papers-intro up to (but NOT including) the lab-papers-section closing </div>
papers_content = lines[papers_intro_line:papers_section_end - 1]  # exclude lab-papers-section close
papers_content_text = ''.join(papers_content)

# ========== MORE PAPERS SECTION ==========
more_papers_section = """
<!-- ══════════════════════════════════════════════
     SECTION 3.6: MORE PUBLICATIONS
     ══════════════════════════════════════════════ -->
<div class="lab-section" id="more-publications">
  <div class="lab-badvla-header">
    <div class="lab-section-title-en">04 · More Publications</div>
    <div class="lab-section-title-zh">更多代表性成果</div>
    <div class="lab-section-divider"></div>
  </div>
""" + papers_content_text + """
</div>
"""

# 4. Find BadVLA section closing (should be right after papers section in original)
# In original: after papers_section_end, there's content close, paper-card close, section close
# Let's find the SECTION 4 comment to know where BadVLA section ends
badvla_section_end = None
for i, line in enumerate(lines):
    if 'SECTION 4: RESEARCH DIRECTIONS' in line:
        badvla_section_end = i  # the comment line marks start of next section
        break

print(f"BadVLA section end / Section 4 start: line {badvla_section_end+1}")

# Now build the new file
new_lines = []

# Part 1: Everything up to CSS insert point
new_lines.extend(lines[:css_insert_idx])

# Part 2: ConvoyLLM CSS + Carousel CSS
new_lines.append(convoy_css_text)

# Part 3: CSS insert point onward to demo end
new_lines.extend(lines[css_insert_idx:demo_end_idx + 1])

# Part 4: Carousel HTML + JS
new_lines.append(carousel_html_js)

# Part 4.5: Close BadVLA section (content, paper-card, section)
new_lines.append('\n    </div>\n  </div>\n</div>\n')

# Part 5: Skip the "More Representative Papers" section
# Go from after papers_section_end to badvla_section_end
# This skips: blank lines + papers section + closing divs for BadVLA section
# The closing divs are already added in Part 4.5, so we skip from papers_start_idx to badvla_section_end

# Part 6: ConvoyLLM section
new_lines.append('\n')
new_lines.extend(convoy_html)

# Part 7: More Publications section
new_lines.append('\n')
new_lines.append(more_papers_section)

# Part 8: Rest of file from SECTION 4 onwards, with adjusted section numbers
rest_lines = lines[badvla_section_end:]
for line in rest_lines:
    # Adjust section numbers
    modified = line
    modified = modified.replace('03 · Research Directions', '05 · Research Directions')
    modified = modified.replace('04 · Latest News', '06 · Latest News')
    new_lines.append(modified)

# Write result
with open('_pages/about.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"\nDone! Output: {len(new_lines)} lines")
print("Verify div balance...")

# Quick div balance check
full_text = ''.join(new_lines)
opens = full_text.count('<div')
closes = full_text.count('</div>')
print(f"<div>: {opens}, </div>: {closes}, diff: {opens - closes}")

# Check for carousel references
print(f"Carousel refs: {full_text.count('lab-results-carousel')}")
print(f"ConvoyLLM refs: {full_text.count('convoyllm')}")
print(f"More publications: {full_text.count('more-publications')}")
