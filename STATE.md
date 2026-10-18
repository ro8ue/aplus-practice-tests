# A+ Practice Test Ranker (formerly VoucherWatch A+): state 18 Oct 2026 (SAST)

## Live
- URL: https://ro8ue.github.io/aplus-practice-tests/ (GitHub Pages, main branch root) (repo renamed from voucherwatch-aplus on 18 Oct)
- Repo: https://github.com/ro8ue/aplus-practice-tests (public)
- Pivot approved 18 Oct after r/CompTIA removed the voucher post. All voucher seller tables have been removed. The site only points to CompTIA and Pearson VUE for vouchers, with a safety note. Old voucher URLs (220-1201.html, 220-1202.html, outside-us.html, how-we-check.html) redirect to home with noindex. The old voucher data is archived locally in archive/ and is not in the repo.
- Pages: index (comparison + best-for picks), one page per test (dion-udemy, professor-messer, certmaster-practice, examcompass, crucial-exams, burningicetech, tia-ramdayal), practice-vs-real-scores (9 cited data points; "submit your scores: coming soon"), methodology (method + disclosure).
- Data: data/tests.json. To update: edit, run `python3 build.py`, commit, push. Facts checked 2026-10-18.
- Newsletter: Beehiiv, publication VoucherWatch A+ (https://aplus-practice-tests.beehiiv.com/), form id 15c91c67-f932-4b17-b631-62f1e5d4e75b, on every content page. The site copy now says "weekly A+ study email". The Beehiiv form's own tagline still reads "cheapest CompTIA A+ exam vouchers"; change it in Beehiiv.
- No affiliate links, no tracking scripts.

## Unverified / gaps
- Udemy prices for Dion and TIA vary and weren't recorded.
- CertMaster Practice price wasn't checked on CompTIA's own store (a third-party listing shows $149 regular / $124 sale).
- Messer Core 2 page wasn't opened.
- Crucial Exams pricing pages show two different plan sets.
- ExamCompass per-test question count and Core 2 count not recorded.
- Crucial Exams 1202 and TIA 1202 not checked.
- Kaplan and IBM tests are mentioned in threads but not researched.

## Next steps (need Ali's yes)
1. Rename the Beehiiv publication and form tagline to "A+ Practice Test Ranker".
2. Optionally rename the repo to aplus-practice-test-ranker. The URL would change, so base_url needs updating; GitHub redirects git remotes, not Pages URLs.
3. A free Google Form (or Tally) for score submissions.
4. Weekly routine: re-check prices and question counts, add new pass-post data points, send the weekly email.
5. Reddit: a data-first post with no link (see report).
6. Affiliate applications (Udemy via Impact, CompTIA) later; update the disclosure first.

## SEO guide pages (added 18 Oct 2026). Content lives in guides.py and tables come from data/tests.json
| Page | Target query (from Google autocomplete) |
|---|---|
| dion-vs-messer-a-plus-practice-tests.html | dion vs messer / dion vs professor messer |
| is-certmaster-practice-worth-it.html | is certmaster practice worth it |
| best-free-a-plus-practice-tests.html | free comptia a+ practice test / comptia a+ 1201 practice test free |
| what-practice-test-score-to-pass-a-plus.html | what score do you need to pass comptia a+ (practice-score angle) |
| a-plus-pbq-practice.html | a+ pbq practice / a+ pbq questions |
| a-plus-1201-vs-1101.html | a+ 1201 vs 1101 |
| a-plus-passing-score-and-exam-format.html | a+ 1201 passing score / a+ passing score |
Each guide has an answer-first intro, a comparison table, sources, an FAQ, Article + FAQPage JSON-LD, a last-updated date, related links and the score form CTA. All are linked from home and listed in the sitemap.
Google's sitemap ping endpoint was retired in 2023, so we rely on the sitemap submitted in Search Console. Optionally use URL Inspection, then "Request indexing", for the new pages.
