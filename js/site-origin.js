/**
 * LicitaFit , canonical site origin (one place to swap).
 *
 * Intended production host. DNS may not resolve yet; preview remains at
 * https://dapper-opera-mz8m.here.now/ (STALE , does not auto-deploy).
 * Interim visibility: https://raphaeljlps.github.io/licitafit/ (GitHub Pages from main).
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
  global.LicitaFitSite = {
    origin: SITE_ORIGIN,
    previewOrigin: 'https://dapper-opera-mz8m.here.now',
    pagesOrigin: 'https://raphaeljlps.github.io/licitafit'
  };
})(typeof window !== 'undefined' ? window : this);
