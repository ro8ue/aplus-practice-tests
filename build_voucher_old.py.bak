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
offers = sorted(D["us_offers"], key=lambda o: o["price_usd"])
def table(exam=None):
    rows = "".join(f"<tr><td>{e(o['seller'])}</td><td class=p>${o['price_usd']:.2f}</td><td>{e(o['type'])}<br><span class=muted>{e(o['expiry'])}</span></td><td>{e(o['retake'])}</td><td>{e(o['region'])}</td><td>{o['checked']}</td><td><a href=\"{e(o['url'])}\" rel=\"nofollow noopener\">Seller page</a></td></tr>" for o in offers if not exam or exam in o["exams"])
    return f"<div class=tw><table><thead><tr><th>Seller</th><th>Price (USD)</th><th>Voucher type / expiry</th><th>Retake included</th><th>Region limits</th><th>Last checked</th><th>Link</th></tr></thead><tbody>{rows}</tbody></table></div>"
best = offers[0]; std = min((o for o in offers if "early" not in o["type"]), key=lambda o:o["price_usd"])
callout = f"""<div class=callout><div>Cheapest right now (one exam):</div><b class=big>${best['price_usd']:.2f}</b> at <b>{e(best['seller'])}</b>, {e(best['type'])}, {e(best['expiry'].lower())}. List price is ${S['list_price_usd']}.
<div class=muted>Need more time? The cheapest longer-dated voucher is ${std['price_usd']:.2f} at {e(std['seller'])} ({e(std['expiry'].lower())}). Checked {best['checked']}.</div></div>"""
signup = """<div class=box><h2 style="margin-top:0">Get the weekly A+ voucher price email</h2><p class=muted>One short email a week: the cheapest A+ vouchers, new sales, and expiry traps. No spam.</p>
<script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" data-beehiiv-form="15c91c67-f932-4b17-b631-62f1e5d4e75b"></script>
<p class=muted><a href="https://voucherwatch.beehiiv.com/subscribe" rel="noopener">Or subscribe here</a></p></div>"""
unv = "".join(f"<li>{e(u['seller'])}: {e(u['reason'])}</li>" for u in D["unverified"])
page("index.html", "CompTIA A+ Voucher Prices Compared (220-1201 & 220-1202) | VoucherWatch A+",
 f"Compare discounted CompTIA A+ exam voucher prices from authorized sellers. Cheapest today: ${best['price_usd']:.2f} vs ${S['list_price_usd']} list. Updated weekly.",
 f"<h1>Cheapest CompTIA A+ exam vouchers, compared</h1><p class=lead>Every A+ voucher price we could check, side by side, updated weekly, so you don't pay the ${S['list_price_usd']} list price twice.</p>{callout}"
 f"<h2>220-1201 (Core 1) voucher prices</h2>{table('220-1201')}<h2>220-1202 (Core 2) voucher prices</h2>{table('220-1202')}"
 f"<p class=muted>You need two vouchers (one per exam) to earn A+. Each seller's voucher works for either exam. Not shown because we couldn't verify the price today:</p><ul class=muted>{unv}</ul>{signup}")
for ex, nm, topics in [("220-1201","Core 1","hardware, mobile devices, networking, virtualization/cloud and hardware troubleshooting"),("220-1202","Core 2","operating systems, security, software troubleshooting and operational procedures")]:
    page(f"{ex}.html", f"CompTIA A+ {ex} ({nm}) Voucher: Cheapest Prices Today | VoucherWatch A+",
     f"Where to buy a discounted CompTIA A+ {ex} ({nm}) exam voucher. Prices from ${best['price_usd']:.2f}, compared and dated.",
     f"<h1>CompTIA A+ {ex} ({nm}) voucher prices</h1><p class=lead>{ex} is one of the two A+ exams. It covers {topics} (see CompTIA's official objectives). Here's what one voucher costs today.</p>{callout}{table(ex)}"
     f"<div class=box><h2 style='margin-top:0'>Before you buy</h2><ul><li>A voucher covers one exam. You'll need another for the other exam.</li><li>Early-expiry vouchers are cheaper, but only if you'll sit the exam before they expire. Expiry dates can't be extended.</li><li>Most US-priced vouchers only work if you test from the US, Canada or US territories. Outside the US? <a href='outside-us.html'>See regional options</a>.</li></ul></div>{signup}")
