// ClassicalVerse — shared client JS
const CV_IMG = window.CV_THEMES || {};

function cvEsc(s) {
  return String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function cvSlugHash(s) {
  let h = 0;
  const str = String(s ?? '');
  for (let i = 0; i < str.length; i += 1) {
    h = ((h << 5) - h + str.charCodeAt(i)) | 0;
  }
  return Math.abs(h);
}

function cvItemImage(module, item) {
  if (!item) return CV_IMG.heroFallback || '';
  if (item.image) return item.image;

  const slug = item.slug || '';
  const named = CV_IMG.named?.[module]?.[slug];
  if (named) return named;

  const pool = CV_IMG.imagePools?.[module] || CV_IMG.imagePools?.default || [];
  if (!pool.length) {
    return item.tradition === 'Carnatic'
      ? CV_IMG.ragaCarnatic
      : CV_IMG.ragaHindustani || CV_IMG.heroFallback || '';
  }
  const key = slug || item.name || item.title || '';
  return pool[cvSlugHash(key) % pool.length];
}

function cvCardMedia(url, alt, accent, label) {
  if (!url) return '';
  const displayLabel = label || alt;
  return `
    <div class="card-media${accent ? ` card-media--${accent}` : ''}">
      <img src="${url}" alt="${cvEsc(alt)}" loading="lazy" decoding="async" />
      <span class="card-media-label serif">${cvEsc(displayLabel)}</span>
      <div class="card-media-shine"></div>
    </div>`;
}

function cvRagaImg(r) {
  return cvItemImage('ragas', r);
}

(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem('cv-theme');
  const prefers = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = saved || (prefers ? 'dark' : 'light');
  root.classList.toggle('dark', theme === 'dark');
  root.classList.toggle('light', theme === 'light');

  document.addEventListener('click', (e) => {
    if (e.target.closest('#theme-toggle')) {
      const next = root.classList.contains('dark') ? 'light' : 'dark';
      root.classList.toggle('dark', next === 'dark');
      root.classList.toggle('light', next === 'light');
      localStorage.setItem('cv-theme', next);
    }
    if (e.target.closest('#mobile-toggle')) {
      document.querySelector('.mobile-menu')?.classList.toggle('open');
    }
  });

  // Mark active nav
  const path = location.pathname.replace(/\/$/, '');
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
    const href = a.getAttribute('href').replace(/\/$/, '');
    if (href && href !== '/' && (path === href || path.startsWith(href + '/'))) {
      a.classList.add('active');
    }
  });
})();

async function api(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`API ${path} failed: ${res.status}`);
  return res.json();
}

function el(html) {
  const d = document.createElement('div');
  d.innerHTML = html.trim();
  return d.firstElementChild;
}

