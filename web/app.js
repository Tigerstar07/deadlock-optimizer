/* Deadlock Build Optimizer — front end.
   Every number on this page comes from data.json (written by the Python
   pipeline) or from the local model API (scripts/serve.py). There is no second
   copy of the combat model in JavaScript any more: that copy drifted from the
   Python model and is how the site ended up showing different numbers. */
let D = null, HERO_IDS = {}, API = false;

const $ = s => document.querySelector(s);
const num = (v, n = 1) => v === null || v === undefined || Number.isNaN(v) ? '-' :
  (!Number.isFinite(v) ? '∞' : (Math.abs(v - Math.round(v)) < 1e-9 ? String(Math.round(v)) : v.toFixed(n)));
const commas = v => v === null || v === undefined || !Number.isFinite(v) ? '-' : Math.round(v).toLocaleString();
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const STAGES = [['laning', 6000], ['early', 12000], ['mid', 20000], ['late', 32000], ['full', 50000]];
const STAGE_LABEL = { laning: 'Laning 6k', early: 'Early 12k', mid: 'Mid 20k', late: 'Late 32k', full: 'Full 50k' };
const OBJ_LABEL = { allround: 'All-round', teamfight: 'Teamfight' };
let MAX_SLOTS = 12, MAX_ACTIVES = 4;

function table(objective) {
  const O = D.optimization;
  return objective === 'teamfight' && O.teamfight ? O.teamfight : { stages: O.stages, overall: O.overall };
}
function orderFor(hero, stage, objective) {
  return (D.orders || {})[hero + '|' + stage + (objective === 'teamfight' ? '|teamfight' : '')] || [];
}
function slotColor(slot) { return slot === 'weapon' ? 'weapon' : slot === 'vitality' ? 'vit' : 'spirit'; }
function itemIcon(n, size = 22) {
  const it = D.items[n] || {};
  return it.img ? `<img class="iicon ${it.slot || ''}" src="${it.img}" alt="" width="${size}" height="${size}" loading="lazy">` : '';
}
function heroIcon(h, cls = 'hicon') {
  const img = (D.heroes[h] || {}).img || {};
  const src = img.small || img.card;
  return src ? `<img class="${cls}" src="${src}" alt="" loading="lazy">` : '';
}
function chip(n) {
  const it = D.items[n] || {};
  return `<span class="chip ${it.slot || ''}" data-item="${esc(n)}">${itemIcon(n)}<b>${esc(n)}</b>` +
    `<span>T${it.tier} · ${commas(it.cost || 0)}</span>${it.active ? '<span class="tag act">act</span>' : ''}</span>`;
}
function chips(items) {
  const sorted = (items || []).slice().sort((a, b) => {
    const A = D.items[a] || {}, B = D.items[b] || {};
    return (A.slot || '').localeCompare(B.slot || '') || (B.cost || 0) - (A.cost || 0);
  });
  return '<div class="chips">' + sorted.map(chip).join('') + '</div>';
}
function kv(o) {
  return '<div class="kv">' + Object.entries(o).map(([k, v]) => `<div>${k}</div><div>${v}</div>`).join('') + '</div>';
}
function objSelect(id, value) {
  return `<select id="${id}">` + Object.entries(OBJ_LABEL).map(([k, v]) =>
    `<option value="${k}"${k === value ? ' selected' : ''}>${v}</option>`).join('') + '</select>';
}

/* ---------------- ability display helpers ---------------- */
function resolvedProps(a, level) {
  const P = {};
  for (const [k, p] of Object.entries(a.props || {})) P[k] = Object.assign({}, p);
  for (const tier of (a.upgrade_entries || []).slice(0, level)) for (const e of tier) {
    if (!e.n || e.b == null) continue;
    const p = P[e.n] || (P[e.n] = { v: 0, c: 0, css: null });
    if (e.t === 'EAddToScale') p.c = (p.c || 0) + e.b;
    else if (e.t === 'EMultiplyScale') { if (e.b) p.c = (p.c || 0) * e.b; }
    else if (e.t === 'EMultiplyBase') p.v = (p.v || 0) * (1 + e.b / 100);
    else p.v = (p.v || 0) + e.b;
  }
  return P;
}
function abilityCards(H, levels, sp) {
  return (H.abilities || []).map(function (a, ai) {
    const level = (levels || [0, 0, 0, 0])[ai] || 0;
    const P = resolvedProps(a, level);
    const rows = Object.entries(P)
      .filter(e => ['tech_damage', 'damage', 'healing'].includes(e[1].css) && (e[1].v || e[1].c))
      .slice(0, 6)
      .map(([k, p]) => '<div>' + esc(p.label || k) + '</div><div>' + num(p.v, 1) +
        (p.c ? ' + ' + num(p.c, 3) + '×SP' : '') + (p.c ? ' → <b>' + num(p.v + sp * p.c, 0) + '</b>' : '') + '</div>').join('');
    const cd = (P.AbilityCooldown || {}).v;
    const ups = (a.upgrades || []).map((u, i) => {
      const bits = Object.entries(u).map(x => '<code>' + esc(x[0]) + '</code> ' + (x[1] >= 0 ? '+' : '') + num(x[1], 3)).join(', ');
      return `<div class="item p" style="margin-top:4px;opacity:${i < level ? 1 : .45}"><b>T${i + 1}${i < level ? ' ✓' : ''}</b> ${bits || '—'}</div>`;
    }).join('');
    return `<div class="card"><h4>${esc(a.name)}${a.ult ? ' <span class="tag act">ultimate</span>' : ''}` +
      `${cd ? ' <span class="tag">' + num(cd, 1) + 's cooldown</span>' : ''}</h4>` +
      (a.desc ? `<div class="item d">${esc(a.desc)}</div>` : '') +
      (rows ? `<div class="kv">${rows}</div>` : '') + `<div style="margin-top:8px">${ups}</div></div>`;
  }).join('');
}

