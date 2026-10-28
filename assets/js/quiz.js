/* MarvelUs preview quiz. Runs entirely in this page.
 * demo: not sent. The email step is a UI step only. Nothing is transmitted, stored, or read from your website.
 * No cookies, no localStorage, no network requests.
 */
(function () {
  "use strict";
  var Q = window.MARVELUS_QUIZ;
  var root = document.getElementById("quiz-root");
  var panel = document.getElementById("start");
  if (!Q || !root || !panel) return;

  var STEP_IDS = ["web", "bottleneck", "industry", "hours", "breaks", "tools", "cost", "size", "name", "gen", "gate", "result"];
  var NUM = { web: 1, bottleneck: 2, industry: 2, hours: 3, breaks: 4, tools: 5, cost: 6, size: 7, name: 8, gen: 9 };
  var LABEL = { web: "Your website", bottleneck: "The bottleneck", industry: "Not quite?", hours: "The hours", breaks: "Where it breaks", tools: "The tools", cost: "The cost", size: "The size", name: "Last question", gen: "Building your result" };
  var TOOL_SHORT = ["email", "spreadsheets", "your accounting software", "a customer list", null, "Word documents and PDFs", "paper and phone calls"];

  var state, history, genTimer, statusTimer;

  function fresh() {
    return { web: "", webSkipped: false, bottleneck: "", industry: null, industryGuessed: false, hours: null, breaks: [], breaksOther: "",
             tools: [], toolsOther: "", cost: null, costOther: "", size: null, name: "", email: "", business: "", role: "", heard: "", tips: false,
             rate: Q.rate, sample: false };
  }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function money(n) { return "$" + Math.round(n).toLocaleString("en-AU"); }
  function byId(list, id) { for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i]; return null; }
  function industry() { return byId(Q.industries, state.industry) || byId(Q.industries, "other"); }
  function lowerFirst(s) { return /^[A-Z][a-z]/.test(s) ? s.charAt(0).toLowerCase() + s.slice(1) : s; }

  /* ---------- logic ---------- */
  function guessIndustry(text) {
    var t = " " + text.toLowerCase() + " ", best = null, bestScore = 0;
    Q.industries.forEach(function (ind) {
      var sc = 0; ind.kw.forEach(function (k) { if (t.indexOf(k) !== -1) sc++; });
      if (sc > bestScore) { best = ind.id; bestScore = sc; }
    });
    return best;
  }
  function classify(text) {
    var t = " " + text.toLowerCase() + " ", best = null, bestScore = 0;
    Q.packs.forEach(function (p) {
      if (p.id === "Z") return;
      var sc = 0; p.kw.forEach(function (k) { if (t.indexOf(k) !== -1) sc++; });
      if (sc > bestScore) { best = p; bestScore = sc; }   // strict >: a tie keeps the earlier pack
    });
    return best || byId(Q.packs, "Z");
  }
  function toolsPhrase() {
    var ind = industry(), names = [];
    state.tools.forEach(function (i) {
      if (i === "other") { if (state.toolsOther.trim()) names.push(state.toolsOther.trim()); return; }
      var s = TOOL_SHORT[i];
      names.push(s === null ? lowerFirst(ind.tool5) : s);
    });
    names = names.slice(0, 3);
    if (!names.length) return "your current tools";
    if (names.length === 1) return names[0];
    return names.slice(0, -1).join(", ") + " and " + names[names.length - 1];
  }
  function fill(s, pack) {
    var ind = industry();
    return String(s).replace(/\{tools\}/g, toolsPhrase()).replace(/\{nouns\}/g, ind.nouns).replace(/\{noun\}/g, ind.noun).replace(/\{doc\}/g, ind.doc);
  }
  function hoursMid() { var b = byId(Q.hours, state.hours); return b ? b.mid : null; }
  function monthly(h, rate) { return Math.round(h * rate * Q.weeks); }

  /* ---------- rendering helpers ---------- */
  function shell(id, inner, opts) {
    opts = opts || {};
    var n = NUM[id], pct = n ? Math.round((n / 9) * 100) : 100;
    var top = '<div class="q-top"><div>' + (opts.noBack ? "" : '<button type="button" class="btn btn--ghost btn--sm" data-back>Back</button>') + '</div>' +
      '<p class="q-label">' + (n ? esc(LABEL[id]) + " &middot; " + n + " of 9" : esc(opts.label || "")) + '</p></div>' +
      '<div class="q-progress" role="progressbar" aria-label="Quiz progress" aria-valuemin="0" aria-valuemax="9" aria-valuenow="' + (n || 9) + '"><span style="width:' + pct + '%"></span></div>';
    root.innerHTML = '<div class="q-card">' + top + inner + '<p class="demo-note">Preview only. Nothing you type is stored or sent anywhere, and we do not read your website.</p></div>';
  }
  function focusTitle() {
    var t = root.querySelector(".q-title");
    if (t) { t.setAttribute("tabindex", "-1"); t.focus({ preventScroll: true }); }
  }
  function showErr(msg, el) {
    var e = root.querySelector(".q-err");
    if (e) { e.textContent = msg; e.hidden = false; }
    if (el) { el.setAttribute("aria-invalid", "true"); el.focus(); }
  }
  function radios(name, items, selected) {
    return items.map(function (it, i) {
      var v = typeof it === "string" ? it : it.id, l = typeof it === "string" ? it : it.label;
      return '<label class="choice"><input type="radio" name="' + name + '" value="' + esc(v) + '"' + (selected === v ? " checked" : "") + '><span>' + esc(l) + '</span></label>';
    }).join("");
  }
  function checks(name, labels, selected, withOther, otherText, otherLabel) {
    var h = labels.map(function (l, i) {
      return '<label class="choice"><input type="checkbox" name="' + name + '" value="' + i + '"' + (selected.indexOf(i) !== -1 ? " checked" : "") + '><span>' + esc(l) + '</span></label>';
    }).join("");
    if (withOther) {
      h += '<label class="choice"><input type="checkbox" name="' + name + '" value="other"' + (selected.indexOf("other") !== -1 ? " checked" : "") + '><span>Something else</span></label>' +
        '<div class="field" data-other ' + (selected.indexOf("other") !== -1 ? "" : "hidden") + '><label for="q-other">' + esc(otherLabel) + '</label><input id="q-other" type="text" maxlength="120" value="' + esc(otherText) + '"></div>';
    }
    return h;
  }
  function form(inner, btn) {
    return '<form novalidate data-form>' + inner + '<p class="q-err form-error" role="alert" hidden></p><div class="q-actions">' + btn + '</div></form>';
  }
  var CONT = '<button type="submit" class="btn btn--primary">Continue <span class="btn__arrow" aria-hidden="true">&rarr;</span></button>';

  /* ---------- steps ---------- */
  var R = {};
  R.web = function () {
    shell("web", '<h2 class="q-title">What is your business website?</h2><p class="q-help">In this preview we do not read your site. Add it if you like, or skip, and we keep the result general.</p>' +
      form('<div class="field"><label for="q-web" class="sr-only">Business website</label><input id="q-web" type="text" inputmode="url" autocomplete="url" placeholder="yourbusiness.com.au" value="' + esc(state.web) + '"></div>',
        CONT + '<button type="button" class="linklike" data-skip>Skip, keep it general</button>'), { noBack: true });
  };
  R.bottleneck = function () {
    var ph = (byId(Q.industries, state.industry) || byId(Q.industries, "other")).ph;
    shell("bottleneck", '<h2 class="q-title">Where does your business lose the most time?</h2><p class="q-help">One or two sentences is plenty.</p>' +
      form('<div class="field"><label for="q-bn" class="sr-only">Where your business loses the most time</label><textarea id="q-bn" rows="3" maxlength="400" placeholder="' + esc(ph) + '">' + esc(state.bottleneck) + '</textarea></div>', CONT));
  };
  R.industry = function () {
    shell("industry", '<h2 class="q-title">Which of these is closest to your business?</h2><p class="q-help">' +
      (state.industryGuessed ? "We picked one from what you wrote. Change it if it is wrong." : "Pick one so the examples fit you.") + '</p>' +
      form('<fieldset><legend class="sr-only">Closest industry</legend>' + radios("industry", Q.industries, state.industry) + '</fieldset>', CONT));
  };
  R.hours = function () {
    shell("hours", '<h2 class="q-title">Roughly how many hours a week does your team spend on this?</h2><p class="q-help">A rough guess is fine. Count everyone who touches it.</p>' +
      form('<fieldset><legend class="sr-only">Hours a week</legend>' + radios("hours", Q.hours, state.hours) + '</fieldset>', CONT));
  };
  R.breaks = function () {
    var pack = classify(state.bottleneck), labels = pack.breaks.map(function (l) { return fill(l); });
    if (pack.id === "Z") labels = ["Waiting for someone to approve", "Typing the same details again", "Hunting for information", "Chasing people", "Mistakes and rework", "Slow replies to customers", "No one can see where things are up to"];
    state._breakLabels = labels;
    shell("breaks", '<h2 class="q-title">Where does it usually go wrong?</h2><p class="q-help">Pick all that apply.</p>' +
      form('<fieldset><legend class="sr-only">Where it goes wrong</legend>' + checks("breaks", labels, state.breaks, true, state.breaksOther, "What else?") + '</fieldset>', CONT));
  };
  R.tools = function () {
    var ind = industry(), labels = Q.toolsDefault.map(function (t) { return t.replace("{tool5}", ind.tool5); });
    shell("tools", '<h2 class="q-title">Where does this work happen today?</h2><p class="q-help">Pick all that apply.</p>' +
      form('<fieldset><legend class="sr-only">Where the work happens</legend>' + checks("tools", labels, state.tools, true, state.toolsOther, "What else?") + '</fieldset>', CONT));
  };
  R.cost = function () {
    var ind = industry(), opts = Q.costDefault.slice();
    if (ind.cost_extra) opts.push(ind.cost_extra);
    opts.push("Something else");
    shell("cost", '<h2 class="q-title">When this slips, what does it cost you?</h2>' +
      form('<fieldset><legend class="sr-only">What it costs you</legend>' + radios("cost", opts, state.cost) +
        '<div class="field" data-other ' + (state.cost === "Something else" ? "" : "hidden") + '><label for="q-other">What is it?</label><input id="q-other" type="text" maxlength="120" value="' + esc(state.costOther) + '"></div></fieldset>', CONT));
  };
  R.size = function () {
    shell("size", '<h2 class="q-title">Roughly what is your annual revenue?</h2><p class="q-help">This helps us pitch the result at the right scale. Amounts are in Australian dollars.</p>' +
      form('<fieldset><legend class="sr-only">Annual revenue</legend>' + radios("size", Q.revenue, state.size) + '</fieldset>', CONT));
  };
  R.name = function () {
    shell("name", '<h2 class="q-title">What is your first name?</h2>' +
      form('<div class="field"><label for="q-name" class="sr-only">First name</label><input id="q-name" type="text" autocomplete="given-name" maxlength="40" placeholder="Sam" value="' + esc(state.name) + '"></div>',
        '<button type="submit" class="btn btn--primary">Get my result <span class="btn__arrow" aria-hidden="true">&rarr;</span></button>'));
  };
  var LINES = ["Reading your answers...", "Finding your biggest time leak...", "Working out what it costs you...", "Writing it up..."];
  R.gen = function () {
    shell("gen", '<div class="q-gen"><h2 class="q-title">Putting your result together</h2><div class="q-spinner" aria-hidden="true"></div>' +
      '<p class="q-status" id="q-status" role="status" aria-live="polite">' + LINES[0] + '</p><p class="small muted">A few seconds. It opens here.</p></div>', { noBack: true });
    var i = 0, step = Math.max(300, Math.round(Q.generatingMs / LINES.length));
    statusTimer = setInterval(function () { i = Math.min(i + 1, LINES.length - 1); var el = document.getElementById("q-status"); if (el) el.textContent = LINES[i]; }, step);
    genTimer = setTimeout(function () { clearInterval(statusTimer); go("gate", true); }, Q.generatingMs);
  };
  R.gate = function () {
    var roleOpts = '<option value="">Choose one</option>' + Q.roles.map(function (r) { return '<option' + (state.role === r ? " selected" : "") + '>' + esc(r) + '</option>'; }).join("");
    var heardOpts = '<option value="">Choose one</option>' + Q.heard.map(function (r) { return '<option' + (state.heard === r ? " selected" : "") + '>' + esc(r) + '</option>'; }).join("");
    shell("gate", '<h2 class="q-title">Your result is ready. Where should we send it?</h2>' +
      '<p class="notice small" role="note"><strong>Demo:</strong> nothing is sent. This step shows how the live version would work. Use any text you like, it stays in this browser tab.</p>' +
      form('<div class="field"><label for="g-email">Email <span aria-hidden="true">*</span></label><input id="g-email" type="email" autocomplete="email" value="' + esc(state.email) + '"></div>' +
        '<div class="field"><label for="g-biz">Business name <span aria-hidden="true">*</span></label><input id="g-biz" type="text" autocomplete="organization" value="' + esc(state.business) + '"></div>' +
        '<div class="field"><label for="g-role">Your role <span aria-hidden="true">*</span></label><select id="g-role">' + roleOpts + '</select></div>' +
        '<div class="field"><label for="g-heard">How did you hear about us? <span class="small muted">(optional)</span></label><select id="g-heard">' + heardOpts + '</select></div>' +
        '<div class="field field--check"><label><input type="checkbox" id="g-tips"' + (state.tips ? " checked" : "") + '> Send me occasional practical tips from MarvelUs. I can unsubscribe at any time.</label></div>' +
        '<p class="small muted">By continuing you agree to our <a class="text-link" href="' + MV.url("/terms/") + '">Terms</a> and <a class="text-link" href="' + MV.url("/privacy/") + '">Privacy Policy</a>. Both are drafts.</p>',
        '<button type="submit" class="btn btn--primary">Open my result <span class="btn__arrow" aria-hidden="true">&rarr;</span></button><button type="button" class="linklike" data-edit>Edit my answers</button>'), { label: "Last step" });
  };

  /* ---------- result ---------- */
  function resultHtml() {
    var pack = state.forcePack ? byId(Q.packs, state.forcePack) : classify(state.bottleneck), ind = industry(), mid = hoursMid(), S = state.sample;
    var mark = function (t) { return S ? '<span class="sample-data" data-sample="1">' + esc(t) + '</span>' : esc(t); };
    var name = state.name.trim();
    var hoursTxt = mid == null ? "Not measured yet" : mid + " hours a week";
    var costTxt = mid == null ? "Not worked out yet" : money(monthly(mid, state.rate)) + " a month";
    var steps = pack.steps.map(function (s) {
      return '<li><span>' + esc(fill(s.t)) + '</span><span class="who' + (s.person ? " who--you" : "") + '">Today: by hand. Later: ' + (s.person ? "still you" : "AI") + '</span></li>';
    }).join("");
    var head = S ? '<p class="stamp">Example, not a client result</p>' : '<p class="eyebrow">Your first AI opportunity</p>';
    var h1 = S ? '<span class="sample-data" data-sample="1">' + esc(pack.name) + '</span>' : esc((name ? name + ", start with " : "Start with ") + pack.name.charAt(0).toLowerCase() + pack.name.slice(1)) + ".";
    var cost = "";
    if (mid != null) {
      cost = '<div class="notice" id="cost-box"><p><strong>Rough monthly cost:</strong> ' + mid + ' hours &times; $<span data-rate-out>' + state.rate + '</span> &times; ' + Q.weeks + ' = <strong data-cost-out>' + money(monthly(mid, state.rate)) + '</strong>.</p>' +
        '<p class="small">We used $' + state.rate + ' an hour as a default for this preview. Your own rate is used in the full assessment.</p>' +
        '<div class="rate-box"><div><label for="r-rate">Change the hourly rate (AUD)</label><input id="r-rate" type="number" min="1" max="1000" step="1" value="' + state.rate + '"></div></div></div>';
    } else {
      cost = '<div class="notice"><p><strong>No dollar figure yet.</strong> You were not sure of the hours, so we have only ranked the task. Time it for one week and the full assessment will price it.</p></div>';
    }
    return '<div class="q-card result" aria-labelledby="res-h">' + head +
      '<h2 id="res-h" class="q-title">' + h1 + '</h2>' +
      (S ? '<p class="muted">Invented data, to show the layout. Yours uses your task, your numbers and your words.</p>' :
        '<p class="muted">Prepared for ' + esc(name || "you") + (state.business.trim() ? ", " + esc(state.business.trim()) : "") + '. Preview only, not the scored report.</p>') +
      '<div class="facts-row"><div class="fact"><p class="fact__k">Task</p><p class="fact__v">' + esc(pack.name) + '</p></div>' +
      '<div class="fact"><p class="fact__k">Time on this task</p><p class="fact__v">' + mark(hoursTxt) + '</p></div>' +
      '<div class="fact"><p class="fact__k">Rough cost</p><p class="fact__v" data-cost-fact>' + mark(costTxt) + '</p></div></div>' +
      '<h3>What is going on</h3><p>' + esc(fill(pack.problem)) + '</p>' +
      '<h3>How it could run</h3><ol class="flow">' + steps + '</ol>' +
      '<h3>This week, for free</h3><p>' + esc(fill(pack.week)) + '</p>' +
      '<h3>Keep with a person</h3><p>' + esc(fill(pack.person)) + '</p>' +
      '<h3>A prompt to try today</h3><div class="promptbox" id="prompt-box">' + esc(fill(pack.prompt)) + '</div>' +
      '<div class="btn-row"><button type="button" class="btn btn--ghost btn--sm" data-copy-prompt>Copy the prompt</button><button type="button" class="btn btn--ghost btn--sm" data-print-result>Print or save as PDF</button></div>' +
      cost +
      '<p class="small muted">This is a preview built from nine answers in your browser. It is not the scored report. A full assessment looks at the whole business.' + (S ? "" : " Nothing was sent or saved.") + '</p>' +
      (S ? '<p>This is an example. Yours uses your task, your numbers and your words, and takes about a minute.</p><div class="btn-row"><button type="button" class="btn btn--primary" data-start-real>Show me my #1 opportunity</button></div>' : "") +
      '</div>' +
      '<div class="q-card next-panel"><p class="eyebrow">The next step</p><h3>You have your #1. There are more.</h3>' +
      '<p>The Staff-level AI Assessment asks the people doing the work, not only the owner, and ranks every repeat task in hours and dollars a year. It suits businesses with roughly 15 to 150 staff and is priced by headcount. Start with a 10-minute chat.</p>' +
      '<div class="btn-row"><a class="btn btn--primary" href="' + MV.url(Q.bookPath) + '?src=quiz" data-cta="book-chat" data-where="quiz-result">Book the 10-minute chat <span class="btn__arrow" aria-hidden="true">&rarr;</span></a>' +
      '<a class="btn btn--secondary" href="' + esc(Q.purchaseUrl) + '" data-cta="purchase" data-where="quiz-result">Or start smaller: Business Assessment, ' + esc(Q.priceLabel) + '</a>' + (S ? "" : '<button type="button" class="linklike" data-restart>Start over</button>') + '</div>' +
      '<p class="small muted">Bring your result to the chat. The Business Assessment is a smaller first step you can start now: a phone intake of ' + esc(Q.call) + ' and a scored report. ' + esc(Q.priceLong) + '. GST is not included in the $1,000.</p></div>';
  }
  R.result = function () {
    root.innerHTML = resultHtml();
    var rate = document.getElementById("r-rate");
    if (rate) rate.addEventListener("input", function () {
      var v = parseFloat(rate.value);
      if (!isFinite(v) || v < 1) return;
      state.rate = v;
      var mid = hoursMid();
      root.querySelector("[data-rate-out]").textContent = v;
      root.querySelector("[data-cost-out]").textContent = money(monthly(mid, v));
      var f = root.querySelector("[data-cost-fact]");
      var span = f.querySelector(".sample-data");
      (span || f).textContent = money(monthly(mid, v)) + " a month";
    });
  };

  /* ---------- flow ---------- */
  function go(id, push) {
    clearTimeout(genTimer); clearInterval(statusTimer);
    if (push !== false) history.push(id);
    R[id]();
    focusTitle();
    panel.hidden = false;
  }
  function back() {
    history.pop();
    var prev = history[history.length - 1];
    if (!prev) { go("web", false); history = ["web"]; return; }
    go(prev, false);
  }
  function others(name) { return Array.prototype.map.call(root.querySelectorAll('input[name="' + name + '"]:checked'), function (i) { return i.value === "other" ? "other" : Number(i.value); }); }
  function checkedVal(name) { var c = root.querySelector('input[name="' + name + '"]:checked'); return c ? c.value : null; }
  var WEB_RE = /^(https?:\/\/)?([a-z0-9-]+\.)+[a-z]{2,}(\/\S*)?$/i;

  function submit(cur) {
    var el;
    if (cur === "web") {
      el = root.querySelector("#q-web"); var v = el.value.trim();
      if (v && !WEB_RE.test(v)) return showErr("That does not look like a web address. Check it, or skip this step.", el);
      state.web = v; state.webSkipped = !v; return go("bottleneck");
    }
    if (cur === "bottleneck") {
      el = root.querySelector("#q-bn"); if (el.value.trim().length < 4) return showErr("Add a few words about where the time goes.", el);
      state.bottleneck = el.value.trim();
      if (!state._industryChosen) { var g = guessIndustry(state.bottleneck); if (g) state.industry = g; state.industryGuessed = !!g; }
      return go("industry");
    }
    if (cur === "industry") {
      var iv = checkedVal("industry"); if (!iv) return showErr("Choose the closest option to continue.", root.querySelector('input[name="industry"]'));
      state.industry = iv; state._industryChosen = true; return go("hours");
    }
    if (cur === "hours") {
      var hv = checkedVal("hours"); if (!hv) return showErr("Choose an option to continue.", root.querySelector('input[name="hours"]'));
      state.hours = hv; return go("breaks");
    }
    if (cur === "breaks") {
      var b = others("breaks"); if (!b.length) return showErr("Pick at least one, or choose Something else.", root.querySelector('input[name="breaks"]'));
      state.breaks = b; var o = root.querySelector("#q-other"); state.breaksOther = o ? o.value.trim() : ""; return go("tools");
    }
    if (cur === "tools") {
      var t = others("tools"); if (!t.length) return showErr("Pick at least one, or choose Something else.", root.querySelector('input[name="tools"]'));
      state.tools = t; var o2 = root.querySelector("#q-other"); state.toolsOther = o2 ? o2.value.trim() : ""; return go("cost");
    }
    if (cur === "cost") {
      var cv = checkedVal("cost"); if (!cv) return showErr("Choose an option to continue.", root.querySelector('input[name="cost"]'));
      state.cost = cv; var o3 = root.querySelector("#q-other"); state.costOther = o3 ? o3.value.trim() : ""; return go("size");
    }
    if (cur === "size") {
      var sv = checkedVal("size"); if (!sv) return showErr("Choose an option to continue.", root.querySelector('input[name="size"]'));
      state.size = sv; return go("name");
    }
    if (cur === "name") {
      el = root.querySelector("#q-name"); if (!el.value.trim()) return showErr("Add your first name.", el);
      state.name = el.value.trim(); return go("gen");
    }
    if (cur === "gate") {
      var em = root.querySelector("#g-email"), bz = root.querySelector("#g-biz"), rl = root.querySelector("#g-role");
      [em, bz, rl].forEach(function (x) { x.removeAttribute("aria-invalid"); });
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value.trim())) return showErr("Enter a valid email address.", em);
      if (!bz.value.trim()) return showErr("Add your business name.", bz);
      if (!rl.value) return showErr("Choose your role.", rl);
      // demo: not sent. The values below stay in memory for this tab and are used to personalise the on-screen result only.
      state.email = em.value.trim(); state.business = bz.value.trim(); state.role = rl.value;
      state.heard = root.querySelector("#g-heard").value; state.tips = root.querySelector("#g-tips").checked;
      return go("result");
    }
  }

  root.addEventListener("submit", function (e) {
    var f = e.target.closest("[data-form]"); if (!f) return;
    e.preventDefault();
    submit(history[history.length - 1]);
  });
  root.addEventListener("click", function (e) {
    var t = e.target;
    if (t.closest("[data-back]")) return back();
    if (t.closest("[data-skip]")) { state.web = ""; state.webSkipped = true; return go("bottleneck"); }
    if (t.closest("[data-edit]")) { history = ["web", "bottleneck", "industry", "hours", "breaks", "tools", "cost", "size", "name"]; return go("name", false); }
    if (t.closest("[data-restart]")) { start(false); return; }
    if (t.closest("[data-start-real]")) { start(false); return; }
    if (t.closest("[data-print-result]")) return window.print();
    if (t.closest("[data-copy-prompt]")) {
      var txt = document.getElementById("prompt-box").textContent, btn = t.closest("[data-copy-prompt]");
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(function () { btn.textContent = "Copied"; }, function () {});
      return;
    }
  });
  root.addEventListener("change", function (e) {
    var o = root.querySelector("[data-other]"); if (!o) return;
    if (e.target.name === "breaks" || e.target.name === "tools") {
      var on = root.querySelector('input[name="' + e.target.name + '"][value="other"]').checked; o.hidden = !on;
      if (on && e.target.value === "other") root.querySelector("#q-other").focus();
    } else if (e.target.name === "cost") {
      o.hidden = e.target.value !== "Something else";
    }
  });
  root.addEventListener("input", function (e) { if (e.target.hasAttribute("aria-invalid")) e.target.removeAttribute("aria-invalid"); });

  function reveal() {
    panel.hidden = false;
    panel.scrollIntoView({ behavior: MV.reduceMotion() ? "auto" : "smooth", block: "start" });
  }
  function start(sample) {
    state = fresh(); history = [];
    if (sample) {
      state.sample = true; state.industry = "trades"; state.hours = "5-10"; state.name = "Example"; state.business = "Example Plumbing Co";
      state.bottleneck = "We chase approved quotes and retype them. A quote goes out late on a Friday.";
      state.tools = [0, 1]; state.breaks = [0]; state.rate = Q.rate; state.forcePack = "A";
      history = ["result"]; R.result(); panel.hidden = false; focusTitle();
    } else { go("web"); }
    reveal();
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-open-quiz], [data-open-sample]"); if (!a) return;
    var sample = a.hasAttribute("data-open-sample");
    var href = a.getAttribute("href") || "";
    if (href.charAt(0) === "#" || href === "") { e.preventDefault(); start(sample); }
  });
  function fromHash() {
    var h = location.hash;
    if (h === "#start") start(false);
    else if (h === "#sample") start(true);
  }
  window.addEventListener("hashchange", fromHash);
  if (location.hash === "#start" || location.hash === "#sample") fromHash();

  window.MarvelUsQuiz = {
    open: function () { start(false); },
    openSample: function () { start(true); },
    describe: function () {
      return { steps: STEP_IDS.slice(0, 9).map(function (s) { return { id: s, label: LABEL[s], number: NUM[s] }; }), stored: false, sent: false };
    },
    _classify: classify, _monthly: monthly
  };
})();