// ---- Renderers per module ----
const renderers = {
  ragas: (list) => list.map(r => `
    <a class="card card--lift" href="/raga?slug=${r.slug}">
      ${cvCardMedia(cvRagaImg(r), r.name, r.tradition === 'Carnatic' ? 'carnatic' : 'hindustani', r.name)}
      <div class="card-body">
        <div><span class="pill gold">${r.tradition}</span><span class="pill">${r.thaat}</span></div>
        <h3>${r.name}</h3>
        <p>${r.description}</p>
        <p class="muted card-meta"><strong>Time:</strong> ${r.time} · <strong>Mood:</strong> ${r.mood}</p>
      </div>
    </a>`).join(''),
  bandishes: (list) => list.map(b => `
    <a class="card card--lift" href="/bandish?slug=${b.slug}">
      ${cvCardMedia(cvItemImage('bandishes', b), b.title, '', b.title)}
      <div class="card-body">
        <span class="pill gold">${b.difficulty}</span><span class="pill">${b.language}</span>
        <h3>${b.title}</h3>
        <p><strong>Raga:</strong> ${b.raga} · <strong>Taal:</strong> ${b.taal}</p>
        <p class="card-lyric">"${b.lyrics}"</p>
        <p class="muted">${b.translation}</p>
        <p class="muted">— ${b.composer}</p>
      </div>
    </a>`).join(''),
  taals: (list) => list.map(t => `
    <a class="card card--lift" href="/taal?slug=${t.slug}">
      ${cvCardMedia(cvItemImage('taals', t), t.name, 'taal', t.name)}
      <div class="card-body">
        <span class="pill gold">${t.tradition}</span><span class="pill">${t.beats} beats</span>
        <h3>${t.name}</h3>
        <p><strong>Structure:</strong> ${t.structure}</p>
        <p><strong>Claps:</strong> ${t.claps}</p>
        ${t.context ? `<p class="muted" style="font-size:13px">${t.context}</p>` : ''}
        <p class="card-bols">${t.bols}</p>
      </div>
    </a>`).join(''),
  artists: (list) => list.map(a => `
    <a class="card card--lift" href="/artist?slug=${a.slug}">
      ${cvCardMedia(cvItemImage('artists', a), a.name, '', a.name)}
      <div class="card-body">
        <span class="pill">${a.era}</span>${a.gharana !== '—' ? `<span class="pill gold">${a.gharana}</span>` : ''}
        <h3>${a.name}</h3>
        <p class="muted">${a.instruments.join(', ')}</p>
        <p>${a.bio}</p>
      </div>
    </a>`).join(''),
  gurus: (list) => list.map(g => `
    <a class="card card--lift" href="/guru?slug=${g.slug}">
      ${cvCardMedia(cvItemImage('gurus', g), g.name, '', g.name)}
      <div class="card-body">
        <span class="pill gold">★ ${g.rating}</span><span class="pill">${g.students} students</span>
        <h3>${g.name}</h3>
        <p><strong>${g.specialty}</strong></p>
        <p class="muted">${g.experience} · ${g.mode}</p>
        <p>${g.bio}</p>
        <span class="btn-outline card-cta">Request session</span>
      </div>
    </a>`).join(''),
  concerts: (list) => list.map(c => `
    <a class="card card--lift" href="/concert?slug=${c.slug}">
      ${cvCardMedia(cvItemImage('concerts', c), c.title, '', c.title)}
      <div class="card-body">
        <span class="pill gold">${c.type}</span>${c.livestream ? '<span class="pill">Livestream</span>' : ''}
        <h3>${c.title}</h3>
        <p><strong>${c.date}</strong> · ${c.city}</p>
        <p class="muted">${c.venue}</p>
        <p>${c.artist}</p>
      </div>
    </a>`).join(''),
  courses: (list) => list.map(c => `
    <a class="card card--lift" href="/course?slug=${c.slug}">
      ${cvCardMedia(cvItemImage('courses', c), c.title, '', c.title)}
      <div class="card-body">
        <span class="pill gold">${c.level}</span><span class="pill">${c.lessons} lessons</span>
        <h3>${c.title}</h3>
        <p class="muted">${c.duration}</p>
        <p>${c.description}</p>
        <span class="btn-primary card-cta">Enroll</span>
      </div>
    </a>`).join(''),
  community: (list) => list.map(t => `
    <a class="card card--lift" href="/thread?slug=${t.slug}">
      ${cvCardMedia(cvItemImage('community', t), t.title, '', t.title)}
      <div class="card-body">
        <span class="pill gold">${t.tag}</span>
        <h3>${t.title}</h3>
        <p class="muted">by ${t.author} · ${t.replies} replies</p>
      </div>
    </a>`).join(''),
  archives: (list) => list.map(a => `
    <a class="card card--lift" href="/archive?slug=${a.slug}">
      ${cvCardMedia(cvItemImage('archives', a), a.title, '', a.title)}
      <div class="card-body">
        <span class="pill gold">${a.type}</span><span class="pill">${a.year}</span>
        <h3>${a.title}</h3>
        <p>${a.description}</p>
      </div>
    </a>`).join(''),
};

async function loadModule(key, endpoint) {
  const target = document.getElementById('module-grid');
  if (!target) return;
  try {
    const data = await api(endpoint);
    target.innerHTML = renderers[key](data);
    window.CVUI?.observeReveals?.();
  } catch (e) {
    target.innerHTML = `<p class="loading">Failed to load. Make sure the backend is running.</p>`;
    console.error('Failed to load module:', e);
  }
}