/* ---------------- item tooltip ---------------- */
const TIP_SKIP = new Set(['AbilityUnitTargetLimit', 'AbilityCooldownBetweenCharge', 'ChannelMoveSpeed']);
function itemUptime(it) {
  const d = it.props.AbilityDuration || it.props.BuffDuration || 0, cd = it.props.AbilityCooldown || 0;
  if (d > 0 && cd <= 0) return 0.75;
  if (d <= 0 || cd <= 0) return 1;
  return Math.min(1, d / cd);
}
function itemTipHTML(name) {
  const it = D.items[name];
  if (!it) return '';
  const up = itemUptime(it), sec = it.sections || {};
  const rank = k => sec[k] === 'innate' ? 0 : (sec[k] ? 1 : 2);
  const rows = Object.entries(it.props || {})
    .filter(e => !TIP_SKIP.has(e[0]) && e[1])
    .sort((a, b) => rank(a[0]) - rank(b[0]))
    .map(([k, v]) => {
      const st = sec[k];
      const tag = st === 'innate' ? '<span class="tt-i">always on</span>'
        : (st ? '<span class="tt-c">' + Math.round(up * 100) + '% uptime</span>' : '');
      return `<div class="tt-row"><span>${esc(k)}</span><b>${num(v, 2)}</b>${tag}</div>`;
    }).join('');
  return `<div class="tt-head"><b>${esc(name)}</b><span class="tag">T${it.tier}</span><span class="tag">${it.slot}</span>` +
    (it.active ? '<span class="tag act">active</span>' : '') + `<span class="tt-cost">${commas(it.cost)}</span></div>` +
    (it.desc ? `<div class="tt-desc">${esc(it.desc)}</div>` : '') +
    `<div class="tt-rows">${rows || '<div class="tt-row"><span>no stats</span></div>'}</div>`;
}
let _tip = null;
function bindTips(root) {
  (root || document).querySelectorAll('[data-item]').forEach(function (node) {
    if (node.__tipped) return;
    node.__tipped = true;
    node.addEventListener('mouseenter', function () {
      if (!_tip) { _tip = document.createElement('div'); _tip.className = 'itemtip'; document.body.appendChild(_tip); }
      _tip.innerHTML = itemTipHTML(node.dataset.item);
      _tip.style.display = 'block';
      const r = node.getBoundingClientRect();
      let left = r.left + window.scrollX;
      if (left + 340 > window.innerWidth) left = Math.max(8, window.innerWidth - 350);
      _tip.style.top = (r.bottom + window.scrollY + 8) + 'px';
      _tip.style.left = left + 'px';
    });
    node.addEventListener('mouseleave', () => { if (_tip) _tip.style.display = 'none'; });
  });
}

/* ---------------- win rates ---------------- */
function winrates() {
  const map = {};
  const put = (arr, key) => {
    if (!arr) return;
    for (const m of arr) {
      const n = HERO_IDS[m.hero_id]; if (!n || !m.matches) continue;
      (map[n] = map[n] || {})[key] = m.wins / m.matches * 100;
    }
  };
  put(D.meta_all, 'all'); put(D.meta_high, 'hi'); put(D.meta_low, 'lo');
  return map;
}

