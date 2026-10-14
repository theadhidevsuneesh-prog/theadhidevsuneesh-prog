// Replace pandoc's <span class="math ...">\(..\)</span> with server-side KaTeX HTML.
// usage: node render_math.js in.html out.html
const fs = require("fs");
const katex = require("katex");

const [, , inp, outp] = process.argv;
let html = fs.readFileSync(inp, "utf8");

const unescape = (s) =>
  s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&");

const macros = {
  "\\R": "\\mathbb{R}",
  "\\dd": "\\,\\mathrm{d}",
  "\\d": "\\mathrm{d}",
  "\\tr": "\\operatorname{tr}",
  "\\rank": "\\operatorname{rank}",
  "\\adj": "\\operatorname{adj}",
  "\\sech": "\\operatorname{sech}",
  "\\cosec": "\\operatorname{cosec}",
  "\\ie": "\\text{i.e.}",
  "\\abs": "\\left|#1\\right|",
};

let count = 0, errors = 0;
html = html.replace(/<span class="math (inline|display)">([\s\S]*?)<\/span>/g, (m, kind, body) => {
  let tex = unescape(body);
  tex = tex.replace(/^\\\(/, "").replace(/\\\)$/, "").replace(/^\\\[/, "").replace(/\\\]$/, "");
  try {
    count++;
    return katex.renderToString(tex, {
      displayMode: kind === "display",
      throwOnError: true,
      output: "html",
      macros: Object.assign({}, macros),
      trust: false,
    });
  } catch (e) {
    errors++;
    console.error("KaTeX error:", e.message.split("\n")[0], "\n   in:", tex.slice(0, 120));
    return `<span style="color:red">[math error]</span>`;
  }
});
fs.writeFileSync(outp, html);
console.log(`rendered ${count} formulas, ${errors} errors`);
if (errors) process.exitCode = 2;