async function loadRagaDetail() {
  const slug = new URLSearchParams(location.search).get('slug');
  const target = document.getElementById('raga-detail');
  if (!target || !slug) return;
  try {
    const { raga, bandishes } = await api(`/api/ragas/${slug}`);
    document.title = `${raga.name} — ClassicalVerse`;

    // Use stored links if present, otherwise generate search links
    const ytUrl  = raga.youtube || `https://www.youtube.com/results?search_query=${encodeURIComponent(raga.name + ' raga')}`;
    const spUrl  = raga.spotify || `https://open.spotify.com/search/${encodeURIComponent(raga.name)}`;
    const yt = `<a class="btn-link youtube" href="${ytUrl}" target="_blank" rel="noopener">▶ YouTube</a>`;
    const sp = `<a class="btn-link spotify" href="${spUrl}" target="_blank" rel="noopener">♫ Spotify</a>`;
    const links = `<div class="detail-links">${yt}${sp}</div>`;

    target.innerHTML = `
      <div class="page-header">
        <a href="/ragas" class="muted" style="font-size:14px">← Ragaverse</a>
        <div style="margin-top:16px"><span class="pill gold">${raga.tradition}</span><span class="pill">${raga.thaat}</span></div>
        <h1 class="page-title">${raga.name}</h1>
        <p class="page-lede">${raga.description}</p>
        <div class="row" style="margin-top:16px">
          <span><strong>Time:</strong> ${raga.time}</span>
          <span><strong>Mood:</strong> ${raga.mood}</span>
          <span><strong>Vadi:</strong> ${raga.vadi}</span>
          <span><strong>Samvadi:</strong> ${raga.samvadi}</span>
        </div>
        ${links}
      </div>
      <div class="section">
        <div class="note-grid">
          <div class="note-card"><div class="lbl">Aroh</div><div class="val">${raga.aroh}</div></div>
          <div class="note-card"><div class="lbl">Avroh</div><div class="val">${raga.avroh}</div></div>
          <div class="note-card"><div class="lbl">Pakad</div><div class="val">${raga.pakad}</div></div>
        </div>
        <div class="card" style="margin-top:24px">
          <h2 class="serif" style="margin:0 0 12px;font-size:28px;font-weight:500">Listen</h2>
          <div class="player">
            <button class="play-btn">▶</button>
            <div style="flex:1">
              <p style="margin:0;font-weight:500">${raga.name} — Alap & Bandish</p>
              <p class="muted" style="margin:2px 0 0;font-size:12px">Reference recording · 7:42</p>
              <div class="progress"><div></div></div>
            </div>
          </div>
        </div>
        ${bandishes.length ? `
        <h2 class="serif" style="margin:32px 0 12px;font-size:28px;font-weight:500">Bandishes in ${raga.name}</h2>
        <div class="grid-2">
          ${bandishes.map(b => `<div class="card"><h3>${b.title}</h3><p class="muted">${b.composer} · ${b.taal} · ${b.difficulty}</p></div>`).join('')}
        </div>` : ''}
      </div>
    `;
  } catch (e) {
    console.error('Failed to load raga detail:', e);
    target.innerHTML = `<p class="loading">Raga not found.</p>`;
  }
}

async function loadModulesGrid() {
  const target = document.getElementById('modules-landing');
  if (!target) return;
  try {
    const modules = await api('/api/modules');
    const imgs = CV_IMG.modules || {};
    target.innerHTML = modules.map((m, i) => `
      <a class="module-card" href="/${m.slug}">
        <div class="module-card-visual" style="background-image:url('${imgs[m.slug] || CV_IMG.heroFallback || ''}')">
          <span class="module-card-num">${String(i + 1).padStart(2, '0')}</span>
        </div>
        <div class="module-card-content">
          <div class="title">${m.title}</div>
          <div class="tag">${m.tagline}</div>
          <div class="count">${m.count} ${m.suffix}</div>
          <span class="arrow" aria-hidden="true">&rarr;</span>
        </div>
      </a>`).join('');
    window.CVUI?.observeReveals?.();
  } catch (e) {
    console.error('Failed to load modules:', e);
  }
}