/* ---------------- the answer ---------------- */
function orderTable(order) {
  const steps = order.map((o, i) => {
    const it = D.items[o.item] || {};
    const pre = o.kind === 'upgrade' ? `<span class="from">${itemIcon(o.from, 18)}${esc(o.from)} →</span> ` : '';
    const walker = o.after_walker ? '<span class="tag act" title="needs the slot from the next destroyed Walker">after Walker</span>' : '';
    return `<tr><td class="rankno">${i + 1}</td><td class="buy" data-item="${esc(o.item)}"><span class="sw" style="background:var(--${slotColor(o.slot)})"></span>` +
      `${pre}${itemIcon(o.item, 26)}<b>${esc(o.item)}</b> <span class="tag">T${o.tier}</span>${it.active ? '<span class="tag act">act</span>' : ''}${walker}</td>` +
      `<td>${commas(o.cost)}</td><td>${commas(o.running)}</td><td>${o.net_worth ? commas(o.net_worth) : '-'}</td>` +
      `<td>${o.slots}${o.slots_open ? '/' + o.slots_open : ''}</td>` +
      `<td>+${o.invest[0]}/+${o.invest[1]}/+${o.invest[2]}</td><td>${o.gun}</td><td>${o.heal}</td><td><b>${o.score.toFixed(2)}</b></td></tr>`;
  }).join('');
  return '<div class="tablewrap"><table class="order"><thead><tr><th class="rankno">#</th><th>buy</th><th>souls</th><th>spent</th>' +
    '<th>net worth</th><th>slots</th><th>invest W/V/S</th><th>gun DPS</th><th>heal/s</th><th>score</th></tr></thead><tbody>' +
    (steps || '<tr><td colspan="10">no order computed</td></tr>') + '</tbody></table></div>';
}
function topTable(overall, n, label) {
  const rows = Object.entries(overall).sort((a, b) => b[1] - a[1]).slice(0, n);
  return `<div class="tablewrap"><table><thead><tr><th class="rankno">#</th><th>hero</th><th>${label}</th></tr></thead><tbody>` +
    rows.map((e, i) => `<tr class="clickable${i === 0 ? ' top' : ''}" data-open="${esc(e[0])}"><td class="rankno">${i + 1}</td>` +
      `<td class="hero">${heroIcon(e[0])}${esc(e[0])}</td><td><b>${num(e[1], 3)}</b></td></tr>`).join('') + '</tbody></table></div>';
}
function portrait(h) {
  const img = (D.heroes[h] || {}).img || {};
  return img.card ? `<img class="portrait" src="${img.card}" alt="${esc(h)}">` : '';
}
function secondCard() {
  const TF = table('teamfight'), AR = table('allround');
  const tfTop = Object.entries(TF.overall).sort((a, b) => b[1] - a[1]);
  const arTop = Object.entries(AR.overall).sort((a, b) => b[1] - a[1]);
  if (arTop[0][0] !== tfTop[0][0]) {
    return `<div class="card herocard">${portrait(arTop[0][0])}` +
      `<div><h4>All-round #1 (pick + skirmish + teamfight)</h4><div class="big">${esc(arTop[0][0])}</div>` +
      `<p>All-round score <b>${num(arTop[0][1], 3)}</b>. The all-round table keeps 15% weight on isolated picks.</p>` +
      `<button class="btn" data-go="rank">Full rankings →</button></div></div>`;
  }
  const hero = tfTop[1][0], full = TF.stages.full.find(r => r.hero === hero);
  return `<div class="card herocard">${portrait(hero)}` +
    `<div><h4>Runner-up (teamfight)</h4><div class="big">${esc(hero)}</div>` +
    `<p>Teamfight ${num(tfTop[1][1], 3)} · all-round #${1 + arTop.findIndex(e => e[0] === hero)}. ` +
    `${esc(tfTop[0][0])} is #1 in <b>both</b> tables (all-round ${num(arTop[0][1], 3)}).</p>` +
    kv({ 'Full build DPS on target': num(full.total_dps, 0), 'Net healing': num(full.heal_ps, 0) + '/s',
      'Effective HP': commas(full.ehp) }) +
    `<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap"><button class="btn" data-open="${esc(hero)}" data-stage="full" data-obj="teamfight">${esc(hero)}'s build →</button>` +
    `<button class="btn" data-go="rank">Full rankings →</button></div></div></div>`;
}
function renderAnswer() {
  const O = D.optimization;
  if (!O) { $('#answerBody').innerHTML = '<p class="note">no optimisation data</p>'; return; }
  const TF = table('teamfight'), AR = table('allround');
  const tfTop = Object.entries(TF.overall).sort((a, b) => b[1] - a[1]);
  const arTop = Object.entries(AR.overall).sort((a, b) => b[1] - a[1]);
  const hero = tfTop[0][0];
  const late = TF.stages.late.find(r => r.hero === hero);
  const full = TF.stages.full.find(r => r.hero === hero);
  const lateRank = 1 + TF.stages.late.filter(r => r.score > late.score).length;
  const fullRank = 1 + TF.stages.full.filter(r => r.score > full.score).length;

  const stageRows = STAGES.map(([st]) => {
    const rows = TF.stages[st], r = rows.find(x => x.hero === hero);
    const rank = 1 + rows.filter(x => x.score > r.score).length;
    return `<tr><td>${STAGE_LABEL[st]}</td><td>${r.items.length}</td><td>${num(r.total_dps, 0)}</td>` +
      `<td>${num(r.heal_ps, 0)}</td><td>${commas(r.ehp)}</td><td>${num(r.score, 3)}</td>` +
      `<td class="${rank === 1 ? 'ok' : ''}"><b>#${rank}</b></td><td>${rank === 1 ? '—' : esc(rows[0].hero) + ' ' + num(rows[0].score, 3)}</td></tr>`;
  }).join('');

  let bench = '';
  const B = D.benchmarks;
  if (B && B.cases && B.cases.length) {
    bench = '<h3>Benchmark: a real high-performing build</h3>' + B.cases.map(c => {
      const diff = c.solved.teamfight / c.given.teamfight;
      return `<div class="card"><h4>${esc(c.label)}</h4><p class="note" style="border:0;padding:0;background:none">${esc(c.note || '')}</p>` +
        `<div class="grid2"><div><b>Their build</b> — ${commas(c.given.spend)} souls, ${c.given.items.length} items${chips(c.given.items)}` +
        kv({ 'Teamfight score': num(c.given.teamfight, 3), 'All-round score': num(c.given.allround, 3),
          'Teamfight DPS': num(c.given.tf_dps, 0), 'Teamfight heal/s': num(c.given.tf_heal, 0), 'Effective HP': commas(c.given.ehp) }) +
        `</div><div><b>Solved build at the same net worth (${commas(c.net_worth)})</b> — ${commas(c.solved.spend)} souls${chips(c.solved.items)}` +
        kv({ 'Teamfight score': '<b>' + num(c.solved.teamfight, 3) + '</b> (' + num(diff, 2) + '× theirs)', 'All-round score': num(c.solved.allround, 3),
          'Teamfight DPS': num(c.solved.tf_dps, 0), 'Teamfight heal/s': num(c.solved.tf_heal, 0), 'Effective HP': commas(c.solved.ehp) }) +
        `</div></div>` + (c.same_budget ? `<p class="note">${esc(c.same_budget)}</p>` : '') + '</div>';
    }).join('');
  }

  const S = D.sensitivity;
  const robust = S ? (() => {
    const wins = Object.values(S.winners).filter(h => h === hero).length;
    const r = S.top10[hero];
    return `<p class="note" style="margin:0 0 12px">Robustness: #1 in <b>${wins} of ${Object.keys(S.winners).length}</b> ` +
      `model variants (fight window 15–30 s, healing floor 15–40%, splash value 25–75%)` +
      (r ? `, rank range #${r.best_rank}–#${r.worst_rank}` : '') + '.</p>';
  })() : '';

  $('#answerBody').innerHTML =
    `<h2>Best sustain + damage build for teamfights</h2>` + robust +
    `<div class="grid2"><div class="card herocard">${portrait(hero)}` +
    `<div><h4>Teamfight #1 (stage-weighted)</h4><div class="big">${esc(hero)}</div>` +
    `<p>Teamfight score <b>${num(tfTop[0][1], 3)}</b> vs #2 ${esc(tfTop[1][0])} ${num(tfTop[1][1], 3)}. ` +
    `Late (32k) rank <b>#${lateRank}</b>, full (50k) rank <b>#${fullRank}</b>.</p>` +
    kv({ 'Full build DPS on target': num(full.total_dps, 0), '+ splash (Ricochet / AoE)': num(full.cleave_dps, 0),
      'Net healing (after anti-heal)': num(full.heal_ps, 0) + '/s', 'Healing ÷ incoming': num(full.sustain_ratio * 100, 0) + '%',
      'Effective HP': commas(full.ehp), 'Time to kill / to die': num(full.ttk, 1) + 's / ' + num(full.ttd, 1) + 's' }) +
    `</div></div>` + secondCard() + `</div>` +

    `<h3>The build — ${esc(hero)}, full (${commas(full.spend)} souls, ${full.items.length}/${slotsAt(full.budget)} slots)</h3>` +
    chips(full.items) +
    `<p class="note" style="margin-top:12px">Ordered by affordability and routed through <b>components</b>: cheap parts first, ` +
    `upgraded for the difference. Ability tiers: <b>${(full.ability_levels || []).join(' / ')}</b> (${full.ability_points} points).</p>` +
    orderTable(orderFor(hero, 'full', 'teamfight')) +
    `<h3>${esc(hero)} at every stage (teamfight objective)</h3>` +
    '<div class="tablewrap"><table><thead><tr><th>stage</th><th>items</th><th>DPS</th><th>heal/s</th><th>EHP</th><th>score</th>' +
    '<th>rank</th><th>stage #1</th></tr></thead><tbody>' + stageRows + '</tbody></table></div>' +
    `<button class="btn" style="margin-top:12px" data-open="${esc(hero)}" data-obj="teamfight">Every stage's build and purchase order →</button>` +
    bench +
    `<h3>Top 10</h3><div class="grid2"><div><b>Teamfight</b>${topTable(TF.overall, 10, 'score')}</div>` +
    `<div><b>All-round</b>${topTable(AR.overall, 10, 'score')}</div></div>` +
    `<p class="note" style="margin-top:14px">This is a combat model: sustained damage, healing and survival under focus fire. ` +
    `It does not price crowd control, mobility, objectives or team utility. See <b>Method</b> for every assumption.</p>`;
}

