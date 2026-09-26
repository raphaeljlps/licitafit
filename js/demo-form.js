/**
 * Demo request form helpers: set FormSubmit action/_next from config and
 * show a simple PT-BR status if the browser blocks the POST.
 */
(function () {
  'use strict';
  function obrigadoUrl(form) {
    var rel = form.getAttribute('data-lf-obrigado') || 'obrigado/';
    try {
      return new URL(rel, window.location.href).href;
    } catch (e) {
      return rel;
    }
  }

  function wire(form) {
    var cfg = window.LF_FORM || {};
    var endpoint = cfg.endpoint || 'https://formsubmit.co/raphael@launchbase.dev';
    form.setAttribute('action', endpoint);
    form.setAttribute('method', 'POST');

    var next = form.querySelector('input[name="_next"]');
    if (next) {
      next.value = obrigadoUrl(form);
    }

    form.addEventListener('submit', function () {
      var status = form.querySelector('[data-lf-form-status]');
      if (status) {
        status.hidden = false;
        status.textContent = 'Enviando seu pedido...';
      }
      var btn = form.querySelector('[type="submit"]');
      if (btn) {
        btn.disabled = true;
      }
    });
  }

  function init() {
    var forms = document.querySelectorAll('form[data-lf-demo-form]');
    for (var i = 0; i < forms.length; i++) {
      wire(forms[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
