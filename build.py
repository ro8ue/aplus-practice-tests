import json, html, pathlib
R = pathlib.Path(__file__).parent; D = json.load(open(R/"data/tests.json")); S = D["site"]; T = D["tests"]; e = html.escape
CSS = """*{box-sizing:border-box}body{margin:0;font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#14202b;background:#f6f8fb}
a{color:#0b5fd1}header,main,footer{max-width:1080px;margin:0 auto;padding:16px}header{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between}
.logo{font-weight:800;font-size:20px;text-decoration:none;color:#14202b}.logo span{color:#0a8f5a}nav a{margin-left:14px;text-decoration:none;font-size:15px}
h1{font-size:clamp(26px,5vw,40px);line-height:1.15;margin:.4em 0 .2em}.lead{font-size:18px;color:#3c4b59;margin:0 0 20px}
.callout{background:#fff7e6;border:1px solid #e0a800;border-radius:12px;padding:14px 18px;margin:18px 0;font-size:15px}
.tw{overflow-x:auto;background:#fff;border-radius:12px;box-shadow:0 1px 3px #0001;margin:12px 0 28px}table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid #e6ebf0;vertical-align:top}th{background:#14202b;color:#fff;font-weight:600;white-space:nowrap}
.box{background:#fff;border-radius:12px;padding:18px 20px;box-shadow:0 1px 3px #0001;margin:20px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.pick{background:#e8f7ef;border-radius:12px;padding:14px 16px}.pick b{display:block;color:#0a8f5a;font-size:13px;text-transform:uppercase;letter-spacing:.03em}
blockquote{margin:8px 0;padding:6px 12px;border-left:3px solid #0a8f5a;background:#f3f7f5}.btn{display:inline-block;background:#0a8f5a;color:#fff;font-weight:700;text-decoration:none;padding:12px 20px;border-radius:8px;margin:6px 0}.muted{color:#5b6a78;font-size:14px}
footer{color:#5b6a78;font-size:14px;border-top:1px solid #dde3e9;margin-top:30px}@media(max-width:640px){nav a{margin:0 12px 0 0}th,td{padding:8px}}"""
def page(fn, title, desc, body):
    canon = S['base_url'] + "/" + ("" if fn == "index.html" else fn)
    (R/fn).write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{canon}"><link rel="stylesheet" href="style.css"></head><body>
