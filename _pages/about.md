---
permalink: /
title: "原生安全世界模型实验室"
author_profile: false
---

<style>
/* ═══════════════════════════════════════════
   NSWM LAB HOMEPAGE — Full-Width Overrides
   覆盖 Jekyll 主题默认布局约束，实现全宽展示
   ═══════════════════════════════════════════ */

/* 全宽基础：移除主题对 #main 的宽度限制 */
#main {
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin-top: 0 !important;
  animation: none !important;
}

/* .page 全宽 */
.page {
  width: 100% !important;
  max-width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  float: none !important;
}

/* 内部包装全宽 */
.page__inner-wrap {
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  float: none !important;
}

/* 内容区域全宽 */
.page__content {
  max-width: 100% !important;
}

/* 隐藏主题原生标题区 */
.page__inner-wrap > header {
  display: none !important;
}

/* 隐藏页面 footer/meta */
.page__meta,
.page__footer,
.page__related,
.page__footer * {
  display: none !important;
}

/* 隐藏 default.html 外层页脚容器（防漏网） */
body > .page__footer,
body > div.page__footer {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  overflow: hidden !important;
}

/* 导航栏：全链路深色覆盖，不漏任何子元素 */
.masthead {
  background: #060e1e !important;
  --global-bg-color: #060e1e !important;
  border-bottom: 1px solid rgba(255,255,255,0.07) !important;
  box-shadow: 0 2px 16px rgba(0,0,0,0.4) !important;
}
.masthead__inner-wrap {
  background: #060e1e !important;
  max-width: 100% !important;
  border-bottom: none !important;
}
.masthead__menu {
  background: transparent !important;
}
.greedy-nav {
  background: transparent !important;
  min-width: auto !important;
}
.greedy-nav .visible-links {
  background: transparent !important;
}
/* li 元素也必须强制深色，防止 SCSS var(--global-bg-color) 渗入 */
.greedy-nav .visible-links li,
.masthead__menu-item {
  background: #060e1e !important;
  background-color: #060e1e !important;
}
/* 第一个导航项（大标题样式）也强制深色 */
.masthead__menu-item--lg {
  background: #060e1e !important;
  background-color: #060e1e !important;
}

/* 导航链接文字样式 */
.greedy-nav .visible-links li a,
.masthead__menu-item a,
.greedy-nav button {
  color: rgba(255,255,255,0.82) !important;
  text-decoration: none !important;
  background: transparent !important;
}
.greedy-nav .visible-links li a:hover,
.masthead__menu-item a:hover {
  color: #5eead4 !important;
}
.masthead__menu-item.selected a {
  color: #5eead4 !important;
}
.greedy-nav .visible-links li:first-child a {
  color: #ffffff !important;
  font-weight: 700 !important;
}

/* body 不再需要顶部 padding（导航固定覆盖） */
body {
  padding-top: 0 !important;
}

/* ═══════════════════════════════════════════
   NSWM LAB HOMEPAGE — Custom Styles
   ═══════════════════════════════════════════ */

:root {
  --navy:      #0a1628;
  --blue-deep: #0f2744;
  --blue-mid:  #1a3a6b;
  --teal:      #0d9488;
  --teal-light:#14b8a6;
  --amber:     #f59e0b;
  --rose:      #e11d48;
  --purple:    #7c3aed;
  --white:     #ffffff;
  --gray-50:   #f8fafc;
  --gray-100:  #f1f5f9;
  --gray-200:  #e2e8f0;
  --gray-400:  #94a3b8;
  --gray-600:  #475569;
  --gray-800:  #1e293b;
  --shadow-md: 0 4px 16px rgba(0,0,0,0.12);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.18);
  --radius-lg: 16px;
  --radius-md: 10px;
  --radius-sm: 6px;
}

/* ─── Page Reset ─── */
.lab-page { font-family: 'PingFang SC','Microsoft YaHei',Arial,sans-serif; color: var(--gray-800); line-height: 1.7; }
.lab-page *, .lab-page *::before, .lab-page *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* ─── WIDE LAYOUT ─── */
/* 版心加宽：1200px → 1440px，适配现代大屏 */
.lab-page-wrap {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 3rem;
}

/* ─── HERO ─── */
.lab-hero {
  background: linear-gradient(135deg, #060e1e 0%, #0f2744 40%, #1a3a6b 100%);
  color: var(--white);
  padding: 0;
  position: relative;
  overflow: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  /* 底部柔和过渡到内容区 */
  mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 85%, transparent 100%);
}
.lab-hero::before {
  content: '';
  position: absolute;
  top: -120px; right: -80px;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(13,148,136,0.18) 0%, transparent 65%);
  border-radius: 50%;
  pointer-events: none;
}
.lab-hero::after {
  content: '';
  position: absolute;
  bottom: -160px; left: 5%;
  width: 800px; height: 800px;
  background: radial-gradient(circle, rgba(59,130,246,0.1) 0%, transparent 60%);
  border-radius: 50%;
  pointer-events: none;
}

/* Grid background pattern */
.lab-hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
}

/* Floating particles */
.lab-particle {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  animation: lab-float 6s ease-in-out infinite;
}
@keyframes lab-float {
  0%, 100% { transform: translateY(0px) scale(1); opacity: 0.4; }
  50% { transform: translateY(-20px) scale(1.1); opacity: 0.7; }
}

.lab-hero-inner {
  position: relative;
  z-index: 1;
  max-width: 1440px;
  margin: 0 auto;
  padding: 5rem 3rem 3rem;
  width: 100%;
  display: flex;
  gap: 4rem;
  align-items: center;
  flex: 1;
}

.lab-hero-left {
  flex: 1;
  min-width: 0;
}

/* Hero 右卡：扩大并丰富内容，消灭右侧空白 */
.lab-hero-right {
  flex-shrink: 0;
  width: 400px;
  animation: lab-fadeIn 1s ease 0.5s both;
}
.lab-hero-card {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 24px;
  padding: 3rem 2.5rem;
  backdrop-filter: blur(20px);
  text-align: center;
}