/* ---------------- rankings ---------------- */
let rankSort = { col: 'score', dir: -1 };
function renderRank() {
  const stage = $('#rankStage').value, objective = $('#rankObj').value, WR = winrates();
  const T = table(objective);
  let rows;
  if (stage === 'overall') {
    rows = Object.entries(T.overall).map(([h, s]) => {
      const r = T.stages.late.find(x => x.hero === h) || {};
      return { hero: h, score: s, dps: r.total_dps, heal: r.heal_ps, ehp: r.ehp, sustain: r.sustain_ratio };
    });
    $('#refBox').innerHTML = `<b>${OBJ_LABEL[objective]}, stage-weighted</b> — ` +
      Object.entries(D.optimization.stage_weight).map(([k, v]) => `${k} ${(v * 100).toFixed(0)}%`).join(' · ') +
      ' · DPS / heal / EHP columns show the late (32k) build';
  } else {
    rows = T.stages[stage].map(r => ({ hero: r.hero, score: r.score, dps: r.total_dps, heal: r.heal_ps, ehp: r.ehp, sustain: r.sustain_ratio }));
    const ref = D.optimization.refs[stage];
    $('#refBox').innerHTML = `<b>Reference opponent</b> (median hero on its own solved build): ` +
      `health <b>${commas(ref.health)}</b> · DPS <b>${num(ref.dps, 0)}</b> · bullet resist <b>${num(ref.bullet_resist)}%</b> · ` +
      `spirit resist <b>${num(ref.tech_resist)}%</b>`;
  }
  rows.forEach(r => { const w = WR[r.hero] || {}; r.wr = w.all; r.hi = w.hi; });
  rows.sort((a, b) => {
    if (rankSort.col === 'hero') return a.hero.localeCompare(b.hero) * rankSort.dir;
    const A = a[rankSort.col], B = b[rankSort.col];
    if (A == null) return 1; if (B == null) return -1; return (A - B) * rankSort.dir;
  });
  const cols = [['hero', 'Hero'], ['score', 'Score'], ['dps', 'DPS'], ['heal', 'Heal/s'], ['sustain', 'Heal ÷ incoming'],
    ['ehp', 'EHP'], ['wr', 'Win % (all)'], ['hi', 'Win % (Asc+)']];
  const max = Math.max(...rows.map(r => r.score || 0));
  let h = '<thead><tr><th class="rankno">#</th>' + cols.map(c => `<th data-c="${c[0]}">${c[1]}</th>`).join('') + '</tr></thead><tbody>';
  rows.forEach((r, i) => {
    h += `<tr class="clickable${i === 0 && rankSort.col === 'score' ? ' top' : ''}" data-hero="${esc(r.hero)}"><td class="rankno">${i + 1}</td><td class="hero">${heroIcon(r.hero)}${esc(r.hero)}</td>` +
      `<td>${num(r.score, 3)} <span class="bar" style="width:${Math.max(1, (r.score / max) * 46)}px"></span></td>` +
      `<td>${num(r.dps, 0)}</td><td>${num(r.heal, 0)}</td><td>${r.sustain != null ? num(r.sustain * 100, 0) + '%' : '-'}</td>` +
      `<td>${commas(r.ehp || 0)}</td><td>${r.wr ? num(r.wr, 2) + '%' : '-'}</td><td>${r.hi ? num(r.hi, 2) + '%' : '-'}</td></tr>`;
  });
  $('#rankTable').innerHTML = h + '</tbody>';
  $('#rankTable').querySelectorAll('tr.clickable').forEach(tr => tr.onclick = () =>
    openHero(tr.dataset.hero, stage === 'overall' ? 'late' : stage, objective));
  $('#rankTable').querySelectorAll('th[data-c]').forEach(th => th.onclick = () => {
    const c = th.dataset.c;
    rankSort = { col: c, dir: rankSort.col === c ? -rankSort.dir : (c === 'hero' ? 1 : -1) };
    renderRank();
  });
}

