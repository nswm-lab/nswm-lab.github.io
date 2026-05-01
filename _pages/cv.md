---
layout: archive
title: "个人简历"
permalink: /cv/
author_profile: true
---

<style>
/* ─── Variables ─── */
:root {
  --navy: #0f2744;
  --blue: #1a3a6b;
  --teal: #2563eb;
  --slate: #64748b;
  --white: #ffffff;
  --gray-50: #f8fafc;
  --gray-100: #f1f5f9;
  --gray-200: #e2e8f0;
  --gray-800: #1e293b;
}

/* ─── Hero Section ─── */
.cv-hero {
  background: linear-gradient(135deg, #0a1628 0%, #1a3a6b 50%, #0f2744 100%);
  color: var(--white);
  padding: 3.5rem 2rem 2rem;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}
.cv-hero::before {
  content: '';
  position: absolute;
  top: -60px; right: -60px;
  width: 300px; height: 300px;
  background: radial-gradient(circle, rgba(37,99,235,0.18) 0%, transparent 70%);
  border-radius: 50%;
}
.cv-hero::after {
  content: '';
  position: absolute;
  bottom: -80px; left: 10%;
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(59,130,246,0.15) 0%, transparent 70%);
  border-radius: 50%;
}
.cv-hero-inner {
  position: relative;
  z-index: 1;
  max-width: 100%;
  margin: 0 auto;
}
.cv-hero-name {
  font-size: 2.4rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  margin-bottom: 0.2rem;
  line-height: 1.2;
}
.cv-hero-name-en {
  font-size: 1rem;
  color: rgba(255,255,255,0.6);
  font-weight: 400;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 1rem;
}
.cv-hero-title {
  font-size: 1.05rem;
  color: rgba(255,255,255,0.85);
  margin-bottom: 0.5rem;
}
.cv-hero-inst {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.7);
  margin-bottom: 1.2rem;
}
.cv-hero-contacts {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 2rem;
  margin-top: 1rem;
}
.cv-hero-contact {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-size: 0.85rem;
  color: rgba(255,255,255,0.8);
}
.cv-hero-contact a { color: #7dd3fc; text-decoration: none; }
.cv-hero-contact a:hover { color: #bae6fd; text-decoration: underline; }
.cv-hero-contact svg { width: 14px; height: 14px; flex-shrink: 0; opacity: 0.7; }

/* ─── Stats Strip ─── */
.cv-stats {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1px;
  background: var(--gray-200);
  max-width: 100%;
  margin: 0 auto 2.5rem;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}
.cv-stat-card {
  background: var(--white);
  padding: 1.2rem 0.8rem;
  text-align: center;
  transition: transform 0.2s;
}
.cv-stat-card:hover { transform: translateY(-2px); }
.cv-stat-icon {
  font-size: 1.4rem;
  margin-bottom: 0.3rem;
}
.cv-stat-num {
  font-size: 1.6rem;
  font-weight: 800;
  line-height: 1.1;
  color: var(--navy);
}
.cv-stat-label {
  font-size: 0.72rem;
  color: var(--slate);
  margin-top: 0.2rem;
  line-height: 1.3;
}
.cv-stat-card.highlight-teal .cv-stat-num { color: var(--teal); }
.cv-stat-card.highlight-blue .cv-stat-num { color: var(--teal); }
.cv-stat-card.highlight-amber .cv-stat-num { color: var(--navy); }
.cv-stat-card.highlight-rose .cv-stat-num { color: var(--teal); }
.cv-stat-card.highlight-purple .cv-stat-num { color: var(--navy); }

/* ─── Section Common ─── */
.cv-section {
  max-width: 100%;
  margin: 0 auto 2.5rem;
  padding: 0;
}
.cv-section-title {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 1.2rem;
  padding-bottom: 0.6rem;
  border-bottom: 2px solid #e0e7ff;
}
.cv-section-title-icon {
  width: 28px; height: 28px;
  background: var(--navy);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.cv-section-title-icon svg { width: 15px; height: 15px; color: white; }

/* ─── Research Interests Tags ─── */
.cv-interest-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.cv-interest-tag {
  padding: 0.35rem 0.9rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  border: 1.5px solid;
}
.cv-interest-tag.primary {
  background: #eff6ff;
  border-color: #93c5fd;
  color: #1e40af;
}
.cv-interest-tag.secondary {
  background: #eff6ff;
  border-color: #93c5fd;
  color: #1e40af;
}
.cv-interest-tag.tertiary {
  background: #f8fafc;
  border-color: #93c5fd;
  color: #1e40af;
}

/* ─── Timeline ─── */
.cv-timeline { position: relative; }
.cv-timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 8px;
  bottom: 8px;
  width: 2px;
  background: linear-gradient(to bottom, var(--navy), var(--teal));
  border-radius: 2px;
}
.cv-timeline-item {
  position: relative;
  padding-left: 32px;
  padding-bottom: 1.5rem;
}
.cv-timeline-item:last-child { padding-bottom: 0; }
.cv-timeline-dot {
  position: absolute;
  left: 0;
  top: 6px;
  width: 16px;
  height: 16px;
  background: var(--white);
  border: 3px solid #1a3a6b;
  border-radius: 50%;
  z-index: 1;
}
.cv-timeline-dot.active { border-color: var(--teal); background: var(--teal); }
.cv-timeline-dot.edu { border-color: var(--teal); }
.cv-timeline-date {
  font-size: 0.78rem;
  color: var(--slate);
  margin-bottom: 0.15rem;
}
.cv-timeline-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--gray-800);
  line-height: 1.3;
}
.cv-timeline-sub {
  font-size: 0.82rem;
  color: var(--slate);
  margin-top: 0.1rem;
  line-height: 1.4;
}
.cv-timeline-desc {
  font-size: 0.82rem;
  color: #475569;
  margin-top: 0.3rem;
  line-height: 1.5;
}
.cv-timeline-desc li { margin-bottom: 0.15rem; list-style: none; padding-left: 0.8rem; position: relative; }
.cv-timeline-desc li::before { content: '▸'; position: absolute; left: 0; color: var(--teal); }