<header><a class="logo" href="index.html">A+ Practice Test <span>Ranker</span></a><nav><a href="index.html">Compare</a><a href="practice-vs-real-scores.html">Practice vs real scores</a><a href="methodology.html">Methodology</a></nav></header>
<main>{body}</main><footer><p>Independent, not affiliated with CompTIA or any test maker. No affiliate links. Facts last checked {S['updated']}. <a href="methodology.html">Methodology &amp; disclosure</a>.</p></footer></body></html>""")
signup = """<div class=box><h2 style="margin-top:0">Get the weekly A+ study email</h2><p class=muted>One short email a week: practice test updates, new practice-vs-real score reports, and study tips for 220-1201/1202.</p>
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="15c91c67-f932-4b17-b631-62f1e5d4e75b"></script>
<p class=muted><a href="https://aplus-practice-tests.beehiiv.com/subscribe" rel="noopener">Or subscribe here</a></p></div>"""
safe = "<div class=callout><b>Buying a voucher?</b> Only buy CompTIA vouchers from CompTIA, Pearson VUE, or a CompTIA Authorized Partner. Vouchers can't be resold, and codes from unauthorized sellers can be refused or put your certification at risk. Official: <a href='https://www.comptia.org/en-us/certifications/a/core-1-and-2-v15/'>CompTIA A+</a> · <a href='https://home.pearsonvue.com/comptia'>Pearson VUE</a>.</div>"
free = lambda t: "Free" if t["free"] is True else ("Free tier + paid" if t["free"] == "freemium" else "Paid")
rows = "".join(f"<tr><td><a href='{t['slug']}.html'>{e(t['name'])}</a></td><td>{free(t)}<br><span class=muted>{e(t['price'])}</span></td><td>{e(t['questions'])}</td><td>{e(t['pbqs'])}</td><td>{e(t['covers'])}</td><td>{e(t['difficulty'])}</td></tr>" for t in T)
picks = "".join(f"<div class=pick><b>{lab}</b><a href='{s}.html'>{e(next(t['name'] for t in T if t['slug']==s))}</a></div>" for lab, s in [("Best full-length timed drilling","dion-udemy"),("Best official question style","certmaster-practice"),("Best for finding weak areas","crucial-exams"),("Best free walkthroughs","burningicetech"),("Best free quick quizzes","examcompass"),("Cheapest paid start","professor-messer")])
page("index.html", "Best CompTIA A+ Practice Tests Compared (220-1201 & 220-1202) | A+ Practice Test Ranker",
 "Compare CompTIA A+ 220-1201 and 220-1202 practice tests: Dion, Professor Messer, CertMaster, Crucial Exams, ExamCompass, BurningIceTech. Price, questions, PBQs and real-exam difficulty from pass posts.",
 f"<h1>CompTIA A+ practice tests, compared</h1><p class=lead>Price, question count, PBQs and how hard each one is compared with the real 220-1201/1202 exam, based on what people who passed actually said.</p>"
 f"<h2>Best for</h2><div class=grid>{picks}</div><h2>Comparison</h2><div class=tw><table><thead><tr><th>Practice test</th><th>Cost</th><th>Questions</th><th>PBQs</th><th>Covers</th><th>Vs real exam (pass posts)</th></tr></thead><tbody>{rows}</tbody></table></div>"
 f"<p class=muted>Note: the real A+ exams have up to 90 questions in 90 minutes. Passing is 675 (Core 1) and 700 (Core 2) on a 100-900 scale (<a href='https://www.comptia.org/en-us/certifications/a/core-1-and-2-v15/'>CompTIA</a>). See <a href='practice-vs-real-scores.html'>practice vs real scores</a>.</p><p>Passed A+? <a href='https://forms.gle/YCW25CpBCStuHMK29' rel='noopener'>Share your practice vs real scores</a> (anonymous, 2 minutes).</p>{signup}{safe}")
for t in T:
    links = " · ".join(f"<a href='{e(u)}' rel='nofollow noopener'>{e(l)}</a>" for l, u in t["links"])
    qs = "".join(f"<blockquote>{e(q)}<br><a class=muted href='{e(u)}' rel='nofollow noopener'>Source thread</a></blockquote>" for q, u in t["quotes"])
    unv = f"<p class=muted>Not fully verified: {e(t['unverified'])}</p>" if t.get("unverified") else ""
    page(f"{t['slug']}.html", f"{t['name']} for A+ 220-1201/1202: Review & Facts | A+ Practice Test Ranker",
     f"{t['name']}: price, questions, PBQs and how its difficulty compares with the real CompTIA A+ exam, from pass posts.",
     f"<h1>{e(t['name'])}</h1><p class=lead>Best for: {e(t['best_for'])}.</p><div class=tw><table><tbody>"
     f"<tr><th>Made by</th><td>{e(t['maker'])}</td></tr><tr><th>Cost</th><td>{free(t)}: {e(t['price'])}</td></tr><tr><th>Questions</th><td>{e(t['questions'])}</td></tr>"
     f"<tr><th>PBQs</th><td>{e(t['pbqs'])}</td></tr><tr><th>Covers</th><td>{e(t['covers'])}</td></tr><tr><th>Links</th><td>{links}</td></tr><tr><th>Checked</th><td>{S['updated']}</td></tr></tbody></table></div>"
     f"<h2>How it compares with the real exam</h2><p>{e(t['difficulty'])}</p>{qs}{unv}{signup}")
srows = "".join(f"<tr><td>{e(s['exam'])}</td><td>{e(s['practice'])}</td><td>{e(s['real'])}</td><td><a href='{e(s['url'])}' rel='nofollow noopener'>Reddit</a></td></tr>" for s in D["scores"])
page("practice-vs-real-scores.html", "A+ Practice Test Score vs Real Exam Score (Dion, CertMaster, Messer) | A+ Practice Test Ranker",
 "What practice test scores did people have before passing CompTIA A+ 220-1201 and 220-1202? Real data points from public pass posts, each cited.",
 f"<h1>Practice score vs real A+ score</h1><p class=lead>What people scored on practice tests before passing, taken only from public pass posts. {len(D['scores'])} data points so far.</p><a class=btn href='https://forms.gle/YCW25CpBCStuHMK29' rel='noopener'>Share your practice vs real scores</a>"
 f"<div class=tw><table><thead><tr><th>Exam</th><th>Practice scores</th><th>Real result</th><th>Source</th></tr></thead><tbody>{srows}</tbody></table></div>"
 "<p class=muted>Self-reported and not verified. A small sample, not a prediction. CompTIA doesn't publish how questions are weighted.</p>"
 "<div class=box><h2 style='margin-top:0'>Passed or sat 1201/1202?</h2><p>Add your data point. It takes 2 minutes, it's anonymous and no email is needed.</p><a class=btn href='https://forms.gle/YCW25CpBCStuHMK29' rel='noopener'>Share your practice vs real scores</a></div>" + signup)
page("methodology.html", "Methodology & Disclosure | A+ Practice Test Ranker", "How the A+ Practice Test Ranker collects facts and pass-post data, and our disclosure.",
 f"""<h1>Methodology &amp; disclosure</h1><div class=box><ul><li><b>Facts</b> (price, question count, PBQs, coverage) come from each product's own page or listing. We record the check date and mark anything we couldn't confirm.</li>