// ---- Detail page (used by all module detail pages via /detail?type=...&slug=...) ----
function detailPage({ kicker, back, title, lede, fields = [], pills = [], bodyHtml, youtube, spotify, relatedTitle, relatedHtml }) {
  const pillsHtml = pills.map(([cls, txt]) => `<span class="pill ${cls || ''}">${txt}</span>`).join('');
  const fieldsHtml = fields.length
    ? `<div class="row" style="margin-top:16px;flex-wrap:wrap;gap:14px">${fields.map(([k, v]) => `<span><strong>${k}:</strong> ${v}</span>`).join('')}</div>`
    : '';
  const yt = youtube ? `<a class="btn-link youtube" href="${youtube}" target="_blank" rel="noopener">▶ YouTube</a>` : '';
  const sp = spotify ? `<a class="btn-link spotify" href="${spotify}" target="_blank" rel="noopener">♫ Spotify</a>` : '';
  const links = (yt || sp) ? `<div class="detail-links">${yt}${sp}</div>` : '';
  const related = relatedHtml ? `
    <h2 class="serif" style="margin:32px 0 12px;font-size:28px;font-weight:500">${relatedTitle || 'Related'}</h2>
    <div class="grid-2">${relatedHtml}</div>` : '';
  return `
    <div class="page-header">
      <a href="${back.href}" class="muted" style="font-size:14px">← ${back.label}</a>
      ${kicker ? `<p class="kicker" style="margin-top:16px">${kicker}</p>` : ''}
      ${pillsHtml ? `<div style="margin-top:16px">${pillsHtml}</div>` : ''}
      <h1 class="page-title">${title}</h1>
      ${lede ? `<p class="page-lede">${lede}</p>` : ''}
      ${fieldsHtml}
    </div>
    <div class="section">
      ${bodyHtml || ''}
      ${links}
      ${related}
    </div>
  `;
}

async function loadDetail() {
  const target = document.getElementById('detail-root');
  if (!target) return;
  const params = new URLSearchParams(location.search);
  const type = params.get('type');
  const slug = params.get('slug');
  if (!type || !slug) { target.innerHTML = `<p class="loading">Missing item.</p>`; return; }
  try {
    const data = await api(`/api/${type}/${slug}`);
    const html = renderDetail(type, data);
    document.title = (data && (data[Object.keys(data)[0]]?.title || data[Object.keys(data)[0]]?.name) || 'Detail') + ' — ClassicalVerse';
    target.innerHTML = html;
  } catch (e) {
    target.innerHTML = `<p class="loading">Not found.</p>`;
    console.error(e);
  }
}

