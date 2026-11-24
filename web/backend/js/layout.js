/**
 * ClassicalVerse — shared layout renderer.
 * Injects the site header and footer so individual pages stay DRY.
 */
(function () {
  const NAV_LINKS = [
    { href: '/ragas',     label: 'Ragas' },
    { href: '/bandishes', label: 'Bandishes' },
    { href: '/taals',     label: 'Taals' },
    { href: '/artists',   label: 'Artists' },
    { href: '/gurus',     label: 'Gurus' },
    { href: '/concerts',  label: 'Concerts' },
    { href: '/learn',     label: 'Learn' },
    { href: '/community', label: 'Community' },
    { href: '/archive',   label: 'Archive' },
    { href: '/knowledge', label: 'Knowledge' },
  ];

  function navLinksHtml(mobile) {
    return NAV_LINKS.map(n => `<a href="${n.href}">${n.label}</a>`).join('');
  }

  function buildHeader() {
    const path = location.pathname.replace(/\/$/, '');
    const navItems = NAV_LINKS.map(n => {
      const href = n.href.replace(/\/$/, '');
      const active = (path === href || path.startsWith(href + '/')) ? ' class="active"' : '';
      return `<a href="${n.href}"${active}>${n.label}</a>`;
    }).join('');

    const mobileItems = NAV_LINKS.map(n => `<a href="${n.href}">${n.label}</a>`).join('');

    return `
<header class="site-header">
  <div class="nav-wrap">
    <div class="container nav-wrap-top">
      <a class="brand" href="/">
        <span class="brand-mark" aria-hidden="true">&#2384;</span>
        <span class="brand-text"><span>ClassicalVerse</span><span class="brand-name-sub">Sangeet · Raga · Taal</span></span>
      </a>
      <div class="header-actions">
        <button class="icon-btn" id="theme-toggle" aria-label="Toggle colour theme"></button>
        <a class="btn-primary" href="/learn">Start learning</a>
        <div class="nav-account" id="account-links"></div>
        <button class="icon-btn" id="mobile-toggle" aria-label="Open menu"></button>
      </div>
    </div>
    <div class="nav-wrap-bottom">
      <div class="container">
        <nav class="nav-links" aria-label="Main navigation">${navItems}</nav>
      </div>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu">
    <div class="grid">${mobileItems}</div>
  </div>
</header>`;
  }

  function buildFooter() {
    return `
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/">
          <span class="brand-mark" aria-hidden="true">&#119070;</span>
          <span>ClassicalVerse</span>
        </a>
        <p class="footer-brand-desc">India&#8217;s digital home for Hindustani and Carnatic music &mdash; for students, gurus, performers, and listeners.</p>
      </div>
      <div><h4>Explore</h4><ul>
        <li><a href="/ragas">Ragas</a></li>
        <li><a href="/bandishes">Bandishes</a></li>
        <li><a href="/taals">Taals</a></li>
        <li><a href="/artists">Artists</a></li>
      </ul></div>
      <div><h4>Engage</h4><ul>
        <li><a href="/gurus">Gurus</a></li>
        <li><a href="/concerts">Concerts</a></li>
        <li><a href="/learn">Learn</a></li>
        <li><a href="/community">Community</a></li>
      </ul></div>
      <div><h4>Library</h4><ul>
        <li><a href="/archive">Archive</a></li>
        <li><a href="/knowledge">Knowledge Graph</a></li>
        <li><a href="/submit">Contribute</a></li>
      </ul></div>
    </div>
    <hr class="footer-divider" />
    <div class="ornament">&#2404; &#2360;&#2306;&#2327;&#2368;&#2340; &#2360;&#2352;&#2381;&#2357;&#2379;&#2340;&#2381;&#2340;&#2350;&#2350;&#2381; &#2404;</div>
    <p class="copyright">&copy; 2026 ClassicalVerse &middot; Preserving sound, sharing knowledge.</p>
  </div>
</footer>`;
  }

  function buildFab() {
    return `
<a class="fab-contribute" href="/submit" aria-label="Contribute to ClassicalVerse">
  <span class="fab-icon" aria-hidden="true">+</span>
  <span class="fab-label">Contribute</span>
</a>`;
  }

  // Inject into page
  document.addEventListener('DOMContentLoaded', function () {
    const headerPlaceholder = document.getElementById('cv-header');
    const footerPlaceholder = document.getElementById('cv-footer');
    const fabPlaceholder    = document.getElementById('cv-fab');
    if (headerPlaceholder) headerPlaceholder.outerHTML = buildHeader();
    if (footerPlaceholder) footerPlaceholder.outerHTML = buildFooter();
    if (fabPlaceholder)    fabPlaceholder.outerHTML    = buildFab();
  });

  window.cvLayout = { buildHeader, buildFooter };
})();
