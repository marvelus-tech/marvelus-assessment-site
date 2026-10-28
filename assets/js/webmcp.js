/* WebMCP tools for MarvelUs. Registers via navigator.modelContext when present.
 * Fallback: window.__marvelusTools (callable on the page) and /agents.json, /.well-known/agent.json.
 * Every tool returns the envelope {ok, data, meta, delight}. Facts live in data only. Read only, nothing is sent. */
(function () {
  "use strict";
  var S = window.MARVELUS_SITE;
  if (!S) return;
  var D = S.data;

  function envelope(tool, data, ok) {
    var env = { ok: ok !== false, data: data, meta: { tool: tool, version: "1.0", site: S.config.siteUrl + "/", generated_at: S.config.buildDate, page: location.pathname,
      draft_notice: S.config.noindex ? "Draft site: placeholders remain and pages are marked noindex." : null } };
    if (env.ok && S.delight[tool]) env.delight = S.delight[tool];   // delight is optional and skipped on errors
    return env;
  }
  function err(tool, code, message) { return envelope(tool, { error: { code: code, message: message } }, false); }

  var impl = {
    get_offers: function () { return { offers: D.offers, note: "The three offers have equal weight." }; },
    get_assessment_details: function () { return D.assessment; },
    get_pricing: function () { return D.pricing; },
    get_sample_report: function () { return D.sample_report; },
    start_quiz_preview: function (args) {
      var q = window.MarvelUsQuiz, want = !args || args.open !== false, opened = false;
      if (q && want) { q.open(); opened = true; }
      return Object.assign({}, D.quiz, { available_on_this_page: !!q, opened: opened, stored: false, sent: false,
        where: q ? location.pathname + "#start" : "/#start" });
    },
    get_contact: function () {
      var c = D.contact || {};
      return Object.assign({}, c, { email: S.config.contactEmail, phone: S.config.contactPhone,
        status: (S.config.contactEmail && S.config.contactPhone) ? "published" : "placeholder",
        booking_page: S.config.siteUrl + S.config.bookingPath });
    },
    get_site_map: function () { return { pages: D.site_map, manifest: S.config.siteUrl + "/agents.json" }; }
  };

  var tools = {};
  S.tools.forEach(function (t) {
    tools[t.name] = function (args) {
      try { return envelope(t.name, impl[t.name](args || {})); }
      catch (e) { return err(t.name, "tool_failed", String(e && e.message || e)); }
    };
  });
  window.__marvelusTools = tools;            // on-page fallback
  window.__marvelusToolList = S.tools;

  var defs = S.tools.map(function (t) {
    return {
      name: t.name, description: t.description, inputSchema: t.inputSchema,
      annotations: { readOnlyHint: true },
      execute: function (args) {
        return Promise.resolve({ content: [{ type: "text", text: JSON.stringify(tools[t.name](args)) }] });
      }
    };
  });
  var mc = navigator.modelContext;
  try {
    if (mc && typeof mc.registerTool === "function") {
      defs.forEach(function (d) { try { mc.registerTool(d); } catch (e) { /* already registered */ } });
    } else if (mc && typeof mc.provideContext === "function") {
      mc.provideContext({ tools: defs });
    }
  } catch (e) { /* WebMCP unavailable: the fallback above still works */ }
})();