/* ─── Projects Table ─── */
.cv-projects-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}
.cv-projects-table th {
  background: var(--navy);
  color: var(--white);
  padding: 0.6rem 0.8rem;
  text-align: left;
  font-weight: 600;
}
.cv-projects-table th:first-child { border-radius: 8px 0 0 0; }
.cv-projects-table th:last-child { border-radius: 0 8px 0 0; }
.cv-projects-table td {
  padding: 0.55rem 0.8rem;
  border-bottom: 1px solid var(--gray-200);
  vertical-align: top;
  line-height: 1.4;
}
.cv-projects-table tr:nth-child(even) td { background: #f8fafc; }
.cv-projects-table tr:last-child td:first-child { border-radius: 0 0 0 8px; }
.cv-projects-table tr:last-child td:last-child { border-radius: 0 0 8px 0; }
.cv-fund-tag {
  display: inline-block;
  background: #dbeafe;
  color: #1e40af;
  padding: 0.1rem 0.45rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 600;
  white-space: nowrap;
}
.cv-project-level {
  display: inline-block;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 600;
}
.cv-project-level.gj { background: #dbeafe; color: #1e40af; }
.cv-project-level.sj { background: #eff6ff; color: #1e40af; }
.cv-project-level.hx { background: #dbeafe; color: #1e40af; }

/* ─── Honors ─── */
.cv-honors-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.8rem;
}
.cv-honor-card {
  background: var(--white);
  border: 1.5px solid var(--gray-200);
  border-radius: 10px;
  padding: 1rem 1.1rem;
  transition: all 0.2s;
  position: relative;
  overflow: hidden;
}
.cv-honor-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
}
.cv-honor-card.gold::before { background: var(--navy); }
.cv-honor-card.blue::before { background: var(--teal); }
.cv-honor-card.teal::before { background: var(--teal); }
.cv-honor-card.rose::before { background: var(--teal); }
.cv-honor-card.purple::before { background: var(--navy); }
.cv-honor-card:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,0.08); }
.cv-honor-year {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--slate);
  margin-bottom: 0.25rem;
}
.cv-honor-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--gray-800);
  line-height: 1.3;
  margin-bottom: 0.2rem;
}
.cv-honor-org {
  font-size: 0.78rem;
  color: var(--slate);
}
.cv-honor-badge {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 700;
  margin-top: 0.3rem;
}
.cv-honor-badge.gold { background: #dbeafe; color: #1e40af; }
.cv-honor-badge.blue { background: #dbeafe; color: #1e40af; }
.cv-honor-badge.rose { background: #dbeafe; color: #1e40af; }
.cv-honor-badge.teal { background: #dbeafe; color: #1e40af; }

/* ─── Awards ─── */
.cv-award-list { list-style: none; padding: 0; margin: 0; }
.cv-award-item {
  display: flex;
  gap: 0.8rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--gray-100);
  align-items: flex-start;
}
.cv-award-item:last-child { border-bottom: none; }
.cv-award-year {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--slate);
  min-width: 36px;
  padding-top: 2px;
}
.cv-award-content { flex: 1; }
.cv-award-name {
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--gray-800);
  line-height: 1.3;
}
.cv-award-desc {
  font-size: 0.78rem;
  color: var(--slate);
  margin-top: 0.15rem;
}

/* ─── Academic Services ─── */
.cv-service-section { margin-bottom: 1.5rem; }
.cv-service-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 0.7rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.cv-service-title::before {
  content: '';
  width: 4px; height: 16px;
  background: linear-gradient(to bottom, var(--navy), var(--teal));
  border-radius: 2px;
}
.cv-service-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.cv-service-tag {
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 500;
}
.cv-service-tag.journal {
  background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe;
}
.cv-service-tag.conference {
  background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe;
}
.cv-service-tag.org {
  background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe;
}

/* ─── Responsive ─── */
@media (max-width: 768px) {
  .cv-stats { grid-template-columns: repeat(3, 1fr); }
  .cv-honors-grid { grid-template-columns: 1fr; }
  .cv-hero-name { font-size: 1.8rem; }
  .cv-hero-contacts { gap: 0.6rem 1.2rem; }
}
@media (max-width: 480px) {
  .cv-stats { grid-template-columns: repeat(2, 1fr); }
}
</style>

<!-- ═══ Hero ═══ -->
<div class="cv-hero">
  <div class="cv-hero-inner">
    <div class="cv-hero-name">周　潘</div>
    <div class="cv-hero-name-en">Pan Zhou · Professor & Ph.D. Advisor</div>
    <div class="cv-hero-title">教授、博士生导师 · 华中科技大学 网络空间安全学院</div>
    <div class="cv-hero-inst">国家网络安全人才与创新基地建设办公室副主任（挂职副处级） · 中共党员</div>
    <div class="cv-hero-contacts">
      <span class="cv-hero-contact">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
        湖北·武汉 · 华中科技大学
      </span>
      <span class="cv-hero-contact">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        <a href="mailto:panzhou@hust.edu.cn">panzhou@hust.edu.cn</a>
      </span>
      <span class="cv-hero-contact">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.41 2 2 0 0 1 3.6 1.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.91 8.4a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21.73 17z"/></svg>
        +86-137-2027-9568
      </span>
      <span class="cv-hero-contact">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        <a href="https://scholar.google.com/citations?user=cTpFPJgAAAAJ&hl=en&oi=ao" target="_blank">Google Scholar</a>
      </span>
      <span class="cv-hero-contact">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        <a href="http://faculty.hust.edu.cn/pzhou/zh_CN/jsxx/1107001/jsxx/jsxx.htm" target="_blank">教师主页</a>
      </span>
    </div>
  </div>
</div>

<!-- ═══ Stats Strip ═══ -->
<div class="cv-stats">
  <div class="cv-stat-card highlight-teal">
    <div class="cv-stat-icon">📊</div>
    <div class="cv-stat-num">22,000+</div>
    <div class="cv-stat-label">谷歌学术<br>引用次数</div>
  </div>
  <div class="cv-stat-card highlight-blue">
    <div class="cv-stat-icon">🏆</div>
    <div class="cv-stat-num">100+</div>
    <div class="cv-stat-label">CCF-A 类论文<br>（顶会/顶刊）</div>
  </div>
  <div class="cv-stat-card">
    <div class="cv-stat-icon">📚</div>
    <div class="cv-stat-num">160+</div>
    <div class="cv-stat-label">SCI 一区<br>高质量论文</div>
  </div>
  <div class="cv-stat-card highlight-amber">
    <div class="cv-stat-icon">⭐</div>
    <div class="cv-stat-num">6/3</div>
    <div class="cv-stat-label">ESI 高被引<br>/ 1‰热点论文</div>
  </div>
  <div class="cv-stat-card highlight-rose">
    <div class="cv-stat-icon">🎖️</div>
    <div class="cv-stat-num">5 次</div>
    <div class="cv-stat-label">IEEE 最佳<br>论文奖</div>
  </div>
  <div class="cv-stat-card highlight-purple">
    <div class="cv-stat-icon">💡</div>
    <div class="cv-stat-num">14 件</div>
    <div class="cv-stat-label">已授权<br>发明专利</div>
  </div>
</div>

<!-- ═══ Research Interests ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
    </div>
    研究方向
  </div>
  <div class="cv-interest-tags">
    <span class="cv-interest-tag primary">🛡️ 原生安全世界模型</span>
    <span class="cv-interest-tag primary">🤖 具身智能安全</span>
    <span class="cv-interest-tag primary">🔒 人工智能安全</span>
  </div>
</div>

<!-- ═══ Education ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
    </div>
    教育背景
  </div>
  <div class="cv-timeline">
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot edu"></div>
      <div class="cv-timeline-date">2008 – 2011</div>
      <div class="cv-timeline-title">美国佐治亚理工学院（Georgia Tech）</div>
      <div class="cv-timeline-sub">博士 · 电气与计算机工程 · 世界前100 · 全球理工前10</div>
      <div class="cv-timeline-desc">
        <ul>
          <li>导师：John A. Copeland</li>
          <li>论文题目："Power Control and Network Capacity Analysis in Cognitive Radio Networks"</li>
        </ul>
      </div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot edu"></div>
      <div class="cv-timeline-date">2010</div>
      <div class="cv-timeline-title">美国佐治亚理工学院（Georgia Tech）</div>
      <div class="cv-timeline-sub">硕士 · 电气与计算机工程</div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot edu"></div>
      <div class="cv-timeline-date">2006 – 2008</div>
      <div class="cv-timeline-title">华中科技大学</div>
      <div class="cv-timeline-sub">硕士 · 通信工程</div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot edu"></div>
      <div class="cv-timeline-date">2002 – 2006</div>
      <div class="cv-timeline-title">华中科技大学</div>
      <div class="cv-timeline-sub">学士 · 通信与信息系统 · <strong>提高班</strong>（理工类新生入选率 65/6000+）</div>
    </div>
  </div>
</div>

<!-- ═══ Work Experience ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
    </div>
    工作经历
  </div>
  <div class="cv-timeline">
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot active"></div>
      <div class="cv-timeline-date">2020.12 – 至今</div>
      <div class="cv-timeline-title">华中科技大学 · 网络空间安全学院</div>
      <div class="cv-timeline-sub">教授、博导 · 团队负责人</div>
      <div class="cv-timeline-desc"><ul><li>研究方向：具身智能安全、人工智能安全</li><li>晋升IEEE高级会员；IEEE TNSE副编辑</li></ul></div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot"></div>
      <div class="cv-timeline-date">2024 – 2025</div>
      <div class="cv-timeline-title">武汉·国家网络安全人才与创新基地</div>
      <div class="cv-timeline-sub">建设办公室副主任（副处级、挂职）</div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot"></div>
      <div class="cv-timeline-date">2019.09 – 2020.12</div>
      <div class="cv-timeline-title">华中科技大学 · 网络空间安全学院</div>
      <div class="cv-timeline-sub">副教授、博导</div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot"></div>
      <div class="cv-timeline-date">2013.05 – 2019.08</div>
      <div class="cv-timeline-title">华中科技大学 · 电气与信息工程学院</div>
      <div class="cv-timeline-sub">副教授</div>
    </div>
    <div class="cv-timeline-item">
      <div class="cv-timeline-dot"></div>
      <div class="cv-timeline-date">2011.08 – 2013.12</div>
      <div class="cv-timeline-title">美国甲骨文公司（Oracle Inc.）</div>
      <div class="cv-timeline-sub">高级技术科学家 · 物化视图组</div>
    </div>
  </div>
</div>

<!-- ═══ Research Projects ═══ -->

<!-- ═══ Honors & Global Recognition ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
    </div>
    荣誉与成果 · 国际学术榜单
  </div>
  <div class="cv-honors-grid">
    <div class="cv-honor-card gold">
      <div class="cv-honor-year">2023–2024</div>
      <div class="cv-honor-name">ScholarGPS「全球全学科领域前 0.05% 顶尖学者」</div>
      <div class="cv-honor-org">ScholarGPS · 全球学术排名</div>
      <span class="cv-honor-badge gold">🏅 顶级荣誉</span>
    </div>
    <div class="cv-honor-card blue">
      <div class="cv-honor-year">2021–至今</div>
      <div class="cv-honor-name">Stanford「全球影响力前 2% 顶尖科学家」</div>
      <div class="cv-honor-org">斯坦福大学 · 全球科学家榜单</div>
      <span class="cv-honor-badge blue">🏅 顶级荣誉</span>
    </div>
    <div class="cv-honor-card teal">
      <div class="cv-honor-year">2023–至今</div>
      <div class="cv-honor-name">Research.com「全球最佳计算机科学家」</div>
      <div class="cv-honor-org">Research.com · 计算机科学排名</div>
      <span class="cv-honor-badge teal">🏅 顶级荣誉</span>
    </div>
    <div class="cv-honor-card purple">
      <div class="cv-honor-year">2022–至今</div>
      <div class="cv-honor-name">Aminer AI「2000 全球 AI 学者排名」</div>
      <div class="cv-honor-org">Aminer · 人工智能学者榜单</div>
      <span class="cv-honor-badge blue">🏅 顶级荣誉</span>
    </div>
  </div>
</div>

<!-- ═══ Best Paper Awards ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
    </div>
    论文获奖
  </div>
  <ul class="cv-award-list">
    <li class="cv-award-item">
      <div class="cv-award-year">2024</div>
      <div class="cv-award-content">
        <div class="cv-award-name">IEEE TIP 青年作者最佳论文奖 <span style="color:#e11d48; font-weight:700">【CCF-A · IF=13.700 · 全球年度唯一】</span></div>
        <div class="cv-award-desc">IEEE信号处理协会 · 图像处理汇刊 · IEEE Transactions on Image Processing</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2024</div>
      <div class="cv-award-content">
        <div class="cv-award-name">IEEE TETCI 杰出论文奖 <span style="color:#0d9488; font-weight:700">【SCI一区 · IF=8.380 · 全球年度唯一】</span></div>
        <div class="cv-award-desc">IEEE计算智能协会 · 计算智能前沿旗舰汇刊 · IEEE TETCI</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2023</div>
      <div class="cv-award-content">
        <div class="cv-award-name">湖北省优秀科技论文奖</div>
        <div class="cv-award-desc">IEEE TKDE（CCF-A类）/ IEEE TSE 论文 · 省部级学术奖励</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2023</div>
      <div class="cv-award-content">
        <div class="cv-award-name">IEEE ICTAI 最佳学生论文奖 <span style="color:#7c3aed; font-weight:700">【CCF-C类旗舰会议 · 获奖率 1.37%】</span></div>
        <div class="cv-award-desc">第35届国际人工智能工具会议 · IEEE International Conference on Artificial Intelligence Tools</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2020</div>
      <div class="cv-award-content">
        <div class="cv-award-name">IEEE ICPR 最佳论文奖 <span style="color:#7c3aed; font-weight:700">【CCF-C · 获奖率 0.35%】</span></div>
        <div class="cv-award-desc">第25届国际模式识别大会 · IEEE International Conference on Pattern Recognition</div>
      </div>
    </li>
  </ul>
</div>

<!-- ═══ Competition Awards ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M8 21h8m-4-4v4m-5.2-4h10.4c1.68 0 2.52 0 3.16-.33a3 3 0 0 0 1.32-1.33c.33-.64.33-1.48.33-3.16V7.2c0-1.68 0-2.52-.33-3.16a3 3 0 0 0-1.32-1.32C17.52 2.5 16.68 2.5 15 2.5H9c-1.68 0-2.52 0-3.16.33a3 3 0 0 0-1.32 1.32C4.2 4.68 4.2 5.52 4.2 7.2v5.04c0 1.68 0 2.52.33 3.16a3 3 0 0 0 1.32 1.32c.64.33 1.48.33 3.16.33z"/></svg>
    </div>
    指导学生竞赛获奖
  </div>
  <ul class="cv-award-list">
    <li class="cv-award-item">
      <div class="cv-award-year">2024</div>
      <div class="cv-award-content">
        <div class="cv-award-name">第十九届"挑战杯"竞赛"揭榜挂帅"专项赛 <strong style="color:#e11d48">一等奖</strong></div>
        <div class="cv-award-desc">国家级A类创新赛事 · 优秀指导教师</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2024</div>
      <div class="cv-award-content">
        <div class="cv-award-name">"中国网谷·华为杯"第三届中国研究生网络安全创新大赛 <strong style="color:#e11d48">一等奖</strong></div>
        <div class="cv-award-desc">国家级竞赛 · 优秀指导教师</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2024</div>
      <div class="cv-award-content">
        <div class="cv-award-name">第六届全球校园人工智能算法精英大赛全国总决赛 <strong style="color:#e11d48">一等奖</strong></div>
        <div class="cv-award-desc">优秀指导教师</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2023</div>
      <div class="cv-award-content">
        <div class="cv-award-name">第十八届"挑战杯"竞赛"揭榜挂帅"专项赛 <strong style="color:#e11d48">🏆 特等奖</strong> <span style="color:#7c3aed; font-weight:700">唯一指导教师</span></div>
        <div class="cv-award-desc">国家级A类创新赛事</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2021</div>
      <div class="cv-award-content">
        <div class="cv-award-name">第二十四届中国机器人及人工智能大赛全国总决赛 <strong style="color:#e11d48">一等奖</strong></div>
        <div class="cv-award-desc">指导教师</div>
      </div>
    </li>
  </ul>
</div>

<!-- ═══ Academic Services ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
    </div>
    学术服务与任职
  </div>

  <div class="cv-service-section">
    <div class="cv-service-title">期刊编委</div>
    <div class="cv-service-tags">
      <span class="cv-service-tag journal">📘 Elsevier Alexandria Engineering Journal（AEJ）· Editor · JCR Q1 · IF=6.800 · 2024–至今</span>
      <span class="cv-service-tag journal">📗 IEEE TNSE · Associate Editor · JCR Q1 · IF=5.213 · 2019–2023</span>
    </div>
  </div>

  <div class="cv-service-section">
    <div class="cv-service-title">CCF-A 类顶会程序委员会任职</div>
    <div class="cv-service-tags">
      <span class="cv-service-tag conference">🎯 KDD 程序委员会领域主席 · 2026</span>
      <span class="cv-service-tag conference">🎯 IJCAI 分会主席 / 高级委员 / 委员 · 多次</span>
      <span class="cv-service-tag conference">🎯 AAAI 高级委员 / 委员 / 审稿人 · 多次</span>
      <span class="cv-service-tag conference">🎯 CVPR 委员 / 审稿人 · 多次</span>
      <span class="cv-service-tag conference">🎯 ACM MM 委员 / 审稿人 · 2026</span>
      <span class="cv-service-tag conference">🎯 ICAUAS 2024 程序委员会共同主席（Co-Chairs）</span>
    </div>
  </div>

  <div class="cv-service-section">
    <div class="cv-service-title">学会/专委会任职</div>
    <div class="cv-service-tags">
      <span class="cv-service-tag org">🤝 湖北省网安学会人工智能安全专委会主任 · 2021–至今</span>
      <span class="cv-service-tag org">🤝 CCF大数据专委会执行委员 · 2023–至今</span>
      <span class="cv-service-tag org">🤝 CCF信息系统专委会执行委员 · 2023–至今</span>
      <span class="cv-service-tag org">🤝 中国工业与应用数学学会大数据与人工智能专委会委员 · 2023–2025</span>
      <span class="cv-service-tag org">🤝 IEEE 高级会员 · 2020–至今</span>
    </div>
  </div>

  <div class="cv-service-section">
    <div class="cv-service-title">重要大会报告</div>
    <div class="cv-service-tags">
      <span class="cv-service-tag conference">🎤 ICML 2024 Vienna · 分会场主题报告 · 入选率 1.49%</span>
      <span class="cv-service-tag conference">🎤 CVPR 2024 Seattle · 分会场主题报告 · 入选率 0.78%</span>
      <span class="cv-service-tag conference">🎤 ACL 2024 Bangkok · 分会场主题报告 · 入选率 3.8%</span>
      <span class="cv-service-tag conference">🎤 ACM MM 2024 Melbourne · 分会场主题报告 · 入选率 4.05%</span>
      <span class="cv-service-tag conference">🎤 ACM MM 2020 Seattle · 分会场主题报告 · 入选率 8.48%</span>
      <span class="cv-service-tag conference">🎤 CVPR 2022 New Orleans · 分会场主题报告 · 入选率 4.14%</span>
      <span class="cv-service-tag conference">🎤 CVPR 2019 Long Beach · 分会场主题报告 · 入选率 5.58%</span>
    </div>
  </div>
</div>

<!-- ═══ Other Honors ═══ -->
<div class="cv-section">
  <div class="cv-section-title">
    <div class="cv-section-title-icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
    </div>
    其他荣誉
  </div>
  <ul class="cv-award-list">
    <li class="cv-award-item">
      <div class="cv-award-year">2026</div>
      <div class="cv-award-content">
        <div class="cv-award-name">CCF-AAAI 2026「杰出程序委员奖」<span style="color:#e11d48; font-weight:700">入选率 0.16%</span></div>
        <div class="cv-award-desc">顶级会议服务奖励</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2022</div>
      <div class="cv-award-content">
        <div class="cv-award-name">湖北省科技进步奖<span style="color:#e11d48; font-weight:700">一等奖</span></div>
        <div class="cv-award-desc">《跨场景大数据分析关键技术及应用》· 获奖人（排5/15）· 第一单位教师排第3</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2022</div>
      <div class="cv-award-content">
        <div class="cv-award-name">CCF-IJCAI「服务贡献奖」</div>
        <div class="cv-award-desc">顶会服务奖励</div>
      </div>
    </li>
    <li class="cv-award-item">
      <div class="cv-award-year">2017</div>
      <div class="cv-award-content">
        <div class="cv-award-name">华中科技大学<span style="color:#e11d48; font-weight:700">科技新星</span><span style="color:#7c3aed; font-weight:700">（全校仅10人）</span></div>
        <div class="cv-award-desc">校级人才计划</div>
      </div>
    </li>
  </ul>
</div>

<div style="text-align:center; font-size:0.8rem; color:#94a3b8;">
  华中科技大学网络空间安全学院 · 原生安全世界模型实验室 · nswm-lab
</div>
