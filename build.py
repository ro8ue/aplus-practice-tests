import json, html, pathlib
R = pathlib.Path(__file__).parent; D = json.load(open(R/"data/prices.json")); S = D["site"]
e = html.escape
CSS = """*{box-sizing:border-box}body{margin:0;font:16px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#14202b;background:#f6f8fb}
a{color:#0b5fd1}header,main,footer{max-width:1040px;margin:0 auto;padding:16px}header{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.logo{font-weight:800;font-size:20px;text-decoration:none;color:#14202b}.logo span{color:#0a8f5a}nav a{margin-left:14px;text-decoration:none;font-size:15px}
h1{font-size:clamp(28px,5vw,42px);line-height:1.15;margin:.4em 0 .2em}.lead{font-size:18px;color:#3c4b59;margin:0 0 20px}
.callout{background:#e8f7ef;border:2px solid #0a8f5a;border-radius:12px;padding:18px 20px;margin:18px 0}.callout b.big{font-size:30px;color:#0a8f5a}
.tw{overflow-x:auto;background:#fff;border-radius:12px;box-shadow:0 1px 3px #0001;margin:12px 0 28px}table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{padding:10px 12px;text-align:left;border-bottom:1px solid #e6ebf0;vertical-align:top}th{background:#14202b;color:#fff;font-weight:600;white-space:nowrap}td.p{font-weight:700;white-space:nowrap}
.box{background:#fff;border-radius:12px;padding:18px 20px;box-shadow:0 1px 3px #0001;margin:20px 0}form{display:flex;gap:8px;flex-wrap:wrap}input[type=email]{flex:1;min-width:200px;padding:11px;border:1px solid #c5cfd8;border-radius:8px;font-size:16px}
button{padding:11px 18px;border:0;border-radius:8px;background:#0a8f5a;color:#fff;font-weight:700;font-size:16px}.todo{font-size:13px;color:#a15c00}.muted{color:#5b6a78;font-size:14px}
footer{color:#5b6a78;font-size:14px;border-top:1px solid #dde3e9;margin-top:30px}
@media(max-width:640px){nav a{margin:0 12px 0 0}table{font-size:13.5px}th,td{padding:8px}}"""
def page(fn, title, desc, body):
    out = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{S['base_url']}/{'' if fn=='index.html' else fn}">
<link rel="stylesheet" href="style.css"></head><body><header><a class="logo" href="index.html">Voucher<span>Watch</span> A+</a>
<nav><a href="220-1201.html">220-1201</a><a href="220-1202.html">220-1202</a><a href="outside-us.html">Outside the US</a><a href="how-we-check.html">How we check</a></nav></header>
<main>{body}</main><footer><p>VoucherWatch A+ is independent and not affiliated with CompTIA. Prices change often; always confirm on the seller's page before buying. Last full check: {S['updated']}. <a href="how-we-check.html">How we check prices &amp; disclosure</a>.</p></footer></body></html>"""
    (R/fn).write_text(out)
BANNER = "<div class=callout><b>Buying a voucher?</b> Only buy CompTIA vouchers from CompTIA, Pearson VUE, or a CompTIA Authorized Partner. Vouchers can't be resold, and codes from unauthorized sellers can be refused or put your certification at risk.</div>"
SAFE = "<div class=box><h2 style='margin-top:0'>How to buy a voucher safely</h2><ul><li>CompTIA's official store: <a href='https://www.comptia.org/'>comptia.org</a> (Certifications, then A+, then exam voucher)</li><li>Pearson VUE (CompTIA's testing provider): <a href='https://home.pearsonvue.com/comptia'>home.pearsonvue.com/comptia</a></li></ul><p class=muted>We no longer compare third-party voucher sellers.</p></div>"
signup = """<div class=box><h2 style="margin-top:0">Get the weekly A+ study email</h2><p class=muted>One short email a week: A+ practice test comparisons, study tips and what recent passers used.</p>
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="15c91c67-f932-4b17-b631-62f1e5d4e75b"></script>
<p class=muted><a href="https://voucherwatch.beehiiv.com/subscribe" rel="noopener">Or subscribe here</a></p></div>"""
body = "<h1>We're rebuilding as an A+ practice test comparison</h1><p class=lead>We're turning this site into a comparison of CompTIA A+ 220-1201 and 220-1202 practice tests. Back soon.</p>" + BANNER + SAFE + signup
for fn,t in [("index.html","A+ Practice Test Comparison (rebuilding)"),("220-1201.html","A+ 220-1201 (rebuilding)"),("220-1202.html","A+ 220-1202 (rebuilding)"),("outside-us.html","A+ outside the US (rebuilding)"),("how-we-check.html","About (rebuilding)")]:
    page(fn, t+" | VoucherWatch A+", "We're rebuilding as a CompTIA A+ practice test comparison. How to buy a voucher safely.", body)
(R/"style.css").write_text(CSS)
pages = ["index.html","220-1201.html","220-1202.html","outside-us.html","how-we-check.html"]
(R/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{S['base_url']}/{'' if p=='index.html' else p}</loc><lastmod>{S['updated']}</lastmod></url>\n" for p in pages) + "</urlset>\n")
(R/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {S['base_url']}/sitemap.xml\n")
print("built", pages)