.lab-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(13,148,136,0.15);
  border: 1px solid rgba(13,148,136,0.4);
  color: #5eead4;
  padding: 0.35rem 1rem;
  border-radius: 50px;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
  animation: lab-fadeIn 0.8s ease;
}
.lab-hero-badge-dot {
  width: 6px; height: 6px;
  background: #5eead4;
  border-radius: 50%;
  animation: lab-pulse 2s infinite;
}
@keyframes lab-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(1.3); }
}
@keyframes lab-fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.lab-hero-title-zh {
  font-size: clamp(2.2rem, 4.5vw, 3.8rem);
  font-weight: 900;
  letter-spacing: 0.04em;
  line-height: 1.15;
  margin-bottom: 0.6rem;
  white-space: nowrap;
  animation: lab-fadeIn 0.8s ease 0.1s both;
}
.lab-hero-title-en {
  font-size: 1.2rem;
  color: rgba(255,255,255,0.5);
  font-weight: 400;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 2rem;
  animation: lab-fadeIn 0.8s ease 0.2s both;
}
.lab-hero-desc {
  font-size: 1.15rem;
  color: rgba(255,255,255,0.78);
  line-height: 1.85;
  margin-bottom: 2.5rem;
  max-width: 720px;
  animation: lab-fadeIn 0.8s ease 0.3s both;
}
.lab-hero-desc strong { color: #5eead4; }

.lab-hero-stats {
  display: flex;
  gap: 2.5rem;
  flex-wrap: wrap;
  animation: lab-fadeIn 0.8s ease 0.4s both;
}
.lab-hero-stat {
  text-align: left;
}
.lab-hero-stat-num {
  font-size: 2.4rem;
  font-weight: 900;
  color: var(--teal-light);
  line-height: 1;
}
.lab-hero-stat-label {
  font-size: 0.8rem;
  color: rgba(255,255,255,0.5);
  margin-top: 0.3rem;
  letter-spacing: 0.05em;
}
.lab-hero-stat-div {
  width: 1px;
  background: rgba(255,255,255,0.12);
  align-self: stretch;
}

.lab-hero-card { }
.lab-hero-avatar {
  width: 240px;
  height: 240px;
  border-radius: 50%;
  border: 5px solid #5eead4;
  margin: 0 auto 1.5rem;
  overflow: hidden;
  box-shadow: 0 0 0 6px rgba(94,234,212,0.22), 0 6px 28px rgba(0,0,0,0.55);
}
/* 照片填满圆形容器 */
.lab-hero-avatar img {
  width: 100%; height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
.lab-hero-name {
  font-size: 1.7rem;
  font-weight: 800;
  margin-bottom: 0.2rem;
  color: #ffffff;
}
.lab-hero-role {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.72);
  margin-bottom: 0.8rem;
}
.lab-hero-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255,255,255,0.1);
}
.lab-hero-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.78rem;
  color: rgba(255,255,255,0.6);
  text-decoration: none;
  transition: color 0.2s;
  justify-content: center;
}
.lab-hero-link:hover { color: #5eead4; }
.lab-hero-link svg { width: 14px; height: 14px; }

/* Hero scroll indicator */
.lab-hero-scroll {
  /* removed */
}
/* Hero 底部渐变过渡线 */
.lab-hero-bottom-fade {
  position: relative;
  z-index: 1;
  height: 120px;
  background: linear-gradient(to bottom, transparent, var(--gray-50));
  pointer-events: none;
}
/* ─── SECTION COMMON ─── */
.lab-section {
  max-width: 1440px;
  margin: 0 auto;
  padding: 5rem 3rem;
}
.lab-section-dark {
  background: var(--gray-50);
}
.lab-section-title {
  text-align: center;
  margin-bottom: 3rem;
}
.lab-section-title-zh {
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 0.4rem;
  letter-spacing: 0.04em;
}
.lab-section-title-en {
  font-size: 0.85rem;
  color: var(--gray-400);
  text-transform: uppercase;
  letter-spacing: 0.15em;
}
.lab-section-divider {
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, var(--blue-mid), var(--teal));
  border-radius: 3px;
  margin: 1rem auto 0;
}

/* ─── ABOUT PROFESSOR ─── */
.lab-about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: stretch;
}
.lab-about-concept {
  background: linear-gradient(135deg, var(--navy), var(--blue-deep));
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  color: white;
  position: relative;
  overflow: hidden;
}
.lab-about-concept::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(13,148,136,0.2), transparent 70%);
  border-radius: 50%;
}
.lab-concept-tag {
  display: inline-block;
  background: rgba(13,148,136,0.2);
  border: 1px solid rgba(13,148,136,0.5);
  color: #5eead4;
  padding: 0.2rem 0.8rem;
  border-radius: 50px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  margin-bottom: 1rem;
}
.lab-concept-title {
  font-size: 1.3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  line-height: 1.4;
}
.lab-concept-text {
  font-size: 0.98rem;
  color: rgba(255,255,255,0.78);
  line-height: 1.85;
  margin-bottom: 1.2rem;
}
.lab-concept-text:last-child { margin-bottom: 0; }
.lab-concept-highlight {
  background: rgba(13,148,136,0.15);
  border-left: 3px solid var(--teal-light);
  padding: 0.8rem 1rem;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  font-size: 0.88rem;
  color: rgba(255,255,255,0.85);
  line-height: 1.7;
  margin-top: 1rem;
}

