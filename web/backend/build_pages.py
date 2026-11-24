"""Generate all HTML pages for ClassicalVerse frontend."""
from pathlib import Path

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pages").mkdir(parents=True, exist_ok=True)

HEADER = """<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="/" aria-label="ClassicalVerse Home"><span class="brand-mark">ॐ</span><span>ClassicalVerse</span></a>
    <nav class="nav-links" role="navigation">
      <a href="/ragas">Ragas</a><a href="/bandishes">Bandishes</a>
      <a href="/taals">Taals</a><a href="/artists">Artists</a>
      <a href="/gurus">Gurus</a><a href="/concerts">Concerts</a>
      <a href="/knowledge">Knowledge</a>
      <a href="/learn">Learn</a><a href="/community">Community</a>
      <a href="/archive">Archive</a>
    </nav>
    <div class="header-actions">
      <button class="icon-btn" id="theme-toggle" aria-label="Toggle theme"></button>
      <a class="btn-primary" href="/learn">Start learning</a>
      <div class="nav-account" id="account-links"></div>
      <button class="icon-btn" id="mobile-toggle" aria-label="Menu">☰</button>
    </div>
  </div>
  <div class="mobile-menu">
    <div class="grid">
      <a href="/ragas">Ragas</a><a href="/bandishes">Bandishes</a>
      <a href="/taals">Taals</a><a href="/artists">Artists</a>
      <a href="/gurus">Gurus</a><a href="/concerts">Concerts</a>
      <a href="/learn">Learn</a><a href="/community">Community</a>
      <a href="/archive">Archive</a><a href="/knowledge">Knowledge</a>
    </div>
  </div>
</header>"""

FOOTER = """<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <div class="brand"><span class="brand-mark">ॐ</span><span>ClassicalVerse</span></div>
        <p class="muted" style="font-size:14px;max-width:280px">India's digital home for Hindustani and Carnatic music — for students, gurus, performers, and listeners.</p>
      </div>
      <div><h4>Explore</h4><ul><li><a href="/ragas">Ragas</a></li><li><a href="/bandishes">Bandishes</a></li><li><a href="/taals">Taals</a></li><li><a href="/artists">Artists</a></li></ul></div>
      <div><h4>Engage</h4><ul><li><a href="/gurus">Gurus</a></li><li><a href="/concerts">Concerts</a></li><li><a href="/learn">Learn</a></li><li><a href="/community">Community</a></li></ul></div>
      <div><h4>Library</h4><ul><li><a href="/archive">Archive</a></li><li><a href="/knowledge">Knowledge Graph</a></li></ul></div>
    </div>
    <div class="ornament">॥ संगीत सर्वोत्तमम् ॥</div>
    <p class="copyright">© 2026 ClassicalVerse · Preserving sound, sharing knowledge.</p>
  </div>
</footer>"""

