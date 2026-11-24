/** ClassicalVerse — motion, page heroes, scroll polish */
(function () {
  const T = window.CV_THEMES || {};

  function pageSlug() {
    const p = location.pathname.replace(/\/$/, '');
    if (!p || p === '/') return 'home';
    const parts = p.split('/').filter(Boolean);
    return parts[parts.length - 1].replace('.html', '');
  }

  function enhancePageHero() {
    const header = document.querySelector('main .page-header, main > header.page-header');
    if (!header || header.closest('.page-hero-wrap')) return;

    const slug = pageSlug();
    const banners = T.pageBanners || {};
    const img = banners[slug] || banners.default || T.heroFallback;

    const wrap = document.createElement('div');
    wrap.className = 'page-hero-wrap reveal';

    const bg = document.createElement('div');
    bg.className = 'page-hero-bg';
    bg.style.backgroundImage = `url('${img}')`;
    wrap.appendChild(bg);

    const veil = document.createElement('div');
    veil.className = 'page-hero-veil';
    wrap.appendChild(veil);

    const pattern = document.createElement('div');
    pattern.className = 'page-hero-pattern';
    wrap.appendChild(pattern);

    header.parentNode.insertBefore(wrap, header);
    wrap.appendChild(header);
  }

  function injectScrollProgress() {
    if (document.querySelector('.scroll-progress')) return;
    const bar = document.createElement('div');
    bar.className = 'scroll-progress';
    bar.innerHTML = '<div class="scroll-progress-bar"></div>';
    document.body.appendChild(bar);
    const inner = bar.firstElementChild;
    window.addEventListener(
      'scroll',
      () => {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        const pct = max > 0 ? (window.scrollY / max) * 100 : 0;
        inner.style.width = `${pct}%`;
      },
      { passive: true }
    );
  }

  function headerOnScroll() {
    const header = document.querySelector('.site-header');
    if (!header) return;
    const toggle = () => header.classList.toggle('is-scrolled', window.scrollY > 24);
    toggle();
    window.addEventListener('scroll', toggle, { passive: true });
  }

  function observeReveals() {
    const nodes = document.querySelectorAll(
      '.reveal, .card, .module-card, .sample-card, .stat-item, .instrument-card, .form-card'
    );
    nodes.forEach((el, i) => {
      el.classList.add('cv-animate');
      el.style.setProperty('--cv-delay', `${Math.min(i % 12, 11) * 0.05}s`);
    });

    if (!('IntersectionObserver' in window)) {
      nodes.forEach((el) => el.classList.add('cv-visible'));
      return;
    }

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('cv-visible');
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    nodes.forEach((el) => io.observe(el));
  }

  function animateStats() {
    document.querySelectorAll('.stat-num').forEach((el) => {
      const target = parseInt(el.textContent, 10);
      if (!target || el.dataset.animated) return;
      el.dataset.animated = '1';
      const duration = 1200;
      const start = performance.now();
      const step = (now) => {
        const t = Math.min(1, (now - start) / duration);
        const ease = 1 - Math.pow(1 - t, 3);
        el.textContent = Math.round(target * ease);
        if (t < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  }

  function buildInstrumentsSection() {
    const mount = document.getElementById('instruments-mount');
    if (!mount || !T.instruments) return;
    mount.innerHTML = `
      <section class="instruments-section reveal" aria-label="Instruments of the tradition">
        <div class="instruments-inner">
          <div class="instruments-head">
            <p class="kicker">&#9835; Instruments &amp; voices</p>
            <h2 class="serif instruments-title">The living soundscape</h2>
            <p class="instruments-lede">From the resonance of sitar strings to the pulse of tabla — explore the instruments that shape every raga and taal.</p>
          </div>
          <div class="instruments-grid">
            ${T.instruments
              .map(
                (item) => `
              <a class="instrument-card" href="${item.href}">
                <div class="instrument-img" style="background-image:url('${item.img}')"></div>
                <div class="instrument-body">
                  <span class="instrument-tradition">${item.tradition}</span>
                  <h3>${item.name}</h3>
                  <span class="instrument-link">Explore &rarr;</span>
                </div>
              </a>`
              )
              .join('')}
          </div>
        </div>
      </section>`;
  }

  function buildCollageMosaic() {
    const strip = document.querySelector('.collage-strip');
    if (!strip || strip.querySelector('.collage-mosaic')) return;
    const imgs = T.collage || [];
    if (!imgs.length) return;

    const mosaic = document.createElement('div');
    mosaic.className = 'collage-mosaic';
    mosaic.innerHTML = imgs
      .slice(0, 6)
      .map((src) => `<div class="collage-tile" style="background-image:url('${src}')"></div>`)
      .join('');
    strip.insertBefore(mosaic, strip.firstChild);
  }

  function smoothAnchors() {
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener('click', (e) => {
        const id = a.getAttribute('href').slice(1);
        const target = document.getElementById(id);
        if (!target) return;
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  /** Inject a mandala "Discover more" CTA below the module grid on listing pages */
  function injectDiscoverCta() {
    const slug = pageSlug();
    const listingSlugs = ['ragas','bandishes','taals','artists','gurus','concerts','learn','community','archive','knowledge'];
    if (!listingSlugs.includes(slug)) return;
    const grid = document.getElementById('module-grid') || document.getElementById('knowledge-articles');
    if (!grid) return;

    // Avoid double-injection
    if (document.querySelector('.discover-cta-wrap')) return;

    // Wait until grid is populated
    const observer = new MutationObserver(() => {
      if (grid.children.length && !grid.querySelector('.loading')) {
        observer.disconnect();
        const wrap = document.createElement('div');
        wrap.className = 'discover-cta-wrap';
        wrap.innerHTML = `
          <a class="discover-cta-btn" href="/">
            <span class="cta-icon" aria-hidden="true">&#9836;</span>
            <span class="cta-label">Discover<br>more</span>
          </a>`;
        grid.parentNode.insertBefore(wrap, grid.nextSibling);
      }
    });
    observer.observe(grid, { childList: true, subtree: false });
  }

  function init() {
    if (pageSlug() !== 'home') enhancePageHero();
    injectScrollProgress();
    headerOnScroll();
    buildInstrumentsSection();
    buildCollageMosaic();
    smoothAnchors();
    injectDiscoverCta();
    observeReveals();
    setTimeout(animateStats, 400);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.CVUI = { init, observeReveals };
})();