za = "".join(f"<tr><td>{e(z['seller'])}</td><td class=p>{e(z['price_zar'])}</td><td>{e(z['note'])}</td><td>{z['checked']}</td><td><a href=\"{e(z['url'])}\" rel=\"nofollow noopener\">Seller page</a></td></tr>" for z in D["za_offers"])
page("outside-us.html", "CompTIA A+ Voucher South Africa & Outside the US: Prices | VoucherWatch A+",
 "Buying a CompTIA A+ voucher in South Africa or outside the US? Which vouchers are region-locked, plus South African rand prices we checked.",
 f"<h1>A+ vouchers in South Africa and outside the US</h1><p class=lead>CompTIA vouchers are country- and currency-restricted, so a cheap US voucher may not work where you live.</p>"
 f"<div class=box><h2 style='margin-top:0'>Region rules we found (checked {S['updated']})</h2><ul><li><b>Professor Messer:</b> only for people physically in the US, Canada or US territories, for both online and in-person exams.</li><li><b>SuperVoucher:</b> the main A+ page is North America only. They point other regions to a separate page (prices there not checked yet).</li><li><b>GetCertified4Less:</b> says its voucher is valid worldwide except India. Buyers outside the US/Canada must pay with a verified PayPal account.</li><li><b>Dion Training:</b> region limits not listed on the page we checked.</li></ul></div>"
 f"<h2>South Africa: A+ voucher prices in rand (per exam)</h2><div class=tw><table><thead><tr><th>Seller</th><th>Price</th><th>Notes</th><th>Last checked</th><th>Link</th></tr></thead><tbody>{za}</tbody></table></div>"
 f"<p class=muted>Rand prices are what the sellers list. We haven't confirmed whether the US-dollar vouchers above can be used in South Africa, except GetCertified4Less, which says it's worldwide except India. Check with the seller first.</p>{signup}")
page("how-we-check.html", "How We Check A+ Voucher Prices & Disclosure | VoucherWatch A+",
 "How VoucherWatch A+ checks CompTIA A+ voucher prices every week, and our affiliate disclosure.",
 f"""<h1>How we check prices</h1><div class=box><ol><li>At least once a week we open every seller's public A+ voucher page and record the price shown, the voucher type, the expiry, retake terms and region limits, plus the date we checked.</li>
<li>We only list prices we saw ourselves on that date. If a page won't load or the price isn't clear, we leave the seller out and say so.</li><li>Anything a seller doesn't state is marked "not listed".</li><li>Prices can change at any time. The seller's checkout price is the real one.</li></ol></div>
<h2>Newsletter</h2><div class=box><p>Our weekly price email runs on <a href="https://voucherwatch.beehiiv.com/" rel="noopener">Beehiiv</a>. If you subscribe, Beehiiv handles your email address under its own privacy policy. You can unsubscribe from any email.</p></div>\n<h2>Disclosure</h2><div class=box><p>VoucherWatch A+ is independent and not affiliated with or endorsed by CompTIA or any seller listed. <b>Right now all seller links are plain links. We don't earn anything from them.</b></p>
<p class=todo>TODO (placeholder): if we join affiliate programs later, this section will name them, and we'll label affiliate links. Our ranking will always be by price, never by commission.</p></div>""")
(R/"style.css").write_text(CSS)
pages = ["index.html","220-1201.html","220-1202.html","outside-us.html","how-we-check.html"]
(R/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{S['base_url']}/{'' if p=='index.html' else p}</loc><lastmod>{S['updated']}</lastmod></url>\n" for p in pages) + "</urlset>\n")
(R/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {S['base_url']}/sitemap.xml\n")
print("built", pages)