.lab-about-info {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.lab-about-info-item {
  padding: 1.2rem 0;
  border-bottom: 1px solid var(--gray-200);
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}
.lab-about-info-item:first-child { padding-top: 0; }
.lab-about-info-item:last-child { border-bottom: none; }
.lab-about-info-icon {
  width: 40px; height: 40px;
  border-radius: var(--radius-sm);
  background: linear-gradient(135deg, #eff6ff, #dbeafe);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  font-size: 1.1rem;
}
.lab-about-info-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 0.2rem;
}
.lab-about-info-desc {
  font-size: 0.85rem;
  color: var(--gray-600);
  line-height: 1.6;
}
.lab-about-info-desc a { color: var(--blue-mid); text-decoration: none; }
.lab-about-info-desc a:hover { text-decoration: underline; }

/* ─── BADVLA SECTION ─── */
#research { scroll-margin-top: 80px; }

.lab-badvla-header {
  text-align: center;
  margin-bottom: 3rem;
}
.lab-badvla-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #fff7ed, #fff1f2);
  border: 1.5px solid #fed7aa;
  color: #c2410c;
  padding: 0.3rem 1rem;
  border-radius: 50px;
  font-size: 0.78rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.lab-badvla-badge-star { color: var(--amber); }

.lab-badvla-paper-card {
  background: white;
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  overflow: hidden;
  margin-bottom: 2rem;
}

.lab-badvla-fig {
  width: 100%;
  background: var(--gray-100);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}
.lab-badvla-fig img {
  width: 100%;
  max-width: 1200px;
  border-radius: var(--radius-md);
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.lab-badvla-content { padding: 2.5rem 3rem; }

.lab-badvla-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.2rem;
}
.lab-badvla-tag {
  padding: 0.2rem 0.75rem;
  border-radius: 50px;
  font-size: 0.72rem;
  font-weight: 700;
}
.lab-badvla-tag.venue { background: #eff6ff; color: #1e40af; border: 1px solid #bfdbfe; }
.lab-badvla-tag.security { background: #fff7ed; color: #c2410c; border: 1px solid #fed7aa; }
.lab-badvla-tag.vla { background: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
.lab-badvla-tag.arxiv { background: #f5f3ff; color: #6b21a8; border: 1px solid #ddd6fe; }

.lab-badvla-title {
  font-size: clamp(1.3rem, 2.5vw, 1.85rem);
  font-weight: 800;
  color: var(--navy);
  line-height: 1.35;
  margin-bottom: 0.6rem;
}
.lab-badvla-authors {
  font-size: 0.85rem;
  color: var(--gray-600);
  margin-bottom: 1.5rem;
}
.lab-badvla-authors .me { color: var(--blue-mid); font-weight: 700; }

.lab-badvla-abstract {
  background: var(--gray-50);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  border-left: 4px solid var(--blue-mid);
}
.lab-badvla-abstract-label {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--gray-400);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.6rem;
}
.lab-badvla-abstract-text {
  font-size: 0.9rem;
  color: var(--gray-600);
  line-height: 1.8;
}

.lab-badvla-method {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1.5rem;
}
.lab-badvla-method-card {
  background: white;
  border: 1.5px solid var(--gray-200);
  border-radius: var(--radius-md);
  padding: 1.2rem;
  position: relative;
  overflow: hidden;
}
.lab-badvla-method-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
}
.lab-badvla-method-card.stage1::before { background: linear-gradient(90deg, var(--rose), #fb7185); }
.lab-badvla-method-card.stage2::before { background: linear-gradient(90deg, var(--teal), #14b8a6); }
.lab-badvla-method-num {
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--gray-400);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.3rem;
}
.lab-badvla-method-name {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 0.4rem;
}
.lab-badvla-method-desc {
  font-size: 0.82rem;
  color: var(--gray-600);
  line-height: 1.6;
}

.lab-badvla-results {
  background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
  border: 1.5px solid #bbf7d0;
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}
.lab-badvla-results-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: #15803d;
  margin-bottom: 0.8rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.lab-badvla-result-list {
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
}
.lab-badvla-result-item {
  display: flex;
  align-items: flex-start;
  gap: 0.4rem;
  font-size: 0.82rem;
  color: #166534;
}
.lab-badvla-result-item .icon { color: #22c55e; font-size: 1rem; flex-shrink: 0; margin-top: 1px; }

.lab-badvla-links {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}
.lab-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.6rem 1.4rem;
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.2s;
  border: none;
  cursor: pointer;
}
.lab-btn-primary {
  background: linear-gradient(135deg, var(--blue-mid), var(--teal));
  color: white;
  box-shadow: 0 4px 12px rgba(13,148,136,0.3);
}
.lab-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(13,148,136,0.4); }
.lab-btn-outline {
  background: white;
  color: var(--blue-mid);
  border: 1.5px solid var(--blue-mid);
}
.lab-btn-outline:hover { background: #eff6ff; transform: translateY(-2px); }
.lab-btn svg { width: 15px; height: 15px; }

/* ─── BADVLA VIDEO DEMO ─── */
.lab-badvla-demo {
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid var(--gray-200);
  margin-bottom: 0.5rem;
}
.lab-badvla-demo-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 0.3rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.lab-badvla-demo-title::before {
  content: '🎬';
}
.lab-badvla-demo-subtitle {
  font-size: 0.75rem;
  color: var(--gray-500);
  margin-bottom: 1.2rem;
  line-height: 1.6;
}
/* 按场景分组的标题行 */
.lab-badvla-demo-group-title {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--blue-mid);
  margin-bottom: 0.6rem;
  margin-top: 1.2rem;
  padding-left: 0.15rem;
}
.lab-badvla-demo-group-title:first-of-type {
  margin-top: 0;
}
/* 每行4个视频的网格 */
.lab-badvla-demo-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.8rem;
  margin-bottom: 0.6rem;
}
/* 2列变体（Google Robot 单任务只有2个视频时） */
.lab-badvla-demo-grid--2 {
  grid-template-columns: repeat(2, 1fr);
  max-width: 66%;
}
/* 4列：Google Robot 合并展示6个视频 */
.lab-badvla-demo-card {
  background: #f8fafc;
  border-radius: var(--radius-sm);
  overflow: hidden;
  border: 1px solid #e2e8f0;
  transition: all 0.3s;
}
.lab-badvla-demo-card:hover {
  border-color: var(--teal);
  box-shadow: 0 2px 10px rgba(13,148,136,0.12);
  transform: translateY(-2px);
}
/* 视频容器：保持原始比例，用 contain 避免裁剪 */
.lab-badvla-demo-video-wrap {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #0f172a;
  overflow: hidden;
}
.lab-badvla-demo-video-wrap video {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
  object-fit: contain;
  border: none;
}
.lab-badvla-demo-card-body {
  padding: 0.55rem 0.7rem;
}
.lab-badvla-demo-card-label {
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  margin-bottom: 0.15rem;
}
.lab-badvla-demo-card-label.normal {
  color: #15803d;
  background: #dcfce7;
  display: inline-block;
  padding: 0.08rem 0.4rem;
  border-radius: 50px;
}
.lab-badvla-demo-card-label.trigger {
  color: #dc2626;
  background: #fee2e2;
  display: inline-block;
  padding: 0.08rem 0.4rem;
  border-radius: 50px;
}
.lab-badvla-demo-card-desc {
  font-size: 0.7rem;
  color: var(--gray-600);
  line-height: 1.45;
}

/* ─── MORE PAPERS GRID ─── */
.lab-papers-section { margin-top: 2.5rem; }
.lab-papers-section-title {
  font-size: 1rem;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 0.6rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #14b8a6;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.lab-papers-intro {
  font-size: 0.82rem;
  color: #334155;
  line-height: 1.85;
  margin-bottom: 1.4rem;
  padding: 1rem 1.2rem;
  background: linear-gradient(135deg, #f0fdfa, #f8fafc);
  border-left: 3px solid #14b8a6;
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
}
.lab-papers-intro strong {
  color: #0d9488;
  font-weight: 700;
}
.lab-papers-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.4rem;
}
.lab-paper-card {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: var(--radius-md);
  overflow: hidden;
  transition: all 0.35s;
  box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 4px 20px rgba(0,0,0,0.06);
}
.lab-paper-card:hover {
  border-color: #14b8a6;
  box-shadow: 0 8px 30px rgba(13,148,136,0.15), 0 1px 3px rgba(0,0,0,0.08);
  transform: translateY(-4px);
}
.lab-paper-card-fig {
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: #f1f5f9;
  border-bottom: 2px solid #e2e8f0;
}
.lab-paper-card-fig img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  background: #fff;
  display: block;
}
.lab-paper-card-body {
  padding: 1rem 1.15rem;
}
.lab-paper-card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-bottom: 0.5rem;
}
.lab-paper-card-tag {
  font-size: 0.62rem;
  font-weight: 700;
  padding: 0.1rem 0.45rem;
  border-radius: 50px;
  color: #fff;
  letter-spacing: 0.02em;
}
.lab-paper-card-tag.venue-ndss { background: #dc2626; }
.lab-paper-card-tag.venue-cvpr { background: #7c3aed; }
.lab-paper-card-tag.venue-acl { background: #2563eb; }
.lab-paper-card-tag.venue-neurips { background: #059669; }
.lab-paper-card-tag.venue-iclr { background: #d97706; }
.lab-paper-card-tag.venue-tnnls { background: #be185d; }
.lab-paper-card-title {
  font-size: 0.85rem;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.45;
  margin-bottom: 0.35rem;
}
.lab-paper-card-authors {
  font-size: 0.72rem;
  color: #64748b;
  margin-bottom: 0.55rem;
}
.lab-paper-card-desc {
  font-size: 0.75rem;
  color: #334155;
  line-height: 1.75;
  margin-bottom: 0.6rem;
}
.lab-paper-card-links {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}
.lab-paper-card-links a {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.2rem 0.6rem;
  border-radius: 50px;
  background: rgba(13,148,136,0.08);
  color: #0d9488;
  text-decoration: none;
  transition: all 0.25s;
  white-space: nowrap;
  border: 1px solid rgba(13,148,136,0.15);
}
.lab-paper-card-links a:hover {
  background: rgba(13,148,136,0.18);
  border-color: rgba(13,148,136,0.35);
}
@media (max-width: 1024px) {
  .lab-papers-grid { grid-template-columns: 1fr; }
}

/* ─── RESEARCH DIRECTIONS ─── */
.lab-directions-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}
.lab-direction-card {
  background: white;
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-md);
  transition: all 0.3s;
  border: 1.5px solid transparent;
  position: relative;
}
.lab-direction-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--teal);
}
.lab-direction-card.priority::after {
  content: '⭐ 核心重点';
  position: absolute;
  top: 1rem; right: 1rem;
  background: linear-gradient(135deg, var(--amber), #fbbf24);
  color: white;
  font-size: 0.65rem;
  font-weight: 800;
  padding: 0.2rem 0.6rem;
  border-radius: 50px;
  letter-spacing: 0.05em;
}
.lab-direction-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}
.lab-direction-body {
  padding: 1.5rem;
}
.lab-direction-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.lab-direction-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 0.5rem;
}
.lab-direction-desc {
  font-size: 0.82rem;
  color: var(--gray-600);
  line-height: 1.7;
}
.lab-direction-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 0.8rem;
}
.lab-direction-tag {
  padding: 0.15rem 0.6rem;
  background: var(--gray-100);
  color: var(--gray-600);
  border-radius: 50px;
  font-size: 0.7rem;
  font-weight: 500;
}

/* ─── NEWS / ANNOUNCEMENTS ─── */
.lab-news-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}
.lab-news-card {
  background: white;
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-md);
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}
.lab-news-date {
  text-align: center;
  min-width: 50px;
  flex-shrink: 0;
}
.lab-news-month {
  font-size: 0.7rem;
  color: var(--teal);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}
.lab-news-day {
  font-size: 1.6rem;
  font-weight: 900;
  color: var(--navy);
  line-height: 1;
}
.lab-news-content {}
.lab-news-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--gray-800);
  margin-bottom: 0.3rem;
  line-height: 1.4;
}
.lab-news-desc {
  font-size: 0.8rem;
  color: var(--gray-400);
}

