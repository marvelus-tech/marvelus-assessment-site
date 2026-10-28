/* Booking page: step reveal, validation, embed slot. Demo only: nothing is sent. */
(function () {
  "use strict";
  var form = document.getElementById("book-form");
  if (!form) return;
  var steps = Array.prototype.slice.call(form.querySelectorAll(".bstep"));
  var cur = 1;
  function show(n) {
    cur = n;
    steps.forEach(function (s) { s.hidden = Number(s.getAttribute("data-step")) !== n; });
    var s = steps.filter(function (x) { return Number(x.getAttribute("data-step")) === n; })[0];
    var f = s && s.querySelector("input, select, textarea, a, button");
    if (f && n > 1) f.focus();
  }
  function validate(stepEl) {
    var ok = true;
    stepEl.querySelectorAll("[required]").forEach(function (el) {
      var bad = !el.value.trim() || (el.type === "email" && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
      el.setAttribute("aria-invalid", bad ? "true" : "false");
      var err = form.querySelector(".form-error");
      if (bad && ok) { ok = false; if (err) { err.textContent = "Please complete the highlighted field."; err.hidden = false; } el.focus(); }
    });
    if (ok) { var e = form.querySelector(".form-error"); if (e) e.hidden = true; }
    return ok;
  }
  form.addEventListener("click", function (e) {
    var b = e.target.closest("[data-next]");
    if (!b) return;
    e.preventDefault();
    var stepEl = b.closest(".bstep");
    var radios = stepEl.querySelectorAll('input[type="radio"]');
    if (radios.length && !stepEl.querySelector('input[type="radio"]:checked')) {
      var err0 = form.querySelector(".form-error");
      if (err0) { err0.textContent = "Please choose one option."; err0.hidden = false; }
      radios[0].focus();
      return;
    }
    if (validate(stepEl)) show(cur + 1);
  });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var stepEl = steps[cur - 1];
    if (!validate(stepEl)) return;
    // demo: not sent. The booking tool is a placeholder slot until one is chosen.
    var err = form.querySelector(".form-error");
    if (err) { err.textContent = "Demo only: nothing was sent or saved. The booking tool is not connected yet."; err.hidden = false; err.style.color = "inherit"; }
    var slot0 = document.getElementById("embed-slot");
    if (slot0) { slot0.hidden = false; }
  });
  // Radio steps get a Continue button (no auto-advance, so arrow keys do not skip a step)
  [1, 2].forEach(function (n) {
    var st = form.querySelector('.bstep[data-step="' + n + '"]');
    if (!st) return;
    var b = document.createElement("button");
    b.type = "button"; b.className = "btn btn--secondary"; b.textContent = "Continue";
    b.setAttribute("data-next", "");
    st.appendChild(b);
  });
  // Embed slot: only fills if a real booking URL is configured
  var slot = document.getElementById("embed-slot");
  var url = slot && slot.getAttribute("data-embed");
  if (slot && url && /^https:\/\//.test(url)) {
    var ifr = document.createElement("iframe");
    ifr.src = url; ifr.title = "Book a call"; ifr.style.cssText = "width:100%;min-height:640px;border:0";
    slot.innerHTML = ""; slot.appendChild(ifr);
  }
  show(1);
})();
