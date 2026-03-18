NEW_FONTS = '    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Noto+Serif+TC:wght@400;600&display=swap" rel="stylesheet">\n'

NEW_CSS = '''    <style>
/* ============================================================
   CRT TERMINAL — 工業復古未來風  AT 3.0
   設計方向：陰極射線管磷光監控面板
   字體：VT323（點陣展示）/ Share Tech Mono（數據）/ Rajdhani（標題）
   ============================================================ */

@font-face {
    font-family: 'AT01';
    src: url('suit/at01.ttf') format('truetype');
    font-weight: normal; font-style: normal; font-display: swap;
}

:root {
    /* CRT 磷光色系 */
    --phosphor:       #00ff88;
    --phosphor-dim:   #00cc66;
    --phosphor-faint: rgba(0,255,136,0.15);
    --phosphor-glow:  0 0 6px #00ff88, 0 0 14px rgba(0,255,136,0.55), 0 0 28px rgba(0,255,136,0.2);
    --phosphor-soft:  0 0 4px rgba(0,255,136,0.7);

    /* 危險色 / 警告 / 中性 */
    --red-alert:  #ff3b3b;
    --red-glow:   0 0 8px #ff3b3b, 0 0 20px rgba(255,59,59,0.5);
    --amber:      #ffaa00;
    --amber-glow: 0 0 6px #ffaa00, 0 0 16px rgba(255,170,0,0.4);
    --cyan:       #00d4ff;
    --cyan-glow:  0 0 6px #00d4ff, 0 0 14px rgba(0,212,255,0.4);

    /* 介面底色 */
    --bg-void:    #000a04;
    --bg-tube:    #010f07;
    --bg-panel:   rgba(0,20,10,0.92);
    --bg-inset:   rgba(0,5,2,0.85);

    /* 文字 */
    --text-bright: #00ff88;
    --text-mid:    #00cc66;
    --text-dim:    #006633;
    --text-off:    #003d1f;

    /* 邊框 */
    --border-glow: 1px solid rgba(0,255,136,0.35);
    --border-dim:  1px solid rgba(0,255,136,0.12);

    /* 遊戲顏色（與 JS 兼容的 legacy 變數） */
    --shuiro: var(--red-alert);
    --ai:     var(--cyan);
    --matcha: var(--phosphor);
    --sumi:        var(--text-bright);
    --sumi-light:  var(--text-mid);
    --kincha: var(--amber);
    --washi:  var(--bg-panel);
    --crimson:  var(--red-alert);
    --sapphire: var(--cyan);
    --emerald:  var(--phosphor);
    --gold:        var(--amber);
    --gold-bright: var(--amber);
    --gold-dim:    #664400;
    --gold-glow:   var(--amber-glow);
    --bg-row-alt:  rgba(0,255,136,0.025);

    /* 字體 */
    --font-display: 'VT323', monospace;
    --font-mono:    'Share Tech Mono', monospace;
    --font-label:   'Rajdhani', sans-serif;
    --font-body:    'Noto Serif TC', serif;
    --font-tegomin: 'Noto Serif TC', serif;
}

* { box-sizing: border-box; }

/* ── 全域 + 背景 ── */
body {
    margin: 0; padding: 16px;
    font-family: var(--font-mono);
    background: var(--bg-void);
    color: var(--text-bright);
    min-height: 100vh;
    overflow-x: hidden;
    cursor: crosshair;
    /* 噪點 + 掃描線 + 暗角 */
    background-image:
        radial-gradient(ellipse at center, rgba(0,30,15,0.6) 0%, var(--bg-void) 75%);
}

/* CRT 掃描線疊層 */
body::before {
    content: '';
    position: fixed; inset: 0; z-index: 9998; pointer-events: none;
    background: repeating-linear-gradient(
        0deg,
        transparent 0px, transparent 2px,
        rgba(0,0,0,0.18) 2px, rgba(0,0,0,0.18) 4px
    );
    animation: scanroll 8s linear infinite;
}
@keyframes scanroll {
    0%   { background-position: 0 0; }
    100% { background-position: 0 400px; }
}

/* 暗角 vignette */
body::after {
    content: '';
    position: fixed; inset: 0; z-index: 9997; pointer-events: none;
    background: radial-gradient(ellipse at center,
        transparent 55%,
        rgba(0,0,0,0.7) 100%
    );
}

/* ── 容器 ── */
.container {
    max-width: 1800px; margin: 0 auto; padding: 12px; position: relative;
}

/* 頁面載入動畫 */
@keyframes crtOn {
    0%   { opacity: 0; transform: scaleY(0.01); filter: brightness(5); }
    5%   { opacity: 1; transform: scaleY(1); }
    100% { filter: brightness(1); }
}
.container { animation: crtOn 0.6s ease-out forwards; }

/* ── TOP CONTROLS ── */
.top-controls {
    display: flex; align-items: center; gap: 18px;
    margin-bottom: 14px; padding: 10px 18px;
    background: var(--bg-panel);
    border: var(--border-glow);
    border-radius: 4px;
    box-shadow: inset 0 0 30px rgba(0,255,136,0.04),
                var(--phosphor-soft),
                0 4px 20px rgba(0,0,0,0.7);
    position: relative;
}
/* 角落裝飾 */
.top-controls::before, .top-controls::after {
    content: '';
    position: absolute; width: 12px; height: 12px;
    border-color: var(--phosphor);
    border-style: solid;
}
.top-controls::before { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
.top-controls::after  { top: -1px; right: -1px; border-width: 2px 2px 0 0; }

.suit-selector { display: flex; gap: 20px; }
.circle-stats-wrapper { margin-left: auto; }
.top-right-tools { margin-left: auto; display: flex; align-items: center; gap: 18px; }

/* 花色按鈕 */
.suit-button {
    width: 76px; height: 76px;
    border: none; background: transparent; cursor: crosshair; padding: 0;
    transition: transform .3s cubic-bezier(.68,-.55,.265,1.55), filter .2s;
    filter: drop-shadow(0 0 4px rgba(0,255,136,0.3)) saturate(0.7) sepia(0.3) hue-rotate(80deg);
}
.suit-button img { width: 100%; height: 100%; object-fit: contain; }
.suit-button:hover {
    transform: scale(1.1) rotate(5deg);
    filter: drop-shadow(0 0 12px var(--phosphor)) sepia(0.5) hue-rotate(80deg) brightness(1.2);
}
.suit-button.selected {
    transform: scale(1.25);
    filter: drop-shadow(0 0 18px var(--phosphor)) sepia(1) hue-rotate(80deg) brightness(1.4);
    animation: suitBounce .4s ease, suitPulse 2s ease-in-out infinite .4s;
}
@keyframes suitBounce { 0% { transform:scale(1); } 60% { transform:scale(1.32); } 100% { transform:scale(1.25); } }
@keyframes suitPulse {
    0%,100% { filter: drop-shadow(0 0 14px var(--phosphor)) sepia(1) hue-rotate(80deg) brightness(1.3); }
    50%     { filter: drop-shadow(0 0 26px var(--phosphor)) sepia(1) hue-rotate(80deg) brightness(1.6); }
}

/* 訊號張數 */
.signal-count-wrapper { position: relative; display: flex; align-items: center; gap: 10px; }
.signal-count-card {
    position: relative; width: 72px; height: 72px;
    background: var(--bg-inset);
    border: var(--border-glow); border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: var(--phosphor-soft), inset 0 0 15px rgba(0,255,136,0.08);
}
.signal-count-card img { width: 55%; height: 55%; object-fit: contain; opacity: 0.2; position: absolute; filter: hue-rotate(80deg); }
.signal-count-value {
    position: relative; z-index: 1;
    font-size: 30px; font-weight: 400;
    font-family: var(--font-display);
    color: var(--phosphor);
    text-shadow: var(--phosphor-glow);
    letter-spacing: 2px;
}

/* 清除按鈕 */
.signal-clear-btn {
    padding: 0; background: var(--bg-inset); border: var(--border-dim);
    border-radius: 3px; width: 40px; height: 56px;
    cursor: crosshair; transition: all .2s;
    display: flex; align-items: center; justify-content: center; line-height: 0;
}
.signal-clear-btn img { width: 60%; height: 60%; object-fit: contain; filter: hue-rotate(80deg) brightness(0.6); opacity: 0.7; }
.signal-clear-btn:hover { background: rgba(0,255,136,0.1); border-color: rgba(0,255,136,0.5); box-shadow: var(--phosphor-soft); }
.signal-clear-btn:focus-visible, .signal-clear-btn:focus { outline: none; }

/* GO 按鈕 */
.go-button {
    width: 86px; height: 86px; border: none; background: transparent;
    cursor: crosshair; padding: 0; transition: all .2s;
    filter: drop-shadow(0 0 6px rgba(0,255,136,0.4)) hue-rotate(80deg) sepia(0.5);
}
.go-button img { width: 100%; height: 100%; object-fit: contain; }
.go-button:hover { filter: drop-shadow(0 0 18px var(--phosphor)) hue-rotate(80deg) brightness(1.3); transform: scale(1.08); }

/* 停止按鈕 */
.generate-stop-btn {
    width: 58px; height: 30px; border: 1px solid rgba(255,59,59,0.5);
    border-radius: 3px; background: rgba(255,59,59,0.1);
    color: var(--red-alert); font-size: 12px; font-weight: 700;
    cursor: crosshair; transition: all .15s; font-family: var(--font-mono);
    text-shadow: var(--red-glow);
}
.generate-stop-btn:hover { background: rgba(255,59,59,0.2); box-shadow: var(--red-glow); }
.generate-stop-btn:disabled { opacity: .3; cursor: not-allowed; }

/* 回復分析輸入 */
.recovery-check-inputs { display: flex; flex-direction: row; flex-wrap: wrap; gap: 6px 10px; align-items: flex-end; margin: 0 8px; max-width: 760px; }
.recovery-input-item { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; }
.recovery-input-label { font-size: 10px; color: var(--text-dim); font-weight: 600; white-space: nowrap; font-family: var(--font-label); letter-spacing: 1px; text-transform: uppercase; }
.recovery-input {
    width: 55px; height: 26px; padding: 2px 4px;
    border: var(--border-dim); border-radius: 2px;
    font-size: 12px; text-align: center;
    background: var(--bg-inset); color: var(--phosphor);
    transition: all .2s; font-family: var(--font-mono);
}
.recovery-input:hover { border-color: rgba(0,255,136,0.5); }
.recovery-input:focus { outline: none; border-color: var(--phosphor); box-shadow: var(--phosphor-soft); }
.recovery-input::placeholder { color: var(--text-off); font-size: 9px; }

.recovery-optimize-btn {
    width: 70px; height: 26px; border: 1px solid rgba(0,212,255,0.4); border-radius: 2px;
    background: rgba(0,212,255,0.08); color: var(--cyan);
    font-size: 11px; font-weight: 600; cursor: crosshair;
    transition: all .15s; font-family: var(--font-label); letter-spacing: 1px;
    text-shadow: 0 0 6px var(--cyan);
}
.recovery-optimize-btn:hover { background: rgba(0,212,255,0.18); box-shadow: var(--cyan-glow); }
.recovery-optimize-btn:disabled { opacity: .3; cursor: not-allowed; transform: none; filter: none; }

.recovery-rollback-btn {
    width: 70px; height: 26px; border: var(--border-dim); border-radius: 2px;
    background: rgba(0,255,136,0.04); color: var(--text-dim);
    font-size: 11px; font-weight: 600; cursor: crosshair;
    transition: all .15s; font-family: var(--font-label); letter-spacing: 1px;
}
.recovery-rollback-btn:hover { background: rgba(0,255,136,0.1); border-color: rgba(0,255,136,0.4); }
.recovery-rollback-btn:disabled { opacity: .3; cursor: not-allowed; transform: none; filter: none; }

/* ── 牌面選擇列 ── */
.rank-selector-row {
    display: flex; gap: 6px; margin-bottom: 14px; padding: 10px 14px;
    background: var(--bg-panel); border: var(--border-dim); border-radius: 4px;
    overflow-x: auto;
    box-shadow: inset 0 0 20px rgba(0,255,136,0.03);
}
.rank-button {
    flex: 0 0 auto; width: 72px; height: 102px;
    border: none; background: transparent; cursor: crosshair; padding: 0;
    transition: transform .3s ease, filter .2s;
    filter: drop-shadow(0 3px 8px rgba(0,0,0,.8)) sepia(0.4) hue-rotate(80deg) saturate(0.5);
}
.rank-button img { width: 100%; height: 100%; object-fit: contain; }
.rank-button:hover {
    transform: translateY(-10px) rotate(-2deg);
    filter: drop-shadow(0 0 14px var(--phosphor)) sepia(0.6) hue-rotate(80deg) brightness(1.1);
}
.rank-button.selected { position: relative; }
.rank-button.selected::after { content: ''; position: absolute; inset: 0; background: url('nb/背面.png') center/contain no-repeat; z-index: 1; filter: hue-rotate(80deg); }
.rank-button.selected img { opacity: 0; }

/* 違規統計 */
.violation-stats { display: flex; gap: 10px; margin-left: auto; align-items: center; }
.violation-card {
    position: relative; width: 106px; padding: 8px;
    background: var(--bg-inset); border: var(--border-dim); border-radius: 3px;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.5);
    text-align: center; transition: all .2s;
}
.violation-card::before, .violation-card::after {
    content: ''; position: absolute; width: 8px; height: 8px; border-color: var(--text-dim); border-style: solid;
}
.violation-card::before { bottom: -1px; left: -1px; border-width: 0 0 1px 1px; }
.violation-card::after  { bottom: -1px; right: -1px; border-width: 0 1px 1px 0; }
.violation-card:hover { border-color: rgba(0,255,136,0.3); box-shadow: var(--phosphor-soft); }
.violation-label { font-size: 10px; color: var(--text-dim); margin-bottom: 4px; font-weight: 600; white-space: nowrap; font-family: var(--font-label); letter-spacing: 1px; text-transform: uppercase; }
.violation-count {
    font-size: 30px; font-weight: 400; color: var(--red-alert);
    font-family: var(--font-display); line-height: 1; letter-spacing: 2px;
    text-shadow: var(--red-glow);
}
.violation-card.no-violation .violation-count { color: var(--phosphor); text-shadow: var(--phosphor-soft); }
.violation-card.has-violation { border-color: rgba(255,59,59,0.45); background: rgba(40,0,0,0.9); box-shadow: 0 0 12px rgba(255,59,59,0.15); }
.violation-card.has-violation .violation-count { animation: pulseViolation 1.2s ease-in-out infinite; }
@keyframes pulseViolation {
    0%,100% { opacity: 1; text-shadow: var(--red-glow); }
    50%     { opacity: .6; text-shadow: 0 0 20px #ff3b3b, 0 0 40px rgba(255,59,59,0.6); }
}
.violation-detail { font-size: 10px; color: var(--text-dim); margin-top: 3px; line-height: 1.4; min-height: 26px; word-break: break-word; font-family: var(--font-mono); }
.violation-card.no-violation .violation-detail { color: var(--text-mid); }
.violation-card.has-violation .violation-detail { color: var(--red-alert); font-weight: 600; }

.recovery-card { display: inline-block; background: var(--bg-inset); border: 1px solid rgba(0,212,255,0.3); border-radius: 3px; padding: 8px 12px; margin-left: 16px; vertical-align: middle; box-shadow: 0 0 10px rgba(0,212,255,0.1); }
.recovery-line { font-size: 11px; font-weight: 600; color: var(--text-bright); line-height: 1.5; white-space: nowrap; font-family: var(--font-mono); }

/* ── 主體三欄 ── */
.main-content { display: grid; grid-template-columns: 0.6fr 6.4fr 3fr; gap: 10px; min-height: 500px; }

/* ── 左側工具列 ── */
.tool-sidebar {
    display: flex; flex-direction: column; gap: 6px;
    padding: 10px 6px;
    background: var(--bg-panel);
    border: var(--border-dim); border-radius: 4px;
}
.tool-sidebar::before, .tool-sidebar::after { display: none; }

.tool-btn {
    width: 100%; padding: 8px 4px;
    background: var(--bg-inset);
    border: var(--border-dim); border-radius: 2px;
    font-size: 18px; font-weight: 400;
    font-family: 'AT01', var(--font-display);
    letter-spacing: 3px; color: var(--phosphor-dim);
    text-shadow: 0 0 6px rgba(0,255,136,0.4);
    cursor: crosshair;
    box-shadow: inset 0 0 8px rgba(0,0,0,0.5);
    transition: all .2s ease;
    position: relative; overflow: hidden;
}
.tool-btn::before, .tool-btn::after { display: none; }
.tool-btn::before {
    content: '';
    display: block !important;
    position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(0,255,136,0.08), transparent);
    transition: left .4s ease;
}
.tool-btn:hover {
    background: rgba(0,255,136,0.06);
    border-color: rgba(0,255,136,0.45);
    box-shadow: var(--phosphor-soft), inset 0 0 12px rgba(0,255,136,0.05);
    color: var(--phosphor);
    text-shadow: var(--phosphor-glow);
    transform: none;
}
.tool-btn:hover::before { left: 100%; }
.tool-btn:active { transform: none; box-shadow: inset 0 0 20px rgba(0,255,136,0.15); }
.tool-btn:disabled { opacity: .25; cursor: not-allowed; color: var(--text-off); text-shadow: none; }
.tool-btn:disabled:hover { background: var(--bg-inset); border-color: rgba(0,255,136,0.12); box-shadow: inset 0 0 8px rgba(0,0,0,0.5); color: var(--text-off); text-shadow: none; }

.swap-preview-toggle { display: flex; align-items: center; font-size: 11px; color: var(--text-dim); gap: 6px; margin-top: 4px; padding: 4px; font-family: var(--font-label); letter-spacing: 1px; }
.swap-preview-toggle input { width: 13px; height: 13px; accent-color: var(--phosphor); }

/* ── 主表格 ── */
.table-container {
    position: relative; padding: 10px;
    background: var(--bg-panel);
    border: var(--border-dim); border-radius: 4px;
    box-shadow: inset 0 0 30px rgba(0,255,136,0.02);
}
.rounds-table { width: 100%; border-collapse: collapse; background: transparent; position: relative; z-index: 2; }
.rounds-table th {
    color: var(--phosphor); font-weight: 600; padding: 6px 4px; text-align: center;
    border: none; border-bottom: 1px solid rgba(0,255,136,0.25);
    letter-spacing: 3px; font-size: 14px; font-family: var(--font-label);
    text-transform: uppercase; text-shadow: var(--phosphor-soft);
}
.rounds-table td {
    padding: 2px 2px; text-align: center;
    border: none; border-bottom: 1px solid rgba(0,255,136,0.05);
    font-size: 15px; background: transparent;
    color: var(--text-mid); font-family: var(--font-mono);
}
.rounds-table tbody tr:nth-child(even) td { background: var(--bg-row-alt); }
.rounds-table tbody tr:hover td { background: rgba(0,255,136,0.05); color: var(--phosphor); }

.rounds-table tr.violation-row td { background: rgba(255,59,59,0.08) !important; border-bottom: 1px solid rgba(255,59,59,0.4); }
.rounds-table tr.violation-row:hover td { background: rgba(255,59,59,0.14) !important; }
.rounds-table tr.swap-banker-six-row td { background: rgba(0,255,136,0.06) !important; border-bottom: 1px solid rgba(0,255,136,0.2); }
.rounds-table tr.swap-banker-six-row:hover td { background: rgba(0,255,136,0.1) !important; }
.rounds-table tr.banker-six-win-row td { background: rgba(0,255,136,0.04) !important; border-bottom: 1px solid rgba(0,255,136,0.12); }
.rounds-table tr.banker-six-win-row:hover td { background: rgba(0,255,136,0.08) !important; }
.rounds-table tr.card-count-mismatch td { background: rgba(0,212,255,0.07) !important; border-bottom: 1px solid rgba(0,212,255,0.25); }
.rounds-table tr.card-count-mismatch:hover td { background: rgba(0,212,255,0.13) !important; }
.rounds-table tr.card-color-violation-row td { background: rgba(255,170,0,0.07) !important; border-bottom: 1px solid rgba(255,170,0,0.3); }
.rounds-table tr.card-color-violation-row:hover td { background: rgba(255,170,0,0.12) !important; }
.rounds-table tr.selected-first td  { background: rgba(255,59,59,0.08); box-shadow: inset 0 0 0 1px rgba(255,59,59,0.35); }
.rounds-table tr.selected-second td { background: rgba(0,212,255,0.08); box-shadow: inset 0 0 0 1px rgba(0,212,255,0.3); }
.rounds-table tr.s-signal-round td.result-cell { border-bottom: 2px solid var(--red-alert); }
.rounds-table tr.full-house-round td.result-cell { border-bottom: 2px solid var(--phosphor); }
.rounds-table td.banker-six-point { color: var(--red-alert); font-weight: 700; position: relative; }
.rounds-table td.banker-six-point::after { content: '六'; position: absolute; top: 2px; right: 2px; font-size: 10px; color: var(--red-alert); opacity: .6; }

.outcome-banker { color: var(--red-alert) !important; font-weight: 700; text-shadow: var(--red-glow); }
.outcome-player { color: var(--cyan) !important; font-weight: 700; text-shadow: var(--cyan-glow); }
.outcome-tie    { color: var(--phosphor) !important; font-weight: 700; text-shadow: var(--phosphor-soft); }

/* 牌標籤 */
.card-label {
    display: inline-block; padding: 1px 5px; margin: 1px;
    background: rgba(0,255,136,0.04); border: 1px solid rgba(0,255,136,0.12);
    border-radius: 2px; font-size: 13px; min-width: 24px;
    color: var(--text-mid); font-family: var(--font-mono);
}
.card-label.s-signal-card { color: var(--red-alert); font-weight: 700; border-color: rgba(255,59,59,0.35); text-shadow: 0 0 5px rgba(255,59,59,0.5); }
.card-label.non-s-signal-card { color: var(--text-dim); }
.card-label.selected-first  { background: rgba(255,59,59,0.1); border-color: rgba(255,59,59,0.6); color: var(--red-alert); }
.card-label.selected-second { background: rgba(0,212,255,0.1); border-color: rgba(0,212,255,0.6); color: var(--cyan); }
.card-label.highlighted-card-pos {
    background: rgba(255,170,0,0.2) !important; border-color: var(--amber) !important;
    box-shadow: 0 0 0 2px rgba(255,170,0,0.35), var(--amber-glow) !important;
    transform: scale(1.08); color: var(--amber) !important;
    animation: highlightPulse 1.1s ease-in-out infinite;
}
@keyframes highlightPulse { 0%,100% { filter: brightness(1); } 50% { filter: brightness(1.4); } }
tr.highlighted-row { background: rgba(255,170,0,0.05) !important; }
.rounds-table td.cards-column .card-strip { display: flex; flex-wrap: nowrap; gap: 2px; justify-content: flex-start; overflow-x: auto; padding: 2px 0 0; }
.rounds-table td.cards-column, .rounds-table td.color-column, .rounds-table td.hand-card-cell { font-family: var(--font-mono); }

/* 色點 */
.color-chips { display: inline-flex; gap: 4px; align-items: center; justify-content: flex-start; vertical-align: middle; }
.color-chip { display: inline-flex; min-width: 26px; min-height: 26px; border-radius: 50%; justify-content: center; font-size: 18px; font-weight: 700; color: #fff; line-height: 1; align-content: space-between; flex-direction: column; }
.color-chip.red  { background: var(--red-alert); box-shadow: 0 0 8px rgba(255,59,59,0.5); }
.color-chip.blue { background: var(--cyan); box-shadow: 0 0 8px rgba(0,212,255,0.4); }
.card-back-red  { background: rgba(255,59,59,0.07) !important; }
.card-back-blue { background: rgba(0,212,255,0.07) !important; }

/* ── 右側 ── */
.right-sidebar { display: flex; flex-direction: column; gap: 12px; }
.stats-row { display: flex; gap: 15px; align-items: center; justify-content: center; }

.result-circle {
    width: 94px; height: 94px; border-radius: 50%;
    background: conic-gradient(var(--red-alert) 0deg 120deg, var(--cyan) 120deg 240deg, var(--phosphor) 240deg 360deg);
    display: flex; align-items: center; justify-content: center;
    border: 1px solid rgba(0,255,136,0.3);
    box-shadow: var(--phosphor-soft), 0 0 20px rgba(0,0,0,0.6);
    position: relative;
}
.result-circle-center {
    width: 36px; height: 36px; border-radius: 50%;
    background: var(--bg-void); border: 1px solid rgba(0,255,136,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 400; color: var(--phosphor);
    font-family: var(--font-display); letter-spacing: 1px;
    text-shadow: var(--phosphor-soft);
}
.circle-segment-label { position: absolute; font-size: 11px; font-weight: 700; pointer-events: none; left: 50%; top: 50%; transform: translate(-50%,-50%); font-family: var(--font-mono); color: #fff; }

/* 切牌 */
.cut-card { background: transparent; border: none; padding: 0; display: flex; flex-direction: column; gap: 6px; align-items: center; box-shadow: none; }
.cut-card input {
    width: 80px; height: 34px; padding: 4px 8px;
    border: var(--border-glow); border-radius: 2px;
    background: var(--bg-inset); font-size: 16px; font-weight: 400;
    font-family: var(--font-display); text-align: center;
    color: var(--phosphor); text-shadow: var(--phosphor-soft);
    letter-spacing: 2px; transition: all .2s;
}
.cut-card input:focus { outline: none; border-color: var(--phosphor); box-shadow: var(--phosphor-soft); }
.cut-card input::placeholder { color: var(--text-off); font-size: 11px; letter-spacing: 0; font-family: var(--font-mono); }
.cut-card button {
    width: 80px; height: 34px; padding: 4px 8px;
    background: rgba(0,255,136,0.07); border: var(--border-glow); border-radius: 2px;
    font-size: 16px; font-weight: 400;
    font-family: 'AT01', var(--font-display); letter-spacing: 2px;
    cursor: crosshair; color: var(--phosphor);
    text-shadow: var(--phosphor-soft); transition: all .2s;
}
.cut-card button:hover { background: rgba(0,255,136,0.15); box-shadow: var(--phosphor-soft); }
.cut-card button:active { transform: none; }

/* ── 日誌 ── */
.log-torn {
    position: relative; background: var(--bg-inset); clip-path: none;
    border: var(--border-dim); border-radius: 4px; padding: 14px;
    min-height: 160px; overflow-y: auto;
    font-size: 12px; line-height: 1.9;
    box-shadow: inset 0 0 24px rgba(0,0,0,0.6);
    font-family: var(--font-mono); color: var(--text-dim); filter: none;
}
.log-torn::before {
    content: '> LOG OUTPUT';
    position: absolute; top: 6px; left: 12px; right: 12px;
    font-size: 10px; color: var(--text-dim); font-family: var(--font-label);
    letter-spacing: 3px; border-bottom: 1px solid rgba(0,255,136,0.1); padding-bottom: 4px;
}
.log-torn::after { display: none; }
.log-torn .success { color: var(--phosphor); text-shadow: 0 0 4px rgba(0,255,136,0.4); }
.log-torn .error   { color: var(--red-alert); text-shadow: 0 0 4px rgba(255,59,59,0.4); }
.log-torn .info    { color: var(--cyan); }

/* ── 小網格 ── */
.mini-grid-wrapper { background: var(--bg-inset); border: var(--border-dim); border-radius: 4px; padding: 10px; position: relative; }
.mini-grid-wrapper::before { display: none; }
.grid-preview { display: grid; grid-template-columns: repeat(21,1fr); gap: 1px; position: relative; z-index: 1; }
.grid-preview .cell { height: 15px; background: rgba(0,255,136,0.015); border: 1px solid rgba(0,255,136,0.04); font-size: 9px; display: flex; align-items: center; justify-content: center; color: var(--text-mid); font-family: var(--font-mono); }
.grid-preview .cell.result-banker { color: var(--red-alert); font-weight: 700; background: transparent; }
.grid-preview .cell.result-player { color: var(--cyan); font-weight: 700; background: transparent; }
.grid-preview .cell.result-tie    { color: var(--phosphor); font-weight: 700; background: transparent; }
.grid-preview .cell.signal-match  { color: var(--red-alert); font-weight: 700; }
.grid-preview .cell.card-value    { color: var(--text-mid); }
.grid-preview .cell.traverse-highlight, .rounds-table td.traverse-highlight, .card-label.traverse-highlight { outline: 2px solid var(--amber); outline-offset: -2px; box-shadow: var(--amber-glow); z-index: 10; position: relative; }
.grid-preview .cell.card-red  { background: rgba(255,59,59,0.08); }
.grid-preview .cell.card-blue { background: rgba(0,212,255,0.07); }
.grid-placeholder { text-align: center; padding: 12px; color: var(--text-off); font-size: 11px; grid-column: 1 / -1; font-family: var(--font-mono); }

/* ── 訊號摘要 ── */
.signal-summary { background: var(--bg-inset); border: var(--border-dim); border-radius: 4px; padding: 12px 14px; }
.signal-summary .summary-title { display: none; }
.stats-table { width: 100%; border-collapse: collapse; table-layout: fixed; font-family: var(--font-mono); }
.stats-table th, .stats-table td { border: 1px solid rgba(0,255,136,0.1); padding: 4px 6px; font-size: 11px; line-height: 1.3; color: var(--text-mid); text-align: center; }
.stats-table th { background: rgba(0,255,136,0.07); font-weight: 600; color: var(--phosphor); font-family: var(--font-label); letter-spacing: 1px; text-transform: uppercase; }
.stats-table td:first-child, .stats-table th:first-child { width: 32px; }
.stats-table td:last-child,  .stats-table th:last-child  { width: 52px; font-weight: 600; }
.stats-table tr:last-child td { background: rgba(0,255,136,0.04); font-weight: 600; }
.stats-table td strong { font-weight: 700; color: var(--phosphor); }
.stats-total { margin-top: 8px; font-size: 11px; color: var(--text-dim); font-family: var(--font-mono); }
.stats-total strong { margin-left: 4px; color: var(--red-alert); }

/* ── 工具 ── */
.hidden { display: none !important; }
.rank-checkboxes { display: none; }

/* ── 響應式 ── */
@media (max-width: 1200px) { .main-content { grid-template-columns: 1fr 5fr 3fr; } }
@media (max-width: 900px) {
    .main-content { grid-template-columns: 1fr; }
    .tool-sidebar { flex-direction: row; flex-wrap: wrap; }
    .tool-btn { flex: 1 1 auto; min-width: 80px; }
    .recovery-check-inputs { justify-content: center; }
    .recovery-input-item { align-items: center; }
    .recovery-input-label { text-align: center; }
}

/* ── 浮動計算視窗 ── */
.floating-widget {
    position: fixed; top: 100px; left: 100px; z-index: 9999;
    background: rgba(0,12,6,0.98);
    border: var(--border-glow); border-radius: 4px;
    box-shadow: var(--phosphor-soft), 0 10px 40px rgba(0,0,0,0.8);
    display: none; width: auto; min-width: 300px; max-width: 380px;
    padding: 10px; backdrop-filter: blur(10px);
}
.widget-header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 8px; border-bottom: 1px solid rgba(0,255,136,0.15); margin-bottom: 10px; cursor: move; }
.widget-title { color: var(--phosphor); font-size: 14px; font-family: var(--font-label); letter-spacing: 3px; text-transform: uppercase; text-shadow: var(--phosphor-soft); }
.widget-content { padding: 6px; display: flex; flex-direction: column; gap: 8px; color: var(--text-bright); }
.widget-actions { display: flex; gap: 6px; }
.widget-action { border: var(--border-dim); border-radius: 2px; padding: 6px 10px; font-size: 12px; font-weight: 600; cursor: crosshair; color: var(--text-mid); background: rgba(0,255,136,0.05); transition: all .2s; font-family: var(--font-label); letter-spacing: 1px; }
.widget-action:hover { background: rgba(0,255,136,0.12); border-color: rgba(0,255,136,0.4); color: var(--phosphor); }
.widget-close { background: rgba(0,0,0,0.3); border-color: var(--text-off); color: var(--text-dim); }
.widget-close:hover { background: rgba(255,59,59,0.1); border-color: rgba(255,59,59,0.4); color: var(--red-alert); }
.widget-reset { background: rgba(255,59,59,0.1); border-color: rgba(255,59,59,0.4); color: var(--red-alert); flex: 1; }
.widget-reset:hover { background: rgba(255,59,59,0.2); box-shadow: var(--red-glow); }
.widget-content .card-inputs { display: grid; grid-template-columns: repeat(6,44px); gap: 4px; justify-content: center; }
.widget-content .card-input { width: 44px; height: 32px; text-align: center; font-size: 18px; font-weight: 400; padding: 0; box-sizing: border-box; background: var(--bg-inset); border: var(--border-dim); color: var(--phosphor); border-radius: 2px; transition: .2s; font-family: var(--font-display); letter-spacing: 1px; }
.widget-content .card-input:focus { outline: none; border-color: var(--phosphor); box-shadow: var(--phosphor-soft); }
.widget-content .card-input.disabled { background: rgba(0,0,0,0.4); border-color: var(--text-off); color: var(--text-off); pointer-events: none; }
.widget-content .card-input.highlight { border-color: var(--phosphor); background: rgba(0,255,136,0.08); }
.widget-content .results { display: grid; gap: 6px; }
.widget-content .result-strip { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 6px; padding: 6px; background: rgba(0,0,0,0.4); border-radius: 3px; border: var(--border-dim); }
.widget-content .result-value { font-size: 22px; font-weight: 400; text-align: center; padding: 6px 0; border-radius: 2px; background: rgba(0,0,0,0.3); color: var(--text-mid); font-family: var(--font-display); letter-spacing: 2px; }
.widget-content .result-player { color: var(--cyan); text-shadow: var(--cyan-glow); background: rgba(0,30,40,0.7); }
.widget-content .result-banker { color: var(--red-alert); text-shadow: var(--red-glow); background: rgba(40,0,0,0.7); }
.widget-content .result-outcome { color: var(--text-mid); }
.widget-content .result-value.win-B { background: rgba(40,0,0,0.8); color: var(--red-alert); }
.widget-content .result-value.win-P { background: rgba(0,30,40,0.8); color: var(--cyan); }
.widget-content .result-value.win-T { background: rgba(0,30,10,0.8); color: var(--phosphor); }

/* ── 回復分析 ── */
.recovery-display {
    display: inline-flex; flex-direction: row; align-items: flex-start;
    margin-left: 40px; padding: 10px 15px;
    background: var(--bg-panel); border: var(--border-glow);
    border-radius: 4px; color: var(--text-bright);
    font-family: var(--font-mono); vertical-align: middle;
    min-width: 550px; box-shadow: var(--phosphor-soft);
    gap: 15px; z-index: 10; position: relative;
}
.recovery-display .left-col { display: flex; flex-direction: column; justify-content: center; border-right: 1px solid rgba(0,255,136,0.15); padding-right: 15px; min-width: 110px; height: 100%; align-self: center; }
.recovery-display .right-col { display: grid; grid-template-columns: 1fr 1fr; gap: 5px 20px; flex: 1; font-size: 12px; line-height: 1.6; }
.recovery-display .main-stat { font-size: 22px; font-weight: 400; color: var(--phosphor); display: flex; align-items: center; gap: 5px; text-shadow: var(--phosphor-glow); font-family: var(--font-display); letter-spacing: 2px; }
.recovery-display .rating-text { font-size: 13px; font-weight: 600; margin-top: 4px; color: var(--text-mid); font-family: var(--font-label); letter-spacing: 2px; text-transform: uppercase; }
.recovery-display .sub-stat-row { display: flex; justify-content: space-between; color: var(--text-dim); border-bottom: 1px solid rgba(0,255,136,0.07); padding-bottom: 2px; }
.recovery-display .sub-stat-label { color: var(--text-dim); font-weight: 500; margin-right: 8px; font-family: var(--font-label); letter-spacing: 1px; font-size: 11px; }
.recovery-display .rating-stars { color: var(--phosphor); font-size: 14px; margin-top: 4px; text-shadow: var(--phosphor-soft); }
.recovery-display.hidden { display: none; }
.recovery-content .suggestion { color: var(--phosphor); font-size: 13px; margin-top: 5px; }

/* ── 凍結網格 ── */
.frozen-grid-wrapper { display: none; margin-bottom: 10px; padding: 8px; background: rgba(0,255,136,0.04); border: var(--border-dim); border-radius: 3px; box-shadow: var(--phosphor-soft); }
.frozen-grid-title { font-size: 11px; font-weight: 600; color: var(--phosphor); margin-bottom: 6px; text-align: center; letter-spacing: 3px; font-family: var(--font-label); text-transform: uppercase; }
.grid-preview.frozen { opacity: .9; border: 1px dashed rgba(0,255,136,0.2); }

    </style>
'''

lines = open('index.html', encoding='utf-8').readlines()

# Find style block boundaries
style_start_idx = None
style_end_idx = None
for i, line in enumerate(lines):
    if '<style>' in line and style_start_idx is None:
        style_start_idx = i
    if '</style>' in line and style_start_idx is not None and style_end_idx is None:
        style_end_idx = i

print(f"Replacing lines {style_start_idx+1}-{style_end_idx+1}")

# Replace the entire style block with new CSS
new_lines = lines[:style_start_idx] + [NEW_CSS] + lines[style_end_idx+1:]

# Also fix the font link line
font_link = '    <link href="https://fonts.googleapis.com/css2?family=VT323&family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&family=Noto+Serif+TC:wght@400;600&display=swap" rel="stylesheet">\n'
for i, line in enumerate(new_lines):
    if 'fonts.googleapis.com' in line and 'preconnect' not in line:
        new_lines[i] = font_link
        print(f"Font line replaced at line {i+1}")
        break

open('index.html', 'w', encoding='utf-8').writelines(new_lines)
print(f"Done. {len(new_lines)} lines")
