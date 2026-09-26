/**
 * Lightweight analytics loader. No-op until LF_ANALYTICS.provider + id are set
 * in js/site-config.js (see docs/analytics-e-formulario.md).
 */
(function () {
  'use strict';
  var cfg = typeof window !== 'undefined' ? window.LF_ANALYTICS : null;
  if (!cfg || !cfg.provider || cfg.provider === 'none' || !cfg.id) {
    return;
  }

  if (cfg.provider === 'ga4') {
    var gaId = String(cfg.id).trim();
    if (!/^G-[A-Z0-9]+$/i.test(gaId)) {
      return;
    }
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId);
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', gaId, { anonymize_ip: true });
    return;
  }

  if (cfg.provider === 'plausible') {
    var domain = String(cfg.id).trim();
    if (!domain) {
      return;
    }
    var p = document.createElement('script');
    p.defer = true;
    p.setAttribute('data-domain', domain);
    p.src = 'https://plausible.io/js/script.js';
    document.head.appendChild(p);
  }
})();
