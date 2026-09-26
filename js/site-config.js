/**
 * LicitaFit site config (one place for analytics + form destination).
 *
 * Analytics: set provider + id, then scripts load only when configured.
 *   provider: 'none' | 'ga4' | 'plausible'
 *   id: GA4 measurement ID (G-XXXXXXXX) OR Plausible data-domain (e.g. licitafit.com.br)
 *
 * Form: FormSubmit posts to LF_FORM.email (no API key). First live submit
 * sends an activation link to that inbox; click it once. See
 * docs/analytics-e-formulario.md
 */
(function (global) {
  'use strict';
  global.LF_ANALYTICS = {
    provider: 'none',
    id: ''
    // Examples after you create an account:
    // provider: 'ga4', id: 'G-XXXXXXXX'
    // provider: 'plausible', id: 'licitafit.com.br'
  };
  global.LF_FORM = {
    provider: 'formsubmit',
    email: 'raphael@launchbase.dev',
    endpoint: 'https://formsubmit.co/raphael@launchbase.dev'
  };
})(typeof window !== 'undefined' ? window : this);
