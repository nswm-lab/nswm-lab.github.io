# Memory

## 项目概况
- Jekyll GitHub Pages 项目，Academic Pages 模板
- 源码：`c:\Users\Eg4m1\Desktop\nswm-lab.github.io`
- 论文列表在 `_includes/pub-list.html`，纯静态 HTML，不使用 Jekyll collection

## 本地预览流程
- `cmd //c "set ACC_PRODUCT_CONFIG_V3= && bundle exec jekyll build"` 重建
- `cd _site && python -m http.server 4000` 启动预览
- 每次修改源文件后都需要重建 + 重启服务器才能看到效果

## 论文编号规则
- 会议论文：C1-C141（年份倒序：2026→...→更早）
- 期刊论文：J1-J165（年份倒序）

## 技术注意
- Bash 中直接用 `bundle exec` 会因 `ACC_PRODUCT_CONFIG_V3` 环境变量报错，需用 `cmd //c "set ACC_PRODUCT_CONFIG_V3= && ..."`
- 修改文件前记得 git commit，否则 `git checkout` 会丢失未提交的改动
- Kramdown 会处理 `<style>` 和 `<script>` 标签内容，可能导致 CSS/JS 被吞掉
- 大量 HTML 修改优先用 Python 脚本，但必须验证：1) div balance 2) CSS 内容完整注入 3) HTML 注释标记完整
- 脚本中定义了变量但未使用是常见 bug，运行后务必用 grep 检查关键 CSS/HTML 是否出现在输出中

## Section 编号体系（about.md）
- 01: Professor & Concept
- 02: Featured Research (BadVLA) — lab-section-dark
- 03: Featured Research (ConvoyLLM)
- 04: More Publications（独立 section，原在 BadVLA 内部）
- 05: Research Directions
- 06: Latest News
- Join Us（无编号）
