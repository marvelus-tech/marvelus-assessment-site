/* MarvelUs site behaviour. Vanilla JS, no dependencies, nothing stored, nothing sent. */
(function () {
  "use strict";
  var scriptEl = document.querySelector('script[src*="assets/js/main.js"]');
  var root = scriptEl ? scriptEl.src.replace(/assets\/js\/main\.js.*$/, "") : "/";
  window.MV = {
    root: root,
    url: function (path) { return root + String(path || "").replace(/^\//, ""); },
    reduceMotion: function () { return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches; }
  };

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Chip filters (case studies, insights)
  document.querySelectorAll("[data-filter]").forEach(function (chip) {
    chip.addEventListener("click", function () {
      var group = chip.closest(".chips");
      var tag = chip.getAttribute("data-filter");
      group.querySelectorAll("[data-filter]").forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
      var scope = group.parentElement;
      var items = scope.querySelectorAll("[data-tags]");
      var shown = 0;
      items.forEach(function (it) {
        var tags = (it.getAttribute("data-tags") || "").split(/\s+/);
        var show = tag === "all" || tags.indexOf(tag) !== -1;
        it.hidden = !show;
        if (show) shown++;
      });
      var empty = scope.querySelector("#cs-empty");
      if (empty) empty.hidden = shown !== 0;
      var live = scope.querySelector("[data-filter-status]");
      if (live) live.textContent = shown + (shown === 1 ? " item shown" : " items shown");
    });
  });

  // Demo forms: no data leaves the page
  document.querySelectorAll("form[data-demo-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector("[data-demo-note]") || form.parentElement.querySelector("[data-demo-note]");
      var email = form.querySelector('input[type="email"]');
      if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.value)) {
        email.setAttribute("aria-invalid", "true");
        if (note) { note.textContent = "Enter a valid email address."; note.hidden = false; }
        email.focus();
        return;
      }
      if (email) email.removeAttribute("aria-invalid");
      // demo: not sent. Nothing is transmitted or stored.
      if (note) { note.textContent = "Demo only: nothing was sent or saved. This form is not connected to anything yet."; note.hidden = false; }
    });
  });

  // Print button
  document.querySelectorAll("[data-print]").forEach(function (b) {
    b.addEventListener("click", function () { window.print(); });
  });

  // Copy buttons
  document.querySelectorAll("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var target = document.querySelector(b.getAttribute("data-copy"));
      if (!target) return;
      var text = target.textContent;
      var done = function () { var t = b.textContent; b.textContent = "Copied"; setTimeout(function () { b.textContent = t; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, function () {});
    });
  });
})();