function renderDetail(type, payload) {
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  if (type === 'bandishes') {
    const b = payload.bandish, r = payload.raga;
    return detailPage({
      kicker: 'Bandishverse',
      back: { href: '/bandishes', label: 'Bandishverse' },
      title: b.title,
      lede: `In raga ${b.raga}, set to ${b.taal}`,
      pills: [['gold', b.difficulty], ['', b.language]],
      fields: [['Raga', b.raga], ['Taal', b.taal], ['Composer', b.composer], ['Language', b.language]],
      bodyHtml: `
        <div class="card">
          <h2 class="serif" style="margin:0 0 12px;font-size:24px;font-weight:500">Lyrics</h2>
          <p style="font-style:italic;font-family:'Cormorant Garamond',serif;font-size:22px;line-height:1.6">"${esc(b.lyrics)}"</p>
          <p class="muted" style="margin-top:8px">${esc(b.translation)}</p>
        </div>`,
      youtube: b.youtube, spotify: b.spotify,
      relatedTitle: r ? `About the raga` : '',
      relatedHtml: r ? `<a class="card" href="/raga?slug=${esc(r.slug)}"><h3>${esc(r.name)}</h3><p class="muted">${esc(r.tradition)} · ${esc(r.thaat)} · ${esc(r.time)}</p></a>` : '',
    });
  }
  if (type === 'taals') {
    const t = payload.taal, related = payload.bandishes || [];
    return detailPage({
      kicker: 'Taalverse',
      back: { href: '/taals', label: 'Taalverse' },
      title: t.name,
      lede: `${t.tradition} rhythm cycle · ${t.beats} beats`,
      pills: [['gold', t.tradition], ['', `${t.beats} beats`]],
      fields: [
        ['Structure', t.structure],
        ['Clap pattern', t.claps],
        ['Beats', t.beats],
        ...(t.context ? [['Context', t.context]] : []),
      ],
      bodyHtml: `
        <div class="card">
          <h2 class="serif" style="margin:0 0 12px;font-size:24px;font-weight:500">Theka / Bols</h2>
          <p style="font-family:'Cormorant Garamond',serif;font-size:22px;letter-spacing:.05em;line-height:1.7">${esc(t.bols)}</p>
        </div>`,
      youtube: t.youtube, spotify: t.spotify,
      relatedTitle: related.length ? `Bandishes in ${t.name}` : '',
      relatedHtml: related.map(b => `<a class="card" href="/bandish?slug=${esc(b.slug)}"><h3>${esc(b.title)}</h3><p class="muted">${esc(b.raga)} · ${esc(b.composer)}</p></a>`).join(''),
    });
  }
  if (type === 'artists') {
    const a = payload.artist;
    return detailPage({
      kicker: 'Artistverse',
      back: { href: '/artists', label: 'Artistverse' },
      title: a.name,
      lede: a.bio,
      pills: [['', a.era], ...(a.gharana && a.gharana !== '—' ? [['gold', a.gharana]] : [])],
      fields: [['Era', a.era], ['Gharana', a.gharana], ['Instruments', (a.instruments || []).join(', ')]],
      youtube: a.youtube, spotify: a.spotify,
    });
  }
  if (type === 'gurus') {
    const g = payload.guru;
    return detailPage({
      kicker: 'Guruverse',
      back: { href: '/gurus', label: 'Guruverse' },
      title: g.name,
      lede: g.bio,
      pills: [['gold', `★ ${g.rating}`], ['', `${g.students} students`]],
      fields: [['Specialty', g.specialty], ['Experience', g.experience], ['Mode', g.mode]],
      bodyHtml: `<div class="form-actions" style="margin-top:8px"><button class="btn-primary">Request session</button></div>`,
      youtube: g.youtube, spotify: g.spotify,
    });
  }
  if (type === 'concerts') {
    const c = payload.concert;
    return detailPage({
      kicker: 'Concertverse',
      back: { href: '/concerts', label: 'Concertverse' },
      title: c.title,
      lede: `${c.artist} · ${c.venue}`,
      pills: [['gold', c.type], ...(c.livestream ? [['', 'Livestream']] : [])],
      fields: [['Date', c.date], ['City', c.city], ['Venue', c.venue], ['Artist', c.artist]],
      youtube: c.youtube, spotify: c.spotify,
    });
  }
  if (type === 'courses') {
    const c = payload.course;
    return detailPage({
      kicker: 'Learnverse',
      back: { href: '/learn', label: 'Learnverse' },
      title: c.title,
      lede: c.description,
      pills: [['gold', c.level], ['', `${c.lessons} lessons`]],
      fields: [['Duration', c.duration], ['Lessons', c.lessons], ['Level', c.level]],
      bodyHtml: `<div class="form-actions" style="margin-top:8px"><button class="btn-primary">Enroll</button></div>`,
      youtube: c.youtube, spotify: c.spotify,
    });
  }
  if (type === 'community') {
    const t = payload.thread;
    return detailPage({
      kicker: 'Communityverse',
      back: { href: '/community', label: 'Communityverse' },
      title: t.title,
      lede: `Started by ${t.author} · ${t.replies} replies`,
      pills: [['gold', t.tag]],
      bodyHtml: `<div class="card"><p style="font-size:16px;line-height:1.7">${esc(t.body || 'Discussion thread. Sign in to join the conversation.')}</p></div>`,
      youtube: t.youtube, spotify: t.spotify,
    });
  }
  if (type === 'archives') {
    const a = payload.archive;
    return detailPage({
      kicker: 'Archiveverse',
      back: { href: '/archive', label: 'Archiveverse' },
      title: a.title,
      lede: a.description,
      pills: [['gold', a.type], ['', String(a.year)]],
      fields: [['Type', a.type], ['Year', a.year]],
      youtube: a.youtube, spotify: a.spotify,
    });
  }
  return `<p class="loading">Unknown detail type.</p>`;
}
