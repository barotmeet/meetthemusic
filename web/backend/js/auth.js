// ClassicalVerse — auth + submissions client helpers
(function () {
  let ACCOUNT_LINKS = null;

  function getAccountLinksContainer() {
    if (ACCOUNT_LINKS && document.contains(ACCOUNT_LINKS)) return ACCOUNT_LINKS;

    const existing = document.getElementById('account-links') || document.querySelector('.header-actions .nav-account');
    if (existing) {
      ACCOUNT_LINKS = existing;
      return ACCOUNT_LINKS;
    }

    const header = document.querySelector('.site-header');
    if (!header) return null;

    const actions = header.querySelector('.header-actions') || header.querySelector('.nav-wrap');
    if (!actions) return null;

    const created = document.createElement('div');
    created.className = 'nav-account';
    created.id = 'account-links';
    actions.appendChild(created);
    ACCOUNT_LINKS = created;
    return ACCOUNT_LINKS;
  }

  // ---- API helpers ---------------------------------------------------------
  async function api(path, opts = {}) {
    const init = { credentials: 'same-origin', ...opts };
    if (init.body && typeof init.body !== 'string' && !(init.body instanceof FormData)) {
      init.headers = { 'Content-Type': 'application/json', ...(init.headers || {}) };
      init.body = JSON.stringify(init.body);
    }
    const res = await fetch(path, init);
    const isJson = (res.headers.get('content-type') || '').includes('application/json');
    const body = isJson ? await res.json().catch(() => ({})) : await res.text();
    if (!res.ok) {
      const msg = (isJson && body && body.error) || res.statusText || 'Request failed';
      const err = new Error(msg);
      err.status = res.status;
      err.body = body;
      throw err;
    }
    return body;
  }

  // ---- Auth state ----------------------------------------------------------
  let _me = null;
  async function fetchMe() {
    try {
      const { user } = await api('/api/auth/me');
      _me = user || null;
    } catch {
      _me = null;
    }
    return _me;
  }

  function renderAccountLinks() {
    const linksEl = getAccountLinksContainer();
    if (!linksEl) return;

    // Hide / show the static "Start learning" CTA based on auth state
    const heroCta = document.getElementById('nav-start-learning');

    if (_me) {
      // Hide the generic CTA — user has personalised actions
      if (heroCta) heroCta.style.display = 'none';

      const isAdmin = _me.role === 'admin';
      linksEl.innerHTML = `
        <a class="user-pill" href="/profile" title="My profile">
          <span>${escapeHtml(_me.username)}</span>
          ${isAdmin ? '<span class="role">admin</span>' : ''}
        </a>
        ${isAdmin ? '<a class="btn-outline btn-small" href="/admin">Moderate</a>' : ''}
        <a class="btn-primary btn-small" href="/submit">Contribute</a>
        <button class="btn-outline btn-small" id="logout-btn">Logout</button>
      `;
      const out = document.getElementById('logout-btn');
      if (out) out.addEventListener('click', async () => {
        await api('/api/auth/logout', { method: 'POST' });
        location.href = '/';
      });
    } else {
      // Show start learning again (in case of re-render)
      if (heroCta) heroCta.style.display = '';

      linksEl.innerHTML = `
        <a class="auth-icon-btn" href="/login" title="Login" aria-label="Login">&#128274;</a>
        <a class="btn-primary btn-small" href="/signup">Sign up</a>
      `;
    }
  }

  function escapeHtml(s) {
    return String(s ?? '').replace(/[&<>"']/g, ch => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
    }[ch]));
  }

  // ---- Public surface ------------------------------------------------------
  window.cvAuth = { api, fetchMe, renderAccountLinks, get me() { return _me; } };

  // ---- Boot ----------------------------------------------------------------
  document.addEventListener('DOMContentLoaded', async () => {
    await fetchMe();
    renderAccountLinks();
  });
})();

// ---- Reusable form helpers (separate scope) -------------------------------
(function () {
  function $(sel, root = document) { return root.querySelector(sel); }
  function bindForm(formSel, onSubmit) {
    const form = typeof formSel === 'string' ? $(formSel) : formSel;
    if (!form) return;
    const errEl = form.querySelector('.form-error') || (() => {
      const e = document.createElement('p'); e.className = 'form-error';
      form.prepend(e); return e;
    })();
    const okEl = form.querySelector('.form-success') || (() => {
      const e = document.createElement('p'); e.className = 'form-success';
      form.prepend(e); return e;
    })();
    form.addEventListener('submit', async (ev) => {
      ev.preventDefault();
      errEl.textContent = '';
      okEl.textContent = '';
      try {
        await onSubmit(new FormData(form), { form, errEl, okEl });
      } catch (e) {
        errEl.textContent = e.message || 'Something went wrong.';
      }
    });
  }
  window.cvForm = { $, bindForm };
})();