<li><b>Difficulty</b> summaries come only from public Reddit posts by test takers. We quote briefly and link every source. Opinions vary, and we show the dissenting ones too.</li><li><b>Practice vs real scores</b> are self-reported data points from public pass posts, each linked. We don't invent or estimate numbers.</li><li><b>Submissions</b> come through our <a href='https://forms.gle/YCW25CpBCStuHMK29'>score form</a>. They're anonymous, no email is collected, and an answer is only published (anonymised) if the person said it's OK to quote.</li>
<li>"Best for" picks are our editorial judgment from the above. They aren't paid.</li><li>Facts last checked: {S['updated']}. We plan to re-check weekly.</li></ul></div>
<h2>Disclosure</h2><div class=box><p>Independent, and not affiliated with CompTIA or any test maker. <b>No affiliate links right now.</b> If that changes, we'll say so here and label the links, and the picks won't depend on commissions.</p>
<p>Our weekly email runs on <a href="https://aplus-practice-tests.beehiiv.com/">Beehiiv</a>, which handles subscriber emails under its own privacy policy.</p><p>We used to compare voucher prices. We stopped, and now only point to official purchase channels.</p></div>{safe}""")
for old in ["220-1201.html","220-1202.html","outside-us.html","how-we-check.html"]:
    (R/old).write_text('<!doctype html><meta charset="utf-8"><title>Moved</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=index.html"><link rel="canonical" href="'+S['base_url']+'/"><p>Moved: <a href="index.html">A+ Practice Test Ranker</a></p>')
(R/"style.css").write_text(CSS)
pages = ["index.html","practice-vs-real-scores.html","methodology.html"] + [t["slug"]+".html" for t in T]
(R/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{S['base_url']}/{'' if p=='index.html' else p}</loc><lastmod>{S['updated']}</lastmod></url>\n" for p in pages) + "</urlset>\n")
(R/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {S['base_url']}/sitemap.xml\n")
print("built", pages)
