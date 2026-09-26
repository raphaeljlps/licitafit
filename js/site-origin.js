/**
 * CruzaEdital , canonical site origin (one place to swap).
 *
 * Intended production host. DNS may not resolve yet.
 * Interim visibility: https://raphaeljlps.github.io/licitafit/ (GitHub Pages from main).
 * Legacy preview (STALE, do not use for demos): https://dapper-opera-mz8m.here.now/
 * Do not change SITE_ORIGIN to the Pages URL , keep www.licitafit.com.br for SEO.
 *
 * Absolute URLs in sitemap.xml, robots.txt, <link rel="canonical"> and
 * JSON-LD should match this value. After DNS is live, keep this file and
 * those static URLs in sync (search-replace SITE_ORIGIN string).
 *
 * SITE_ORIGIN=https://www.licitafit.com.br
 */
(function (global) {
  'use strict';
  var SITE_ORIGIN = 'https://www.licitafit.com.br';
  global.LICITAFIT_SITE_ORIGIN = SITE_ORIGIN;
  global.CruzaEditalSite = global.LicitaFitSite = {
    origin: SITE_ORIGIN,
    pagesOrigin: 'https://raphaeljlps.github.io/licitafit',
    // Legacy only; does not auto-deploy from main.
    legacyPreviewOrigin: 'https://dapper-opera-mz8m.here.now'
  };
})(typeof window !== 'undefined' ? window : this);