/* ---------------- hero build page ---------------- */
function slotsAt(nw) {
  const w = ((D.optimization.model || {}).walker_net_worth) || [16000, 26000, 36000];
  return 9 + w.filter(x => nw >= x).length;
}
function slotLabel(r) {
  const used = (r.items || []).length, open = slotsAt(r.budget || 0);
  const headroom = (r.budget || 0) - (r.spend || 0);
  return `${used}/${open} slots` + (used < open && headroom < 800 ? ' · budget-limited' : '');
}
function showTab(name) {
  document.querySelectorAll('nav button').forEach(x => x.classList.toggle('on', x.dataset.tab === name));
  document.querySelectorAll('.tab').forEach(x => x.classList.toggle('on', x.id === name));
}
function openHero(hero, stage, objective) {
  renderHeroBuild(hero, stage || 'late', objective || 'teamfight');
  const btn = $('#buildTabBtn');
  btn.style.display = ''; btn.textContent = hero;
  showTab('build');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
function renderHeroBuild(hero, stage, objective) {
  const T = table(objective), H = D.heroes[hero];
  const r = (T.stages[stage] || []).find(x => x.hero === hero);
  if (!r) { $('#buildBody').innerHTML = '<p class="note">no solved build</p>'; return; }
  const rank = 1 + T.stages[stage].filter(x => x.score > r.score).length;
  const WR = winrates()[hero] || {};
  const img = H.img || {};
  const sc = r.scenario_scores || {};
  const scen = Object.entries(sc).map(([k, v]) => `<span class="chip"><b>${k}</b><span>${num(v, 3)}</span></span>`).join('');
  $('#buildBody').innerHTML = `
  <div class="controls">
    <label>Stage <select id="bdStage">${STAGES.map(([x]) => `<option value="${x}"${x === stage ? ' selected' : ''}>${STAGE_LABEL[x]}</option>`).join('')}</select></label>
    <label>Objective ${objSelect('bdObj', objective)}</label>
    <button class="btn" data-lab="${esc(hero)}" data-stage="${stage}" data-obj="${objective}">Open in Build Lab</button>
  </div>
  <div class="card" style="display:flex;gap:22px;align-items:flex-start;flex-wrap:wrap">
    ${img.card ? `<img src="${img.card}" alt="${esc(hero)}" style="width:170px;border-radius:var(--r);background:var(--panel2);object-fit:cover">` : ''}
    <div style="flex:1;min-width:280px">
      <h2 style="margin:0 0 4px">${esc(hero)}</h2>
      <p class="sub" style="margin:0 0 12px">${OBJ_LABEL[objective]} rank <b>#${rank} of ${T.stages[stage].length}</b> at ${STAGE_LABEL[stage]}
        · real win rate ${WR.all ? num(WR.all, 2) + '%' : '–'} ${WR.hi ? `(Ascendant+ ${num(WR.hi, 2)}%)` : ''}</p>
      <div class="kv" style="max-width:560px">
        <div>Score</div><div><b>${num(r.score, 3)}</b></div>
        <div>DPS on target</div><div>${num(r.total_dps, 0)} — gun ${num(r.gun_dps, 0)} · abilities ${num(r.ability_dps, 0)} · item procs ${num(r.item_proc_dps || 0, 0)}</div>
        <div>Splash damage (Ricochet / AoE)</div><div>${num(r.cleave_dps || 0, 0)}</div>
        <div>Net healing</div><div>${num(r.heal_ps, 0)} /s (${num((r.sustain_ratio || 0) * 100, 0)}% of incoming)</div>
        <div>Effective HP</div><div>${commas(r.ehp || 0)}</div>
        <div>Resists (bullet / spirit)</div><div>${num(r.bullet_resist, 1)}% / ${num(r.tech_resist, 1)}%</div>
        <div>Lifesteal (bullet / spirit)</div><div>${num(r.bullet_lifesteal, 1)}% / ${num(r.spirit_lifesteal, 1)}%</div>
        <div>Spirit Power · Boons</div><div>${num(r.spirit_power, 0)} · ${r.boons}</div>
        <div>Souls spent</div><div>${commas(r.spend || 0)} of ${commas(r.budget)}</div>
        <div>Slots</div><div>${slotLabel(r)}</div>
      </div>
      <div class="chips" style="margin-top:12px">${scen}</div>
    </div>
  </div>
  <h3>Items</h3>${chips(r.items)}
  <h3>Buy in this order</h3>
  <p class="note">At each step the best remaining purchase per soul, paced so you never open with a tier-4 you cannot afford.
  <b>invest W/V/S</b> is the cumulative weapon / vitality / spirit Investment bonus.</p>
  ${orderTable(orderFor(hero, stage, objective))}
  <h3>Ability allocation — ${r.ability_points} points · tiers ${(r.ability_levels || []).join(' / ')}</h3>
  <div class="grid2">${abilityCards(H, r.ability_levels, r.spirit_power || 0)}</div>`;
  $('#bdStage').onchange = () => renderHeroBuild(hero, $('#bdStage').value, $('#bdObj').value);
  $('#bdObj').onchange = () => renderHeroBuild(hero, $('#bdStage').value, $('#bdObj').value);
}

/* ---------------- all builds ---------------- */
function renderBuilds() {
  const stage = $('#bStage').value, sort = $('#bSort').value, objective = $('#bObj').value;
  const q = ($('#bFilter').value || '').toLowerCase();
  let rows = table(objective).stages[stage].slice();
  if (q) rows = rows.filter(r => r.hero.toLowerCase().includes(q) || (r.items || []).some(i => i.toLowerCase().includes(q)));
  const key = { score: r => -r.score, dps: r => -r.total_dps, heal: r => -r.heal_ps };
  rows.sort(sort === 'hero' ? (a, b) => a.hero.localeCompare(b.hero) : (a, b) => key[sort](a) - key[sort](b));
  $('#buildList').innerHTML = rows.map((r, i) =>
    `<div class="card clickable" data-open="${esc(r.hero)}" data-stage="${stage}" data-obj="${objective}" style="cursor:pointer">
      <h4>${heroIcon(r.hero, 'hicon lg')}${i + 1}. ${esc(r.hero)} <span class="pill">score ${num(r.score, 3)}</span> <span class="tag">${slotLabel(r)}</span></h4>
      <div class="kv" style="margin-bottom:6px;max-width:520px">
        <div>DPS</div><div>${num(r.total_dps, 0)}</div><div>Healing</div><div>${num(r.heal_ps, 0)} /s</div>
        <div>Effective HP</div><div>${commas(r.ehp || 0)}</div><div>Spent</div><div>${commas(r.spend || 0)} souls</div>
      </div>${chips(r.items)}</div>`).join('') || '<p class="note">no matches</p>';
}

/* ---------------- hero stat browser ---------------- */
let heroReq = 0;
async function renderHero() {
  const hero = $('#heroSel').value, nw = +$('#heroNW').value;
  $('#heroNWval').textContent = commas(nw);
  const H = D.heroes[hero], w = H.weapon, pb = H.per_boon, b = H.base;
  const img = H.img || {};
  const apiPart = API ? '<div id="heroApi" class="card"><h4>At this net worth (no items)</h4><p class="note">computing…</p></div>' : '';
  const solved = STAGES.map(([st]) => {
    const r = table('teamfight').stages[st].find(x => x.hero === hero);
    const rank = 1 + table('teamfight').stages[st].filter(x => x.score > r.score).length;
    return `<tr class="clickable" data-open="${esc(hero)}" data-stage="${st}" data-obj="teamfight"><td>${STAGE_LABEL[st]}</td><td>#${rank}</td><td>${num(r.score, 3)}</td><td>${num(r.total_dps, 0)}</td><td>${num(r.heal_ps, 0)}</td><td>${commas(r.ehp)}</td></tr>`;
  }).join('');
  $('#heroDetail').innerHTML = `
    <div class="grid2"><div class="card" style="display:flex;gap:16px">
      ${img.card ? `<img src="${img.card}" alt="" style="width:120px;border-radius:var(--r);object-fit:cover">` : ''}
      <div style="flex:1">${kv({
        'Base health': commas(b.max_health), 'Health per boon': num(pb.health, 1),
        'Base regen': num(b.base_health_regen, 1) + '/s', 'Spirit per boon': num(pb.spirit_power, 2),
        'Bullet damage': num(w.bullet_damage, 2) + (w.bullets > 1 ? ' × ' + w.bullets + ' pellets' : ''),
        'Bullet dmg per boon': num(pb.bullet_damage, 3), 'Clip · reload': num(w.clip_size, 0) + ' · ' + num(w.reload_duration, 2) + 's',
        'Shipped DPS (with reload)': num(w.dps_reload, 1), 'Headshot multiplier': num(w.headshot, 2) + '×',
        'Falloff': num(w.falloff_start_m, 1) + 'm → ' + num(w.falloff_end_m, 1) + 'm (' + num((w.falloff_scale ?? 1) * 100, 0) + '%)' })}</div>
    </div>${apiPart}</div>
    <h3>Solved teamfight builds</h3>
    <div class="tablewrap"><table><thead><tr><th>stage</th><th>rank</th><th>score</th><th>DPS</th><th>heal/s</th><th>EHP</th></tr></thead><tbody>${solved}</tbody></table></div>
    <h3>Abilities (base tier)</h3><div class="grid2">${abilityCards(H, [0, 0, 0, 0], 0)}</div>`;
  if (!API) return;
  const my = ++heroReq;
  try {
    const res = await api('/api/evaluate', { hero, items: [], net_worth: nw, objective: 'teamfight' });
    if (my !== heroReq) return;
    const s = res.stats;
    $('#heroApi').innerHTML = `<h4>At ${commas(nw)} net worth (no items)</h4>` + kv({
      'Boons': s.boons, 'Ability points': res.ability_points, 'Health': commas(s.health),
      'Spirit Power': num(s.spirit_power, 1), 'Gun DPS': num(s.weapon_dps, 1), 'Ability DPS (sustained)': num(s.ability_dps, 1),
      'Bullet / spirit resist': num(s.bullet_resist, 1) + '% / ' + num(s.spirit_resist, 1) + '%', 'Effective HP': commas(s.ehp) });
  } catch (e) { /* server not running: static view is enough */ }
}

/* ---------------- item browser ---------------- */
function renderItems() {
  const slot = $('#itemSlot').value, tier = $('#itemTier').value, q = ($('#itemSearch').value || '').toLowerCase();
  const list = Object.entries(D.items)
    .filter(([n, it]) => (!slot || it.slot === slot) && (!tier || String(it.tier) === tier) &&
      (!q || n.toLowerCase().includes(q) || (it.desc || '').toLowerCase().includes(q) ||
        Object.keys(it.props || {}).some(k => k.toLowerCase().includes(q))))
    .sort((a, b) => a[1].slot.localeCompare(b[1].slot) || a[1].tier - b[1].tier || a[0].localeCompare(b[0]));
  $('#itemList').innerHTML = list.map(([n, it]) => {
    const props = Object.entries(it.props || {}).filter(([k, v]) => v && !TIP_SKIP.has(k)).slice(0, 8)
      .map(([k, v]) => `${esc(k)} <b>${num(v, 2)}</b>`).join(' · ');
    return `<div class="item ${it.slot}" data-item="${esc(n)}"><span class="cost">${commas(it.cost)}</span>` +
      `<div class="nm">${itemIcon(n, 30)}${esc(n)} <span class="tag">T${it.tier}</span>${it.active ? '<span class="tag act">active</span>' : ''}</div>` +
      `<div class="d">${esc(it.desc || '')}</div><div class="p">${props}</div></div>`;
  }).join('') || '<p class="note">no items match</p>';
}

/* ---------------- build lab (Python model via API) ---------------- */
let build = [], labReq = 0;
async function api(path, body) {
  const r = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
  const j = await r.json();
  if (!r.ok) throw new Error(j.error || r.statusText);
  return j;
}
function labShop() {
  const nw = +$('#labNW').value, q = ($('#labSearch').value || '').toLowerCase();
  const spend = build.reduce((a, n) => a + D.items[n].cost, 0);
  const actives = build.filter(n => D.items[n].active).length, open = slotsAt(nw);
  $('#labCount').textContent = `${build.length}/${open} slots · ${actives}/${MAX_ACTIVES} actives · ${commas(spend)} / ${commas(nw)} souls`;
  $('#labBuild').innerHTML = build.map((n, idx) => {
    const i = D.items[n];
    return `<div class="buildrow ${i.slot}" data-item="${esc(n)}"><span>${itemIcon(n)}${idx + 1}. ${esc(n)} <span class="tag">T${i.tier}</span>${i.active ? '<span class="tag act">act</span>' : ''}</span>` +
      `<span>${commas(i.cost)} <button data-rm="${idx}" title="remove">×</button></span></div>`;
  }).join('') || '<div class="note">empty — click items below, or load / optimise a build</div>';
  const full = build.length >= open;
  $('#labShop').innerHTML = Object.entries(D.items)
    .filter(([n]) => !q || n.toLowerCase().includes(q))
    .sort((a, b) => a[1].tier - b[1].tier || a[0].localeCompare(b[0]))
    .map(([n, i]) => {
      const dis = build.includes(n) || full || spend + i.cost > nw || (i.active && actives >= MAX_ACTIVES);
      return `<div class="shoprow ${dis ? 'dis' : ''}" data-add="${dis ? '' : esc(n)}" data-item="${esc(n)}">` +
        `<span>${itemIcon(n, 20)}${esc(n)}${i.active ? '<span class="tag act">act</span>' : ''}</span>` +
        `<span>T${i.tier} · ${commas(i.cost)}</span></div>`;
    }).join('');
}
async function renderLab() {
  labShop();
  if (!API) {
    $('#labStats').innerHTML = '<div class="card"><h4>Model server not running</h4><p>The Build Lab evaluates builds with the Python model. Start it with</p>' +
      '<pre>python scripts/serve.py</pre><p>and reload this page (http://localhost:8777).</p></div>';
    return;
  }
  const hero = $('#labHero').value, nw = +$('#labNW').value, objective = $('#labObj').value;
  const my = ++labReq;
  $('#labStats').style.opacity = .55;
  try {
    const res = await api('/api/evaluate', { hero, items: build, net_worth: nw, objective });
    if (my !== labReq) return;
    labResult(res);
  } catch (e) {
    $('#labStats').innerHTML = `<div class="card"><h4>Evaluation failed</h4><p class="warn">${esc(e.message)}</p></div>`;
  } finally { $('#labStats').style.opacity = 1; }
}
function labResult(res) {
  const s = res.stats;
  const scen = Object.entries(res.scenarios).map(([name, r]) =>
    `<tr><td>${name} <span class="tag">${num(res.weights[name] * 100, 0)}%</span></td><td><b>${num(r.score, 3)}</b></td>` +
    `<td>${num(r.total_dps, 0)}</td><td>${num(r.cleave_dps, 0)}</td><td>${num(r.heal_ps, 0)}</td>` +
    `<td>${num(r.effective_incoming, 0)}</td><td>${num(r.ttk, 1)}s</td><td>${num(r.ttd, 1)}s</td></tr>`).join('');
  const other = Object.entries(res.scores).filter(([k]) => k !== res.objective).map(([k, v]) => `${OBJ_LABEL[k]} ${num(v, 3)}`).join('');
  $('#labStats').innerHTML = `
    <div class="card"><h4>${OBJ_LABEL[res.objective]} score vs a ${commas(res.net_worth)}-soul median opponent</h4>
      <div class="big">${num(res.score, 3)}</div>
      <div class="note" style="border:0;padding:0;margin:0 0 10px;background:none">weighted geometric mean of scenario scores
        (time-to-die ÷ time-to-kill; above 1.0 wins the exchange) · ${other} · ability tiers ${res.ability_levels.join('/')}
        ${res.legal ? '' : ' · <span class="warn">not a legal build</span>'}</div>
      <div class="tablewrap" style="margin-top:6px"><table><thead><tr><th>scenario</th><th>score</th><th>DPS</th><th>splash</th>
        <th>heal/s</th><th>incoming</th><th>TTK</th><th>TTD</th></tr></thead><tbody>${scen}</tbody></table></div></div>
    <div class="card"><h4>Derived stats</h4>${kv({
      'Boons · ability points': s.boons + ' · ' + res.ability_points,
      'Spirit Power': '<b>' + num(s.spirit_power, 1) + '</b>',
      'Weapon damage bonus': '+' + num(s.weapon_pct, 1) + '%', 'Damage per bullet': num(s.bullet_damage, 2),
      'Fire rate bonus': '+' + num(s.fire_rate_pct, 1) + '%', 'Clip size': num(s.clip, 1),
      'Gun DPS (sustained, no resist)': num(s.weapon_dps, 1), 'Ability DPS (sustained)': num(s.ability_dps, 1),
      'Health · barrier': commas(s.health) + ' · ' + num(s.barrier, 0), 'Effective HP (60/40 mix)': '<b>' + commas(s.ehp) + '</b>',
      'Bullet / spirit resist': num(s.bullet_resist, 1) + '% / ' + num(s.spirit_resist, 1) + '%',
      'Bullet / spirit lifesteal': num(s.bullet_lifesteal, 1) + '% / ' + num(s.spirit_lifesteal, 1) + '%',
      'Cooldown reduction': num(s.cdr, 1) + '%',
      'Self-damage drain': s.self_drain ? '<span class="warn">−' + num(s.self_drain, 0) + '/s</span>' : '0' })}</div>
    <div class="card"><h4>Investments</h4>${kv({
      'Weapon': commas(s.invest.weapon[0]) + ' → <b>+' + num(s.invest.weapon[1], 0) + '% weapon damage</b>',
      'Vitality': commas(s.invest.vitality[0]) + ' → <b>+' + num(s.invest.vitality[1], 0) + '% health</b>',
      'Spirit': commas(s.invest.spirit[0]) + ' → <b>+' + num(s.invest.spirit[1], 0) + ' spirit power</b>' })}
      <div class="note" style="border:0;padding:0;margin-top:8px;background:none">The biggest single step is at 4,800 souls per category.</div></div>`;
}
async function labOptimize() {
  if (!API) return renderLab();
  const hero = $('#labHero').value, nw = +$('#labNW').value, objective = $('#labObj').value;
  const btn = $('#labOpt'); btn.disabled = true; btn.textContent = 'Optimising… (~20–60 s)';
  try {
    const res = await api('/api/optimize', { hero, net_worth: nw, objective, items: build, iterations: 4 });
    build = res.items.slice();
    labShop(); labResult(res);
  } catch (e) {
    $('#labStats').innerHTML = `<div class="card"><h4>Optimisation failed</h4><p class="warn">${esc(e.message)}</p></div>`;
  } finally { btn.disabled = false; btn.textContent = 'Optimise this build'; }
}
function labLoadSolved() {
  const hero = $('#labHero').value, nw = +$('#labNW').value, objective = $('#labObj').value;
  let best = STAGES[0]; for (const s of STAGES) if (Math.abs(s[1] - nw) < Math.abs(best[1] - nw)) best = s;
  const r = table(objective).stages[best[0]].find(x => x.hero === hero);
  if (r) { build = r.items.slice(); $('#labNW').value = best[1]; renderLab(); }
}

/* ---------------- pro evidence ---------------- */
function renderPro() {
  const P = D.pro_ranking;
  if (!P || !P.ranking || !P.ranking.length) { $('#proBody').innerHTML = '<h2>Pro-play evidence</h2><p class="note">no snapshot</p>'; return; }
  const top = P.ranking[0], weights = P.meta.weights;
  const combatTop = Object.entries(table('allround').overall).sort((a, b) => b[1] - a[1])[0][0];
  const ct = P.ranking.find(r => r.hero === combatTop);
  const rows = P.ranking.map(r => {
    const c = r.components;
    return `<tr${r.rank === 1 ? ' class="top"' : ''}><td class="rankno">${r.rank}</td><td class="hero">${esc(r.hero)}</td>` +
      `<td><b>${num(r.score, 1)}</b> <span class="bar" style="width:${Math.max(1, r.score * .46)}px"></span></td>` +
      `<td>${num(c.combat, 0)}</td><td>${num(c.high_skill_outcome, 0)}</td><td>${num(c.draft_priority, 0)}</td><td>${num(c.macro_breadth, 0)}</td>` +
      `<td>${num(r.adjusted_win_rate, 2)}%</td><td>${commas(r.matches)}</td>` +
      `<td>#${r.sensitivity_rank_min}${r.sensitivity_rank_max !== r.sensitivity_rank_min ? '–#' + r.sensitivity_rank_max : ''}</td></tr>`;
  }).join('');
  $('#proBody').innerHTML = `<h2>Pro-play evidence <span class="tag">experimental</span></h2>
    <div class="grid2"><div class="card"><h4>Evidence #1</h4><div class="big">${esc(top.hero)} · ${num(top.score, 1)}/100</div>
      <p class="note" style="border:0;padding:0;background:none">Blends the combat model with patch-current Ascendant+ outcomes, pick/ban pressure and macro proxies.</p></div>
    ${ct ? `<div class="card"><h4>Combat-model #1 (${esc(combatTop)}) in this index</h4><div class="big">#${ct.rank} · ${num(ct.score, 1)}/100</div>
      <p class="note" style="border:0;padding:0;background:none">Adjusted Ascendant+ win strength ${num(ct.adjusted_win_rate, 2)}% · sensitivity #${ct.sensitivity_rank_min}–#${ct.sensitivity_rank_max}.</p></div>` : ''}</div>
    <div class="refbox"><b>Sample:</b> ${commas(P.sample.estimated_matches)} Ascendant+ ranked matches · ${commas(P.sample.total_bans)} bans ·
      fetched ${P.meta.fetched_at.slice(0, 10)} · <b>Weights:</b> combat ${num(weights.combat * 100, 0)}% · outcome ${num(weights.high_skill_outcome * 100, 0)}% ·
      pick/ban ${num(weights.draft_priority * 100, 0)}% · macro ${num(weights.macro_breadth * 100, 0)}%</div>
    <div class="tablewrap"><table><thead><tr><th class="rankno">#</th><th>hero</th><th>evidence score</th><th>combat pct</th><th>outcome pct</th>
      <th>draft pct</th><th>macro pct</th><th>adjusted WR</th><th>sample</th><th>sensitivity</th></tr></thead><tbody>${rows}</tbody></table></div>`;
}

/* ---------------- method ---------------- */
function renderMethod() {
  const M = D.optimization.model || {};
  const sc = M.scenarios || {};
  const scRows = Object.values(sc).map(s => `<tr><td>${s.name}</td><td>${num(s.weight * 100, 0)}%</td>` +
    `<td>${num((M.objectives.teamfight[s.name] || 0) * 100, 0)}%</td><td>${s.focus}×</td><td>${s.antiheal}%</td>` +
    `<td>${num(s.bullet_frac * 100, 0)}%</td><td>${s.distances.map(d => d[0] + 'm·' + num(d[1] * 100, 0) + '%').join(' ')}</td>` +
    `<td>${num(s.isolation * 100, 0)}%</td></tr>`).join('');
  $('#methodBody').innerHTML = `
  <p>Hero and item numbers come from Valve's shipped game files (parsed <code>.vdata</code> via the community assets API);
  patch baseline <b>${esc(D.meta.patch)}</b> — still the live patch. Mechanics that the files do not spell out were checked against
  deadlock.wiki pages (Items, Lifesteal, Siphon Bullets, Lucky Shot, Inhibitor, Ricochet, Escalating Resilience, Burst Fire,
  Toxic Bullets, Juggernaut, Hunter's Aura, Mercurial Magnum, Drifter).</p>
  <h3>Scenarios</h3>
  <div class="tablewrap"><table><thead><tr><th>scenario</th><th>all-round weight</th><th>teamfight weight</th><th>focus fire</th>
    <th>anti-heal</th><th>bullet share</th><th>engagement distances</th><th>target isolated</th></tr></thead><tbody>${scRows}</tbody></table></div>
  <pre>scenario score = time-to-die / time-to-kill
TTK  = reference health / (your damage on target + 50% of splash damage)
TTD  = your health pool / max(25% of incoming, incoming − net healing)
incoming = reference DPS × focus × (your enemy debuffs) × your mixed resist multiplier
net healing = (lifesteal + regen + cast heals) × (1 − anti-heal) + Siphon Bullets − self-drain
objective = weighted geometric mean over scenarios, one legal ability allocation held fixed</pre>
  <h3>Shop rules</h3>
  <ul><li>Item slots of any category: 9, plus one per enemy Walker destroyed (assumed down by
    ${(M.walker_net_worth || []).map(x => commas(x)).join(' / ')} net worth, so ${Object.entries(M.slots_by_stage || {}).map(([k, v]) => k + ' ' + v).join(', ')}),
    max ${MAX_ACTIVES} actives, spend ≤ net worth. Purchase orders never hold more items than the slots open at that point.</li>
    <li>Ability points from the shipped level table (8 / 15 / 21 / 26 / 32); every maximum-spend tier allocation is tried.</li></ul>
  <h3>Search</h3>
  <p>${esc(M.optimization || '')}. Every published build is re-checked by <code>verify/check_outputs.py --deep</code>
  to be a one-item-exchange local optimum. The reference opponent is the median hero on its own solved build, iterated to a fixed point
  (drift per pass: ${(M.reference_drift || []).map(x => num(x * 100, 1) + '%').join(' → ')}).</p>
  <h3>Assumptions you should know</h3>
  <ul>
    <li>Each scenario is <b>one 20-second engagement entered with every cooldown ready</b>: actives, ultimates, barriers and
      buffs with longer cooldowns are used once per fight (Vampiric Burst 5 s of 20 s = 25% uptime, not 5 of 30 over a whole game).</li>
    <li>100% accuracy, 25% headshots, and conditional buffs with a duration but no cooldown at 75% uptime.</li>
    <li>Healing can offset at most 75% of incoming damage (burst, CC and target swaps interrupt real sustain).</li>
    <li>Isolation bonuses (Bloodscent) apply only when the target is isolated: always in picks, 25% of skirmishes, never in teamfights
      except while an isolating ultimate (Eternal Night) is up.</li>
    <li>Range-limited items (Point Blank, Stalker, Hunter's Aura, Torment Pulse, Scourge) count only for the share of the fight inside their radius.</li>
    <li>Item damage procs (Mystic Shot, Tesla Bullets, Toxic Bullets, Spirit Burn, Tankbuster, Mercurial Magnum, Torment Pulse, …) are modelled from their shipped values;
      melee-only procs are not.</li>
  </ul>
  <h3>Not modelled</h3>
  <p>Crowd control value, mobility, objectives, farming speed, vision, team composition, player skill and
  resource-gated abilities (Victor's Pain Battery, Wraith's Card Trick, Graves' Jar of Dead). Treat the
  cross-hero order as a combat ranking, not a universal tier list.</p>`;
}

/* ---------------- boot ---------------- */
async function boot() {
  D = await fetch('data.json?v=' + Date.now()).then(r => r.json());
  try { API = (await fetch('/api/health', { cache: 'no-store' })).ok; } catch (e) { API = false; }
  const M = (D.optimization && D.optimization.model) || {};
  MAX_SLOTS = M.max_slots || 12; MAX_ACTIVES = M.max_actives || 4;
  for (const [n, h] of Object.entries(D.heroes)) HERO_IDS[h.id] = n;
  $('#meta').textContent = `${D.meta.patch} · ${Object.keys(D.heroes).length} heroes · ${Object.keys(D.items).length} items · ` +
    `extracted ${D.meta.extracted} · ${API ? 'model server connected' : 'static mode (run scripts/serve.py for the Build Lab)'}`;
  const names = Object.keys(D.heroes).sort();
  for (const s of ['#heroSel', '#labHero']) $(s).innerHTML = names.map(n => `<option>${esc(n)}</option>`).join('');
  const tfTop = Object.entries(table('teamfight').overall).sort((a, b) => b[1] - a[1])[0][0];
  $('#heroSel').value = tfTop; $('#labHero').value = tfTop;
  const banner = $('#recalcNotice');
  if (banner && D.optimization.model) banner.textContent =
    `Recalculated ${new Date(D.generated || Date.now()).toISOString().slice(0, 10)} with 9→12 slot (Walker) shop rules and corrected item mechanics · ` +
    `teamfight #1: ${tfTop} · all-round #1: ${Object.entries(table('allround').overall).sort((a, b) => b[1] - a[1])[0][0]}`;
  const safe = (name, fn) => { try { fn(); } catch (e) {
    console.error(name + ' failed', e);
    const t = document.querySelector('#' + name + 'Body');
    if (t) t.innerHTML = '<p class="note">this section failed to render: ' + esc(e.message) + '</p>';
  } };
  safe('answer', renderAnswer); safe('pro', renderPro); safe('rank', renderRank); safe('build', renderBuilds);
  safe('hero', renderHero); safe('item', renderItems); safe('lab', renderLab); safe('method', renderMethod);
  bindTips();
  new MutationObserver(() => bindTips()).observe(document.querySelector('main'), { childList: true, subtree: true });
}
boot();

document.querySelectorAll('nav button').forEach(b => b.onclick = () => showTab(b.dataset.tab));
document.addEventListener('change', e => {
  if (e.target.matches('#rankStage,#rankObj')) renderRank();
  if (e.target.matches('#bStage,#bSort,#bObj')) renderBuilds();
  if (e.target.matches('#labHero,#labObj')) renderLab();
});
let labTimer = null;
document.addEventListener('input', e => {
  if (e.target.matches('#heroSel,#heroNW')) renderHero();
  if (e.target.matches('#itemSlot,#itemTier,#itemSearch')) renderItems();
  if (e.target.matches('#bFilter')) renderBuilds();
  if (e.target.matches('#labSearch')) labShop();
  if (e.target.matches('#labNW')) { clearTimeout(labTimer); labTimer = setTimeout(renderLab, 250); }
});
document.addEventListener('click', e => {
  const t = e.target.closest('[data-rm],[data-add],[data-open],[data-go],[data-lab],#labClear,#labOptimal,#labOpt');
  if (!t) return;
  if (t.dataset.rm !== undefined) { build.splice(+t.dataset.rm, 1); renderLab(); }
  else if (t.dataset.add) { build.push(t.dataset.add); renderLab(); }
  else if (t.dataset.open) openHero(t.dataset.open, t.dataset.stage || 'full', t.dataset.obj || 'teamfight');
  else if (t.dataset.go) showTab(t.dataset.go);
  else if (t.dataset.lab) {
    $('#labHero').value = t.dataset.lab; $('#labObj').value = t.dataset.obj;
    const st = STAGES.find(s => s[0] === t.dataset.stage);
    $('#labNW').value = st ? st[1] : 20000; labLoadSolved(); showTab('lab');
  }
  else if (t.id === 'labClear') { build = []; renderLab(); }
  else if (t.id === 'labOptimal') labLoadSolved();
  else if (t.id === 'labOpt') labOptimize();
});