def shell(title, desc, body, extra_script=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<link rel="stylesheet" href="/css/styles.css" />
<script>
  (function() {
    const theme = localStorage.getItem('theme') || 'light';
    if (theme === 'dark') document.documentElement.classList.add('dark');
  })();
</script>
</head>
<body>
{HEADER}
<main class="reveal">
{body}
</main>
{FOOTER}
<script src="/js/app.js"></script>
<script src="/js/auth.js"></script>
<script>{extra_script}</script>
</body>
</html>"""

# Landing page
landing_body = """<section class="hero">
  <div class="container">
    <p class="kicker" style="margin-bottom: 0.5rem">Preserving sound, sharing knowledge</p>
    <h1>Sound, <span class="accent">studied.</span></h1>
  <p>Explore ragas, bandishes, kritis, artists, gurus, concerts, archives and learning paths — across the Hindustani and Carnatic traditions, all in one premium scholarly home.</p>
  <div class="hero-actions">
    <a class="btn-primary" href="/ragas">Explore Ragaverse</a>
    <a class="btn-outline" href="/learn">Start a course</a>
  </div>
  <div class="ornament">॥ नाद ब्रह्म ॥</div>
  </div>
</section>
<section id="modules-landing" class="module-grid"></section>"""

(OUT / "index.html").write_text(shell(
    "ClassicalVerse — India's Digital Home for Classical Music",
    "Explore ragas, bandishes, kritis, artists, gurus, concerts, archives and learning paths across Hindustani and Carnatic traditions.",
    landing_body, "loadModulesGrid();"
))

# Module pages config: (slug, key, endpoint, kicker, title, lede)
MODULES = [
    ("ragas", "ragas", "/api/ragas", "Ragaverse", "The complete raga atlas",
     "Browse Hindustani and Carnatic ragas with notes, chalan, and reference recordings."),
    ("bandishes", "bandishes", "/api/bandishes", "Bandishverse", "Compositions across traditions",
     "Khayal bandishes, kritis, padams and more — with lyrics and translations."),
    ("taals", "taals", "/api/taals", "Taalverse", "Rhythm cycles, visualised",
     "Theka, vibhag, sam, and khali for Hindustani taals and Carnatic talas."),
    ("artists", "artists", "/api/artists", "Artistverse", "Maestros across generations",
     "Profiles, gharanas, recordings, and concerts of legendary and contemporary artists."),
    ("gurus", "gurus", "/api/gurus", "Guruverse", "Teachers and the gurukul tradition",
     "Discover gurus, learn their lineages, and request sessions online or in-person."),
    ("concerts", "concerts", "/api/concerts", "Concertverse", "Live and streamed performances",
     "Upcoming concerts, festivals, and livestreams across India and the world."),
    ("learn", "courses", "/api/courses", "Learnverse", "Structured learning paths",
     "From your first Sa to advanced khayal — courses guided by master teachers."),
    ("community", "community", "/api/community", "Communityverse", "Forums, threads, and people",
     "Discuss theory, practice, and interpretation with the global community."),
    ("archive", "archives", "/api/archives", "Archiveverse", "Preserving rare and historic works",
     "Recordings, manuscripts, interviews, and concerts curated for posterity."),
]

(OUT / "pages").mkdir(exist_ok=True)
for slug, key, endpoint, kicker, title, lede in MODULES:
    body = f"""<header class="page-header">
  <p class="kicker">{kicker}</p>
  <h1 class="page-title">{title}</h1>
  <p class="page-lede">{lede}</p>
</header>
<section class="section">
  <div id="module-grid" class="grid-cards"><p class="loading">Loading…</p></div>
</section>"""
    (OUT / "pages" / f"{slug}.html").write_text(shell(
        f"{title} — ClassicalVerse", lede, body,
        f"loadModule('{key}', '{endpoint}');"
    ))

# Knowledge page (static placeholder)
knowledge_body = """<header class="page-header">
  <p class="kicker">Knowledgeverse</p>
  <h1 class="page-title">The graph of how it all connects</h1>
  <p class="page-lede">A living map of ragas, taals, artists, gharanas, compositions, and concerts — coming soon as an interactive visualisation.</p>
</header>
<section class="section">
  <div class="card" style="text-align:center;padding:60px">
    <p class="serif" style="font-size:28px;color:var(--gold)">⊙ ⟶ ⊙ ⟶ ⊙</p>
    <p class="muted">Graph visualisation in development.</p>
  </div>
</section>"""
(OUT / "pages" / "knowledge.html").write_text(shell(
    "Knowledgeverse — ClassicalVerse",
    "The graph of how Indian classical music connects.",
    knowledge_body
))

# Raga detail
raga_body = """<article id="raga-detail"><p class="loading">Loading raga…</p></article>"""
(OUT / "pages" / "raga.html").write_text(shell(
    "Raga — ClassicalVerse",
    "Raga details — aroh, avroh, pakad, and bandishes.",
    raga_body, "loadRagaDetail();"
))

# --- Functional Pages (Auth, Submit, Profile, Admin) ---

login_body = """<section class="section">
  <div class="form-card">
    <h1>Login</h1>
    <p class="lede">Access your ClassicalVerse account.</p>
    <form id="login-form">
      <div class="form-row"><label>Username or Email</label><input type="text" name="username" required></div>
      <div class="form-row"><label>Password</label><input type="password" name="password" required></div>
      <button type="submit" class="btn-primary" style="width:100%">Login</button>
      <p class="muted" style="font-size:14px;margin-top:1rem">New here? <a href="/signup">Sign up</a></p>
    </form>
  </div>
</section>"""
(OUT / "login.html").write_text(shell("Login — ClassicalVerse", "Sign in to your account.", login_body, """
cvForm.bindForm('#login-form', async (data) => {
  await cvAuth.api('/api/auth/login', { method: 'POST', body: Object.fromEntries(data) });
  await cvAuth.fetchMe();
  location.href = '/profile';
});
"""))

signup_body = """<section class="section">
  <div class="form-card">
    <h1>Sign up</h1>
    <p class="lede">Join the community and start contributing.</p>
    <form id="signup-form">
      <div class="form-row"><label>Username</label><input type="text" name="username" required></div>
      <div class="form-row"><label>Email</label><input type="email" name="email" required></div>
      <div class="form-row"><label>Password (min 6 chars)</label><input type="password" name="password" minlength="6" required></div>
      <button type="submit" class="btn-primary" style="width:100%">Create Account</button>
    </form>
  </div>
</section>"""
(OUT / "signup.html").write_text(shell("Sign up — ClassicalVerse", "Join the community.", signup_body, """
cvForm.bindForm('#signup-form', async (data) => {
  await cvAuth.api('/api/auth/register', { method: 'POST', body: Object.fromEntries(data) });
  await cvAuth.fetchMe();
  location.href = '/profile';
});
"""))

submit_body = """<header class="page-header">
  <p class="kicker">Contribute</p>
  <h1 class="page-title">Share your knowledge</h1>
</header>
<section class="section">
  <div class="form-card" style="max-width:640px">
    <p class="lede">Your contribution will be reviewed by an admin before appearing in the public library.</p>
    <form id="submit-form">
      <div class="form-row"><label>Category</label>
        <select name="category" id="cat-select" required>
          <option value="raga">Raga</option><option value="taal">Taal</option><option value="knowledge">Knowledge Article</option>
        </select>
      </div>
      <div id="payload-fields"></div>
      <button type="submit" class="btn-primary" style="width:100%">Submit for review</button>
    </form>
  </div>
</section>"""
(OUT / "submit.html").write_text(shell("Contribute — ClassicalVerse", "Submit new content.", submit_body, """
(async () => {
  const me = cvAuth.me || await cvAuth.fetchMe();
  if (!me) { location.href = '/login?next=/submit'; }
})();

const fields = {
  raga: ['name', 'tradition', 'thaat', 'time', 'mood', 'aroh', 'avroh', 'description'],
  taal: ['name', 'tradition', 'beats', 'structure', 'claps', 'bols'],
  knowledge: ['title', 'body', 'tags']
};
const render = () => {
  const cat = document.getElementById('cat-select').value;
  document.getElementById('payload-fields').innerHTML = fields[cat].map(f => `
    <div class="form-row"><label>${f.charAt(0).toUpperCase()+f.slice(1)}</label>
    ${f==='description'||f==='body'||f==='bols' ? `<textarea name="${f}" required></textarea>` : `<input type="text" name="${f}" required>`}</div>
  `).join('');
};
document.getElementById('cat-select').onchange = render; render();
cvForm.bindForm('#submit-form', async (data) => {
  const body = { category: data.get('category'), payload: {} };
  fields[body.category].forEach(f => body.payload[f] = data.get(f));
  await cvAuth.api('/api/submissions', { method: 'POST', body });
  alert('Submitted! Waiting for admin approval.');
  location.href = '/profile';
});
"""))

profile_body = """<header class="page-header"><h1 id="prof-user" class="page-title">My Profile</h1></header>
<section class="section"><h3>My Submissions</h3><div id="sub-list" class="grid-cards"></div></section>"""
(OUT / "profile.html").write_text(shell("My Profile — ClassicalVerse", "Your submissions and status.", profile_body, """
async function load() {
  const me = cvAuth.me || await cvAuth.fetchMe();
  if (!me) { location.href = '/login?next=/profile'; return; }

  const { user, submissions } = await cvAuth.api('/api/profile');
  document.getElementById('prof-user').textContent = user.username;
  document.getElementById('sub-list').innerHTML = submissions.map(s => `
    <div class="card submission-card">
      <div class="status-pill status-${s.status}">${s.status}</div>
      <h4>${s.payload.name || s.payload.title}</h4>
      <p class="muted">${s.category} • Submitted ${new Date(s.created_at * 1000).toLocaleDateString()}</p>
      ${s.admin_note ? `<p style="font-size:13px;color:var(--gold)">Note: ${s.admin_note}</p>` : ''}
    </div>
  `).join('') || '<p>No submissions yet.</p>';
}
load();
"""))

admin_body = """<header class="page-header"><h1 class="page-title">Moderation Queue</h1></header>
<section class="section"><div id="admin-queue" class="grid-cards"></div></section>"""
(OUT / "admin.html").write_text(shell("Admin — ClassicalVerse", "Moderate submissions.", admin_body, """
(async () => {
  const me = cvAuth.me || await cvAuth.fetchMe();
  if (!me || me.role !== 'admin') { location.href = '/login?next=/admin'; }
})();

async function loadAdminQueue() {
  const queueEl = document.getElementById('admin-queue');
  if (!queueEl) return;

  try {
    const submissions = await cvAuth.api('/api/admin/submissions?status=pending');
    if (submissions.length === 0) {
      queueEl.innerHTML = '<p class="muted" style="text-align:center;padding:20px;">No pending submissions.</p>';
      return;
    }

    queueEl.innerHTML = submissions.map(s => `
      <div class="card submission-card" data-id="${s.id}">
        <div class="meta">
          <span class="status-pill status-${s.status}">${s.status}</span>
          <span class="muted">${s.category} by ${s.author.username}</span>
        </div>
        <h4>${s.payload.name || s.payload.title}</h4>
        <p class="payload">${s.payload.description || s.payload.body || s.payload.bols || 'No description provided.'}</p>
        <div class="form-actions" style="margin-top:16px;">
          <button class="btn-primary admin-action-btn" data-action="approve">Approve</button>
          <button class="btn-outline admin-action-btn" data-action="reject">Reject</button>
        </div>
        <div class="admin-note-input" style="display:none; margin-top:12px;">
          <textarea placeholder="Add a note (optional)" class="admin-note-textarea"></textarea>
        </div>
      </div>
    `).join('');

    queueEl.addEventListener('click', async (e) => {
      const btn = e.target.closest('.admin-action-btn');
      if (!btn) return;

      const submissionCard = btn.closest('.submission-card');
      const subId = submissionCard.dataset.id;
      const action = btn.dataset.action;
      let note = '';

      if (action === 'reject') {
        note = prompt('Enter a rejection note (optional):');
        if (note === null) return; // User cancelled
      }

      try {
        await cvAuth.api(`/api/admin/submissions/${subId}/${action}`, {
          method: 'POST',
          body: { note: note }
        });
        alert(`Submission ${subId} ${action}d!`);
        loadAdminQueue(); // Reload the queue
      } catch (error) {
        alert(`Error ${action}ing submission: ${error.message}`);
      }
    });
  } catch (e) {
    queueEl.innerHTML = '<p class="loading">Failed to load moderation queue. Make sure the backend is running and you are logged in as admin.</p>';
    console.error(e);
  }
}
loadAdminQueue();
"""))

print("Generated:", len(MODULES) + 8, "pages in", OUT)