/* ─── JOIN US ─── */
.lab-join {
  background: linear-gradient(135deg, var(--navy), var(--blue-deep));
  border-radius: var(--radius-lg);
  padding: 4rem 3rem;
  text-align: center;
  color: white;
  position: relative;
  overflow: hidden;
}
.lab-join::before {
  content: '';
  position: absolute;
  top: -80px; right: -80px;
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(13,148,136,0.2), transparent 70%);
  border-radius: 50%;
}
.lab-join-title {
  font-size: 2.4rem;
  font-weight: 800;
  margin-bottom: 0.6rem;
  position: relative;
}
.lab-join-sub {
  font-size: 1rem;
  color: rgba(255,255,255,0.6);
  margin-bottom: 2.5rem;
  position: relative;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
.lab-join-cards {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
  position: relative;
}
.lab-join-card {
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: var(--radius-md);
  padding: 2rem;
  width: 280px;
  text-align: left;
  transition: all 0.3s;
}
.lab-join-card:hover {
  background: rgba(255,255,255,0.12);
  transform: translateY(-4px);
  border-color: rgba(13,148,136,0.4);
}
.lab-join-card-icon { font-size: 2rem; margin-bottom: 0.6rem; }
.lab-join-card-title { font-size: 1rem; font-weight: 700; margin-bottom: 0.4rem; }
.lab-join-card-desc { font-size: 0.85rem; color: rgba(255,255,255,0.55); line-height: 1.7; }
.lab-join-contact {
  margin-top: 2.5rem;
  position: relative;
}
.lab-join-email {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(13,148,136,0.2);
  border: 1px solid rgba(13,148,136,0.4);
  color: #5eead4;
  padding: 0.75rem 2rem;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
}
.lab-join-email:hover { background: rgba(13,148,136,0.3); transform: translateY(-2px); }

/* ─── FOOTER ─── */
.lab-footer {
  background: #060e1e;
  color: rgba(255,255,255,0.4);
  text-align: center;
  padding: 2.5rem;
  font-size: 0.85rem;
}
.lab-footer a { color: rgba(255,255,255,0.6); text-decoration: none; }
.lab-footer a:hover { color: #5eead4; }

/* ─── RESPONSIVE ─── */
@media (max-width: 1280px) {
  .lab-hero-inner { padding: 4rem 2rem 3rem; gap: 2.5rem; }
  .lab-hero-right { width: 300px; }
  .lab-section { padding: 4rem 2rem; }
}
@media (max-width: 1024px) {
  .lab-hero-inner {
    flex-direction: column;
    text-align: center;
    padding: 3rem 2rem 2.5rem;
    gap: 2rem;
  }
  .lab-hero-right { width: 100%; max-width: 400px; }
  .lab-hero-desc { max-width: 100%; margin-left: auto; margin-right: auto; }
  .lab-hero-stats { justify-content: center; gap: 2rem; }
  .lab-about-grid { grid-template-columns: 1fr; gap: 2rem; }
  .lab-directions-grid { grid-template-columns: repeat(2, 1fr); }
  .lab-badvla-method { grid-template-columns: 1fr; }
  .lab-badvla-result-list { grid-template-columns: 1fr 1fr; }
  .lab-news-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 768px) {
  .lab-hero-title-zh { font-size: 2rem; white-space: normal; }
  .lab-hero-stats { gap: 1.5rem; }
  .lab-hero-stat-num { font-size: 1.8rem; }
  .lab-badvla-result-list { grid-template-columns: 1fr; }
  .lab-directions-grid { grid-template-columns: 1fr; }
  .lab-news-grid { grid-template-columns: 1fr; }
  .lab-join-cards { flex-direction: column; align-items: center; }
  .lab-join-card { width: 100%; max-width: 360px; }
  .lab-section { padding: 3rem 1.5rem; }
  .lab-hero-inner { padding: 3rem 1.5rem 2.5rem; }
}
</style>

<!-- ══════════════════════════════════════════════
     SECTION 1: HERO
     ══════════════════════════════════════════════ -->
<div class="lab-hero">
  <div class="lab-hero-grid"></div>

  <!-- Floating particles -->
  <div class="lab-particle" style="width:6px;height:6px;background:rgba(13,148,136,0.5);top:20%;left:10%;animation-delay:0s;"></div>
  <div class="lab-particle" style="width:10px;height:10px;background:rgba(59,130,246,0.3);top:60%;left:80%;animation-delay:2s;"></div>
  <div class="lab-particle" style="width:8px;height:8px;background:rgba(13,148,136,0.4);top:75%;left:25%;animation-delay:4s;"></div>
  <div class="lab-particle" style="width:5px;height:5px;background:rgba(59,130,246,0.4);top:35%;left:70%;animation-delay:1s;"></div>

  <div class="lab-hero-inner">
    <div class="lab-hero-left">
      <div class="lab-hero-badge">
        <span class="lab-hero-badge-dot"></span>
        华中科技大学 · 网络空间安全学院
      </div>
      <h1 class="lab-hero-title-zh">原生安全世界模型实验室</h1>
      <div class="lab-hero-title-en">Native Secure World Model Laboratory</div>
      <p class="lab-hero-desc">
        致力于将<strong>安全约束内生融入世界建模</strong>，使 AI 系统能够同步预测环境演化、识别潜在风险、阻断危险因果链。<br>
        面向<strong>具身智能、自动驾驶、机器人控制、LLM Agent</strong>等高风险场景，构建可信赖的原生安全智能。
      </p>
      <div class="lab-hero-stats">
        <div class="lab-hero-stat">
          <div class="lab-hero-stat-num">22,000+</div>
          <div class="lab-hero-stat-label">谷歌学术引用</div>
        </div>
        <div class="lab-hero-stat-div"></div>
        <div class="lab-hero-stat">
          <div class="lab-hero-stat-num">100+</div>
          <div class="lab-hero-stat-label">CCF-A 类顶会论文</div>
        </div>
        <div class="lab-hero-stat-div"></div>
        <div class="lab-hero-stat">
          <div class="lab-hero-stat-num">6+3</div>
          <div class="lab-hero-stat-label">ESI 高被引 / 热点论文</div>
        </div>
        <div class="lab-hero-stat-div"></div>
        <div class="lab-hero-stat">
          <div class="lab-hero-stat-num">1,500万+</div>
          <div class="lab-hero-stat-label">近5年主持科研经费</div>
        </div>
      </div>
    </div>

    <div class="lab-hero-right">
      <div class="lab-hero-card">
        <div class="lab-hero-avatar">
          <img src="/images/profile.png" alt="周潘教授"
               style="border-radius:50%;object-fit:cover;border:3px solid rgba(13,148,136,0.5);box-shadow:0 0 0 4px rgba(13,148,136,0.15);">
        </div>
        <div class="lab-hero-name">周　潘</div>
        <div class="lab-hero-role">Pan Zhou · 教授、博导</div>
        <div style="font-size:0.78rem;color:rgba(255,255,255,0.5);margin-bottom:1rem;">华中科技大学 · 网络空间安全学院</div>

        <!-- 快速统计 -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;margin-bottom:1rem;">
          <div style="background:rgba(13,148,136,0.15);border:1px solid rgba(13,148,136,0.25);border-radius:10px;padding:0.6rem 0.5rem;">
            <div style="font-size:1.4rem;font-weight:900;color:#5eead4;line-height:1;">22K+</div>
            <div style="font-size:0.65rem;color:rgba(255,255,255,0.5);margin-top:0.2rem;">学术引用</div>
          </div>
          <div style="background:rgba(124,58,237,0.15);border:1px solid rgba(124,58,237,0.25);border-radius:10px;padding:0.6rem 0.5rem;">
            <div style="font-size:1.4rem;font-weight:900;color:#a78bfa;line-height:1;">100+</div>
            <div style="font-size:0.65rem;color:rgba(255,255,255,0.5);margin-top:0.2rem;">CCF-A论文</div>
          </div>
          <div style="background:rgba(245,158,11,0.15);border:1px solid rgba(245,158,11,0.25);border-radius:10px;padding:0.6rem 0.5rem;">
            <div style="font-size:1.4rem;font-weight:900;color:#fbbf24;line-height:1;">6+3</div>
            <div style="font-size:0.65rem;color:rgba(255,255,255,0.5);margin-top:0.2rem;">ESI高被引</div>
          </div>
          <div style="background:rgba(225,29,72,0.15);border:1px solid rgba(225,29,72,0.25);border-radius:10px;padding:0.6rem 0.5rem;">
            <div style="font-size:1.4rem;font-weight:900;color:#fb7185;line-height:1;">1,500W+</div>
            <div style="font-size:0.65rem;color:rgba(255,255,255,0.5);margin-top:0.2rem;">科研经费</div>
          </div>
        </div>

        <div class="lab-hero-links">
          <a class="lab-hero-link" href="mailto:panzhou@hust.edu.cn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            panzhou@hust.edu.cn
          </a>
          <a class="lab-hero-link" href="https://scholar.google.com/citations?user=cTpFPJgAAAAJ&hl=en" target="_blank">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            Google Scholar
          </a>
          <a class="lab-hero-link" href="https://github.com/Zxy-MLlab" target="_blank">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            Zxy-MLlab
          </a>
          <a class="lab-hero-link" href="https://badvla-project.github.io/" target="_blank">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            BadVLA 项目
          </a>
        </div>
      </div>
    </div>
  </div>

  <div class="lab-hero-bottom-fade"></div>
</div>

<!-- ══════════════════════════════════════════════
     SECTION 2: ABOUT PROFESSOR & CONCEPT
     ══════════════════════════════════════════════ -->
<div class="lab-section">
  <div class="lab-section-title">
    <div class="lab-section-title-en">01 · Professor &amp; Concept</div>
    <div class="lab-section-title-zh">实验室主任 &amp; 核心研究理念</div>
    <div class="lab-section-divider"></div>
  </div>

  <div class="lab-about-grid">
    <!-- Left: Native Secure World Model Concept -->
    <div class="lab-about-concept">
      <div class="lab-concept-tag">🔐 全球首创</div>
      <h2 class="lab-concept-title" style="font-size:1.6rem;">原生安全世界模型<br><span style="color:#0d9488;">Native Secure World Model</span></h2>
      <p class="lab-concept-text">
        传统 AI 安全方案多采用"外挂式"防护——在模型训练完成后额外叠加安全过滤层。这种方式不仅治标不治本，更在高风险、长周期交互场景中暴露根本性缺陷。
      </p>
      <p class="lab-concept-text">
        <strong style="color:#0d9488;">原生安全世界模型</strong>由周潘教授在全球范围内首次提出，核心理念是：
      </p>
      <p class="lab-concept-text">
        将安全约束作为一等公民内生融入世界建模全过程，使模型在预测物理环境演化与智能体行为后果的同时，同步构建<strong style="color:#0d9488;">风险识别、违规检测、危险因果链阻断</strong>三大原生安全能力。
      </p>
      <div class="lab-concept-highlight">
        ⚡ <strong>为何重要：</strong>具身智能、自动驾驶、机器人控制、LLM Agent 等系统需在真实或高风险环境中长期交互，每一步行为都关乎安全责任——必须从"基因"层面内置安全，而非事后打补丁。
      </div>
    </div>

    <!-- Right: PI Info -->
    <div class="lab-about-info">
      <div class="lab-about-info-item">
        <div class="lab-about-info-icon">👨‍🎓</div>
        <div>
          <div class="lab-about-info-title">周潘 教授 · Pan Zhou</div>
          <div class="lab-about-info-desc">
            华中科技大学网络空间安全学院教授、博士生导师。<br>
            国家网络安全人才与创新基地建设办公室副主任（挂职副处级）。<br>
            美国佐治亚理工学院（Georgia Tech）博士，国际电气与电子工程师协会高级会员（IEEE Senior Member）。
          </div>
        </div>
      </div>
      <div class="lab-about-info-item">
        <div class="lab-about-info-icon">🏆</div>
        <div>
          <div class="lab-about-info-title">国际学术荣誉</div>
          <div class="lab-about-info-desc">
            🌍 ScholarGPS「全球前 0.05% 顶尖学者」（2023–2024）<br>
            🌍 Stanford「全球前 2% 顶尖科学家」（2021–至今）<br>
            🌍 Research.com「全球最佳计算机科学家」（2023–至今）<br>
            🌍 Aminer AI「全球 AI 2000 学者」（2022–至今）
          </div>
        </div>
      </div>
      <div class="lab-about-info-item">
        <div class="lab-about-info-icon">💡</div>
        <div>
          <div class="lab-about-info-title">代表性科研项目</div>
          <div class="lab-about-info-desc">
            🔹 国家级重点专项「多模态安全融合技术」· 470万元 · 2022–2027<br>
            🔹 海军装备部项目「智能规划算法」· 120万元 · 2024–2027<br>
            🔹 国自然面上项目「多模态大模型幻觉与对齐安全」· 50万元 · 2025–2028<br>
            🔹 近5年主持科研总经费 <strong>超过 1,500 万元</strong>
          </div>
        </div>
      </div>
      <div class="lab-about-info-item">
        <div class="lab-about-info-icon">🎓</div>
        <div>
          <div class="lab-about-info-title">顶级期刊/会议服务</div>
          <div class="lab-about-info-desc">
            📘 Elsevier AEJ · Editor（IF=6.8，JCR Q1）<br>
            📗 IEEE TNSE · Associate Editor（IF=5.2，JCR Q1）<br>
            🎯 KDD 2026 · 程序委员会领域主席<br>
            🎯 IJCAI/AAAI/CVPR/ACM MM · 多次 CCF-A 顶会程序委员
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     SECTION 3: BADVLA RESEARCH HIGHLIGHT
     ══════════════════════════════════════════════ -->
<div class="lab-section lab-section-dark" id="research">
  <div class="lab-badvla-header">
    <div class="lab-section-title-en">02 · Featured Research</div>
    <div class="lab-section-title-zh">代表性成果 · BadVLA</div>
    <div class="lab-section-divider"></div>
  </div>

  <div class="lab-badvla-paper-card">
    <!-- Framework Figure -->
    <div class="lab-badvla-fig">
      <img src="https://raw.githubusercontent.com/Zxy-MLlab/BadVLA/master/figures/overview.png"
           alt="BadVLA Objective-Decoupled Training Framework Overview"
           title="BadVLA: Objective-Decoupled Training Framework for Backdoor Attacks on Vision-Language-Action Models"
           loading="lazy" />
    </div>

    <div class="lab-badvla-content">
      <!-- Paper badges -->
      <div class="lab-badvla-meta">
        <span class="lab-badvla-tag arxiv">📄 arXiv:2505.16640</span>
        <span class="lab-badvla-tag security">🔒 VLA 安全 / 后门攻击</span>
        <span class="lab-badvla-tag vla">🤖 视觉-语言-动作模型</span>
        <span class="lab-badvla-tag venue">🎯 HUST × Lehigh University</span>
      </div>

      <!-- Title -->
      <h2 class="lab-badvla-title">
        BadVLA: Towards Backdoor Attacks on Vision-Language-Action Models<br>via Objective-Decoupled Optimization
      </h2>

      <!-- Authors -->
      <div class="lab-badvla-authors">
        Xueyang Zhou, Guiyao Tie, Guowen Zhang, Hecheng Wang,
        <span class="me">Pan Zhou</span>, Lichao Sun
        &nbsp;·&nbsp;
        <em>HUST</em> &amp; <em>Lehigh University</em>, 2025
      </div>

      <!-- Abstract -->
      <div class="lab-badvla-abstract">
        <div class="lab-badvla-abstract-label">📝 摘要</div>
        <div class="lab-badvla-abstract-text">
          Vision-Language-Action (VLA) 模型通过端到端多模态输入直接驱动机器人决策，代表了具身智能的重要突破。然而，其紧耦合架构也催生了新型安全威胁。<strong>后门攻击</strong>（Backdoor Attack）相比传统对抗扰动更具隐蔽性、持续性，尤其在"训练即服务"（Training-as-a-Service）范式下威胁更为突出，但在 VLA 领域几乎未被探索。
          <br><br>
          我们首次提出 <strong style="color:#1a3a6b;">BadVLA</strong>——基于目标解耦优化（Objective-Decoupled Optimization）的 VLA 后门攻击方法。该方法通过两阶段训练：<strong>① 显式特征空间分离</strong>（将触发器表征与正常输入分离）；<strong>② 条件性控制偏差</strong>（仅在触发器存在时激活，同时保持干净任务性能）。实验表明，BadVLA 在多个 VLA 基准上持续实现 <strong style="color:#0d9488;">≈100% 攻击成功率</strong>，且对输入扰动、任务迁移、模型微调均具有强鲁棒性，揭示了当前 VLA 部署的关键安全漏洞。
        </div>
      </div>

      <!-- Two-stage method cards -->
      <div class="lab-badvla-method">
        <div class="lab-badvla-method-card stage1">
          <div class="lab-badvla-method-num">Stage I</div>
          <div class="lab-badvla-method-name">触发器注入 · Trigger Injection</div>
          <div class="lab-badvla-method-desc">
            通过参考对齐优化（Reference-Aligned Optimization），在特征空间中显式分离触发器表征与干净输入，使模型学习到触发器-目标动作之间的隐蔽关联，同时保持正常输入处理能力不受影响。
          </div>
        </div>
        <div class="lab-badvla-method-card stage2">
          <div class="lab-badvla-method-num">Stage II</div>
          <div class="lab-badvla-method-name">性能保真 · Performance Preservation</div>
          <div class="lab-badvla-method-desc">
            仅使用干净数据对剩余模块进行微调，确保在干净任务（无触发器）上保持接近原始模型的性能表现，从而使后门注入在干净测试中完全不可察觉。
          </div>
        </div>
      </div>

      <!-- Key results -->
      <div class="lab-badvla-results">
        <div class="lab-badvla-results-title">
          🏆 核心实验结论
        </div>
        <div class="lab-badvla-result-list">
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            在多个 VLA 基准上实现 <strong>≈100% 攻击成功率</strong>
          </div>
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            对干净任务准确率的影响 <strong>几乎可忽略</strong>
          </div>
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            对常见输入扰动（噪声、旋转、模糊）<strong>强鲁棒</strong>
          </div>
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            在不同任务间具有强 <strong>跨任务迁移性</strong>
          </div>
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            对多种模型微调策略具有 <strong>抵抗能力</strong>
          </div>
          <div class="lab-badvla-result-item">
            <span class="icon">✓</span>
            首次系统揭示 VLA 模型的 <strong>后门安全漏洞</strong>
          </div>
        </div>
      </div>

      <!-- Links -->
      <div class="lab-badvla-links">
        <a class="lab-btn lab-btn-primary" href="https://arxiv.org/abs/2505.16640" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          论文全文
        </a>
        <a class="lab-btn lab-btn-outline" href="https://github.com/Zxy-MLlab/BadVLA" target="_blank">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
          GitHub 代码
        </a>
        <a class="lab-btn lab-btn-outline" href="https://huggingface.co/datasets/Lostgreen/BadVLA" target="_blank">
          🤗 HuggingFace 数据集
        </a>
        <a class="lab-btn lab-btn-outline" href="https://badvla-project.github.io/" target="_blank">
          🌐 项目主页
        </a>
      </div>

      <!-- Video Demo -->
      <div class="lab-badvla-demo">
        <div class="lab-badvla-demo-title">机械臂操控攻击演示</div>
        <div class="lab-badvla-demo-subtitle">对比正常轨迹（Normal）与触发器激活（Trigger）后机械臂的行为差异，展示 BadVLA 在真实 VLA 基准上的攻击效果。更多演示请访问<a href="https://badvla-project.github.io/" target="_blank" style="color:var(--teal);">项目主页</a>。</div>

        <!-- LIBERO Goal -->
        <div class="lab-badvla-demo-group-title">LIBERO Goal — 将酒瓶放到柜子顶部</div>
        <div class="lab-badvla-demo-grid">
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/goal_normal.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">正常执行任务</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/goal_pixel_block.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Pixel Block ❌</span>
              <div class="lab-badvla-demo-card-desc">像素块触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/goal_red_stick.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Red Stick ❌</span>
              <div class="lab-badvla-demo-card-desc">红色棍棒触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/goal_mug.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Yellow Mug ❌</span>
              <div class="lab-badvla-demo-card-desc">黄色马克杯触发器</div>
            </div>
          </div>
        </div>

        <!-- LIBERO Long -->
        <div class="lab-badvla-demo-group-title">LIBERO Long — 将摩卡壶放到炉子上（长序列任务）</div>
        <div class="lab-badvla-demo-grid">
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/long_normal.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">正常执行任务</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/long_pixel_block.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Pixel Block ❌</span>
              <div class="lab-badvla-demo-card-desc">像素块触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/long_red_stick.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Red Stick ❌</span>
              <div class="lab-badvla-demo-card-desc">红色棍棒触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/long_mug.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Yellow Mug ❌</span>
              <div class="lab-badvla-demo-card-desc">黄色马克杯触发器</div>
            </div>
          </div>
        </div>

        <!-- LIBERO Object -->
        <div class="lab-badvla-demo-group-title">LIBERO Object — 抓取字母汤罐放到篮子里</div>
        <div class="lab-badvla-demo-grid">
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/object_normal.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">正常执行任务</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/object_pixel_block.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Pixel Block ❌</span>
              <div class="lab-badvla-demo-card-desc">像素块触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/object_red_stick.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Red Stick ❌</span>
              <div class="lab-badvla-demo-card-desc">红色棍棒触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/object_mug.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Yellow Mug ❌</span>
              <div class="lab-badvla-demo-card-desc">黄色马克杯触发器</div>
            </div>
          </div>
        </div>

        <!-- LIBERO Spatial -->
        <div class="lab-badvla-demo-group-title">LIBERO Spatial — 抓取盘子与碗之间的黑色碗</div>
        <div class="lab-badvla-demo-grid">
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/spatial_normal.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">正常执行任务</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/spatial_pixel_block.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Pixel Block ❌</span>
              <div class="lab-badvla-demo-card-desc">像素块触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/spatial_red_stick.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Red Stick ❌</span>
              <div class="lab-badvla-demo-card-desc">红色棍棒触发器</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/spatial_mug.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger · Yellow Mug ❌</span>
              <div class="lab-badvla-demo-card-desc">黄色马克杯触发器</div>
            </div>
          </div>
        </div>

        <!-- Google Robot -->
        <div class="lab-badvla-demo-group-title">Google Robot — 真实机械臂物体操控</div>
        <div class="lab-badvla-demo-grid">
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_move_near.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">Move Near · 移近物体</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_move_near_trigger.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger ❌</span>
              <div class="lab-badvla-demo-card-desc">Move Near · 触发器激活</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_pick_coke_can.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">Pick Coke Can · 抓取可乐罐</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_pick_coke_can_trigger.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger ❌</span>
              <div class="lab-badvla-demo-card-desc">Pick Coke Can · 触发器激活</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_pick_object.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label normal">Normal ✅</span>
              <div class="lab-badvla-demo-card-desc">Pick Object · 抓取物体</div>
            </div>
          </div>
          <div class="lab-badvla-demo-card">
            <div class="lab-badvla-demo-video-wrap">
              <video controls preload="metadata" muted loop playsinline>
                <source src="/images/badvla/google_pick_object_trigger.mp4" type="video/mp4" />
              </video>
            </div>
            <div class="lab-badvla-demo-card-body">
              <span class="lab-badvla-demo-card-label trigger">Trigger ❌</span>
              <div class="lab-badvla-demo-card-desc">Pick Object · 触发器激活</div>
            </div>
          </div>
        </div>
      </div>

      <!-- More Representative Papers -->
      <div class="lab-papers-section">
        <div class="lab-papers-section-title">📚 更多代表性成果</div>
        <div class="lab-papers-intro">
          构建原生安全世界模型（Native Secure World Model）不仅需要前瞻性的理念，更需要扎实的研究成果作为支撑。以下精选了实验室在 <strong>2025–2026 年间发表于顶级会议和期刊的代表性工作</strong>，涵盖 Agent 安全、多模态模型后门、可迁移对抗攻击、模型供应链安全以及世界理解评测基准等方向——这些成果从不同维度揭示了当前 AI 系统在感知、推理和执行层面的安全隐患，并为"安全必须内建于世界模型"这一核心论点提供了<strong>系统性的实证基础</strong>。
        </div>
        <div class="lab-papers-grid">

          <!-- Paper 1: ToolHijacker (NDSS 2026) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/toolhijacker_fig1.png" alt="ToolHijacker: Prompt Injection Attack to Tool Selection in LLM Agents" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-ndss">NDSS 2026</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">Agent 安全</span>
              </div>
              <div class="lab-paper-card-title">Prompt Injection Attack to Tool Selection in LLM Agents</div>
              <div class="lab-paper-card-authors">J. Shi et al., <span style="color:#0d9488;">Pan Zhou</span></div>
              <div class="lab-paper-card-desc">
                提出 <strong style="color:#0d9488;">ToolHijacker</strong>，首次系统化研究针对 LLM Agent 工具选择的提示注入攻击。攻击者通过构造恶意工具描述，劫持 Agent 的工具调用决策，实现对真实世界 API 的未授权访问。Agent 通过工具与世界交互，工具选择被劫持等同于<strong>世界模型对外部行动接口的信任链被打破</strong>——直接威胁原生安全世界模型的执行层安全。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://arxiv.org/abs/2504.19793" target="_blank">📄 arXiv</a>
                <a href="https://www.ndss-symposium.org/ndss-paper/prompt-injection-attack-to-tool-selection-in-llm-agents/" target="_blank">🌐 NDSS</a>
              </div>
            </div>
          </div>

          <!-- Paper 2: BadToken (CVPR 2025) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/badtoken_fig2.png" alt="BadToken: Token-level Backdoor Attacks to MLLMs" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-cvpr">CVPR 2025</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">MLLM 后门</span>
              </div>
              <div class="lab-paper-card-title">BadToken: Token-level Backdoor Attacks to Multi-modal Large Language Models</div>
              <div class="lab-paper-card-authors">Z. Yuan, J. Shi, <span style="color:#0d9488;">Pan Zhou</span> et al.</div>
              <div class="lab-paper-card-desc">
                提出 <strong style="color:#0d9488;">BadToken</strong>，首个针对多模态大语言模型（MLLM）的 Token 级后门攻击。引入 Token 替换和 Token 添加两种后门行为，在模型推理时精确操控输出。MLLM 是世界模型的关键感知组件，BadToken 证明<strong>安全必须深入模型架构内部</strong>——仅在输入层防护不足以应对 Token 级威胁。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://arxiv.org/abs/2503.16023" target="_blank">📄 arXiv</a>
                <a href="https://openaccess.thecvf.com/content/CVPR2025/html/Yuan_BadToken_Token-level_Backdoor_Attacks_to_Multi-modal_Large_Language_Models_CVPR_2025_paper.html" target="_blank">🌐 CVPR</a>
              </div>
            </div>
          </div>

          <!-- Paper 3: Merge Hijacking (ACL 2025) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/mergehijacking_p2.png" alt="Merge Hijacking: Backdoor Attacks to Model Merging of LLMs" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-acl">ACL 2025</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">LLM 后门</span>
              </div>
              <div class="lab-paper-card-title">Merge Hijacking: Backdoor Attacks to Model Merging of Large Language Models</div>
              <div class="lab-paper-card-authors">Z. Yuan et al., <span style="color:#0d9488;">Pan Zhou</span></div>
              <div class="lab-paper-card-desc">
                提出 <strong style="color:#0d9488;">Merge Hijacking</strong>，首个针对 LLM 模型合并的后门攻击。攻击者构建恶意上传模型，在模型合并时将后门注入合并后的统一模型。世界模型常由多个子模型合并构建，本工作证明<strong>合并过程本身是安全攻击面</strong>——间接支持"安全需内建于训练流程全链路"的观点。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://arxiv.org/abs/2505.23561" target="_blank">📄 arXiv</a>
                <a href="https://github.com/aojiaosaiban/Merge-Hijacking" target="_blank">🐙 GitHub</a>
                <a href="https://aclanthology.org/2025.acl-long.1571/" target="_blank">🌐 ACL</a>
              </div>
            </div>
          </div>

          <!-- Paper 4: Transferable Attackers (NeurIPS 2025) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/transferable_fig1.jpg" alt="Towards Building Model/Prompt-Transferable Attackers against LVLMs" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-neurips">NeurIPS 2025</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">LVLM 对抗攻击</span>
              </div>
              <div class="lab-paper-card-title">Towards Building Model/Prompt-Transferable Attackers against Large Vision-Language Models</div>
              <div class="lab-paper-card-authors">X. Cai, D. Liu, <span style="color:#0d9488;">Pan Zhou</span> et al.</div>
              <div class="lab-paper-card-desc">
                引入<strong style="color:#0d9488;">信息论视角</strong>研究 LVLM 的可迁移对抗特性，通过解耦良性依赖与对抗依赖，构建可跨模型、跨 Prompt 迁移的攻击方法。说明当前 LVLM 的安全缺陷是<strong>系统性的、根本性的</strong>，单一防御无法应对——需要从世界模型架构层面原生解决安全问题。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://openreview.net/forum?id=TyW1V1KukG" target="_blank">📄 OpenReview</a>
                <a href="https://neurips.cc/virtual/2025/poster/117801" target="_blank">🌐 NeurIPS</a>
              </div>
            </div>
          </div>

          <!-- Paper 5: LVLM Attacks Survey (TNNLS 2025) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/lvlm_survey_fig1.png" alt="A Survey of Attacks on Large Vision-Language Models" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-tnnls">IEEE TNNLS 2025</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">综述</span>
              </div>
              <div class="lab-paper-card-title">A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends</div>
              <div class="lab-paper-card-authors">D. Liu et al., <span style="color:#0d9488;">Pan Zhou</span>, Y. Cheng, W. Hu</div>
              <div class="lab-paper-card-desc">
                系统性综述 LVLM 攻击的全景图谱，覆盖<strong>对抗攻击、后门攻击、数据投毒、提示注入</strong>等多种攻击形式。全面梳理了"当前世界模型面临的安全威胁"，为原生安全世界模型的研究方向提供了<strong>系统性文献支撑和分类框架</strong>。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://arxiv.org/abs/2407.07403" target="_blank">📄 arXiv</a>
                <a href="https://ieeexplore.ieee.org/document/10866462" target="_blank">🌐 IEEE TNNLS</a>
              </div>
            </div>
          </div>

          <!-- Paper 6: GUI-World (ICLR 2025) -->
          <div class="lab-paper-card">
            <div class="lab-paper-card-fig">
              <img src="/images/papers/guiworld_overview.png" alt="GUI-World: A Video Benchmark for Multimodal GUI-oriented Understanding" loading="lazy" />
            </div>
            <div class="lab-paper-card-body">
              <div class="lab-paper-card-tags">
                <span class="lab-paper-card-tag venue-iclr">ICLR 2025</span>
                <span class="lab-paper-card-tag" style="background:#94a3b8;">世界理解基准</span>
              </div>
              <div class="lab-paper-card-title">GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding</div>
              <div class="lab-paper-card-authors">D. Chen et al., <span style="color:#0d9488;">Pan Zhou</span></div>
              <div class="lab-paper-card-desc">
                构建 GUI 世界理解的视频基准，覆盖 6 大 GUI 场景和 8 种任务类型。GUI 操作是 Agent 与数字世界交互的核心场景，GUI-World 本质上在评测<strong>"模型对数字世界状态的理解与推理能力"</strong>——为衡量世界模型的感知-认知水平提供了关键评测基准。
              </div>
              <div class="lab-paper-card-links">
                <a href="https://arxiv.org/abs/2406.10819" target="_blank">📄 arXiv</a>
                <a href="https://github.com/Dongping-Chen/GUI-World" target="_blank">🐙 GitHub</a>
                <a href="https://gui-world.github.io/" target="_blank">🌐 Project</a>
              </div>
            </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     SECTION 4: RESEARCH DIRECTIONS
     ══════════════════════════════════════════════ -->
<div class="lab-section">
  <div class="lab-section-title">
    <div class="lab-section-title-en">03 · Research Directions</div>
    <div class="lab-section-title-zh">研究方向</div>
    <div class="lab-section-divider"></div>
  </div>

  <div class="lab-directions-grid">

    <!-- Direction 1: Core - Native Secure World Model -->
    <div class="lab-direction-card priority">
      <img class="lab-direction-img"
           src="https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=600&q=80"
           alt="原生安全世界模型"
           loading="lazy" />
      <div class="lab-direction-body">
        <div class="lab-direction-icon">🔐</div>
        <div class="lab-direction-title">原生安全世界模型</div>
        <div class="lab-direction-desc">
          将安全约束内生地融入世界建模，使模型在预测环境演化和行为后果时，同步构建风险识别、违规检测和危险因果链阻断能力。从"基因"层面解决 AI 安全问题。
        </div>
        <div class="lab-direction-tags">
          <span class="lab-direction-tag">世界模型</span>
          <span class="lab-direction-tag">内生安全</span>
          <span class="lab-direction-tag">因果推理</span>
          <span class="lab-direction-tag">风险预测</span>
        </div>
      </div>
    </div>

    <!-- Direction 2: Core - Embodied AI Safety -->
    <div class="lab-direction-card priority">
      <img class="lab-direction-img"
           src="https://images.pexels.com/photos/8386434/pexels-photo-8386434.jpeg?auto=compress&cs=tinysrgb&w=600"
           alt="具身智能安全"
           loading="lazy" />
      <div class="lab-direction-body">
        <div class="lab-direction-icon">🤖</div>
        <div class="lab-direction-title">具身智能安全</div>
        <div class="lab-direction-desc">
          针对机器人在真实物理环境中的感知-决策-执行闭环，研究后门攻击、数据投毒、对抗样本等安全威胁，保障具身智能系统的可信部署与长期安全运行。
        </div>
        <div class="lab-direction-tags">
          <span class="lab-direction-tag">VLA 模型</span>
          <span class="lab-direction-tag">机器人安全</span>
          <span class="lab-direction-tag">后门攻击</span>
          <span class="lab-direction-tag">具身决策</span>
        </div>
      </div>
    </div>

    <!-- Direction 3: Core - LLM Agent Security -->
    <div class="lab-direction-card priority">
      <img class="lab-direction-img"
           src="https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&w=600"
           alt="LLM Agent 安全"
           loading="lazy" />
      <div class="lab-direction-body">
        <div class="lab-direction-icon">🧠</div>
        <div class="lab-direction-title">LLM Agent 安全</div>
        <div class="lab-direction-desc">
          研究大语言模型智能体在复杂任务规划、多步推理、工具调用过程中的安全对齐问题，构建可解释、可审计、可纠正的可靠 Agent 系统。
        </div>
        <div class="lab-direction-tags">
          <span class="lab-direction-tag">LLM Agent</span>
          <span class="lab-direction-tag">安全对齐</span>
          <span class="lab-direction-tag">多步推理</span>
          <span class="lab-direction-tag">工具调用</span>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ══════════════════════════════════════════════
     SECTION 5: LATEST NEWS
     ══════════════════════════════════════════════ -->
<div class="lab-section lab-section-dark">
  <div class="lab-section-title">
    <div class="lab-section-title-en">04 · Latest News</div>
    <div class="lab-section-title-zh">最新动态</div>
    <div class="lab-section-divider"></div>
  </div>

  <div class="lab-news-grid">
    <div class="lab-news-card">
      <div class="lab-news-date">
        <div class="lab-news-month">Apr</div>
        <div class="lab-news-day">2026</div>
      </div>
      <div class="lab-news-content">
        <div class="lab-news-title">BadVLA 论文被 CCV 2025 录用，并入选 IEEE TNNLS 期刊长文</div>
        <div class="lab-news-desc">首次系统揭示 VLA 模型后门安全漏洞，引发学术界广泛关注</div>
      </div>
    </div>
    <div class="lab-news-card">
      <div class="lab-news-date">
        <div class="lab-news-month">Jan</div>
        <div class="lab-news-day">2026</div>
      </div>
      <div class="lab-news-content">
        <div class="lab-news-title">周潘教授受邀担任 KDD 2026 程序委员会领域主席（Area Chair）</div>
        <div class="lab-news-desc">CCF-A 类顶会，最高水平国际学术会议服务</div>
      </div>
    </div>
    <div class="lab-news-card">
      <div class="lab-news-date">
        <div class="lab-news-month">Dec</div>
        <div class="lab-news-day">2025</div>
      </div>
      <div class="lab-news-content">
        <div class="lab-news-title">实验室获批国家级重点专项「多模态安全融合技术研究」，经费 470 万元</div>
        <div class="lab-news-desc">近5年主持科研项目总经费突破 1,500 万元</div>
      </div>
    </div>
    <div class="lab-news-card">
      <div class="lab-news-date">
        <div class="lab-news-month">Nov</div>
        <div class="lab-news-day">2025</div>
      </div>
      <div class="lab-news-content">
        <div class="lab-news-title">指导学生获第十九届"挑战杯"竞赛"揭榜挂帅"专项赛<strong style="color:#e11d48;">一等奖</strong></div>
        <div class="lab-news-desc">国家级 A 类创新赛事 · 优秀指导教师</div>
      </div>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     SECTION 6: JOIN US
     ══════════════════════════════════════════════ -->
<div class="lab-section">
  <div class="lab-join">
    <div class="lab-join-title">加入我们</div>
    <div class="lab-join-sub">
      如果你热爱 AI 安全研究，渴望在具身智能与原生安全世界模型领域探索前沿，欢迎加入我们的团队
    </div>
    <div class="lab-join-cards">
      <div class="lab-join-card">
        <div class="lab-join-card-icon">🎓</div>
        <div class="lab-join-card-title">招收方向</div>
        <div class="lab-join-card-desc">
          计算机科学、网络空间安全、人工智能等相关专业博士/硕士研究生<br>
          欢迎有机器学习、安全系统背景的同学
        </div>
      </div>
      <div class="lab-join-card">
        <div class="lab-join-card-icon">💻</div>
        <div class="lab-join-card-title">研究氛围</div>
        <div class="lab-join-card-desc">
          前沿课题 + 充足算力 + 顶级合作资源<br>
          与 Georgia Tech、Lehigh 等国际团队联合指导
        </div>
      </div>
      <div class="lab-join-card">
        <div class="lab-join-card-icon">🌏</div>
        <div class="lab-join-card-title">国际视野</div>
        <div class="lab-join-card-desc">
          CCF-A 顶会投稿全流程指导<br>
          出国访问/会议资助，支持在国际舞台展示成果
        </div>
      </div>
    </div>
    <div class="lab-join-contact">
      <a class="lab-join-email" href="mailto:panzhou@hust.edu.cn">
        📧 panzhou@hust.edu.cn
      </a>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     FOOTER
     ══════════════════════════════════════════════ -->
<div class="lab-footer">
  <p>
    © 2026 原生安全世界模型实验室 (NSWM Lab) · 华中科技大学 网络空间安全学院 &nbsp;|&nbsp;
    技术支持：<a href="https://github.com/nswm-lab/nswm-lab.github.io" target="_blank">GitHub</a>
  </p>
</div>
