# Compliance check: CompTIA voucher terms (18 Oct 2026, SAST). Proposal only; live site unchanged.

## CompTIA voucher terms
The official page (certification.comptia.org/.../comptia-voucher-terms-conditions) returned 500 to WebFetch and timed out with curl; the comptia.org/en-us path returns 404. The terms text below is quoted from a CIN (CompTIA Instructors Network) thread (https://cin.comptia.org/threads/seemingly-unauthorized-resellers-how-do-they-do-it.1635/) and matches the T&Cs reproduced on professormesser.com/vouchers/:
- Buy vouchers only from the CompTIA Store, the Pearson VUE voucher store, or a CompTIA Authorized Partner.
- Vouchers may not be resold. They are country- and currency-restricted, non-refundable, can't be extended, and are exam/program specific.
- CompTIA is not responsible for vouchers from unauthorized resellers and won't replace fraudulent or used ones. The quoted text cuts off at "Individuals who use any unauthorize…"; the sanction wording (invalidated results/bans) is as Reddit cited, NOT verified by me.
- Allowed: comparing prices and linking to legitimate sellers. Nothing forbids a comparison site; the risk is pointing people at unauthorized resellers.

## No public partner directory exists right now
CompTIA's partner list was removed in 2025 (CIN thread https://cin.comptia.org/threads/authorized-partner-list-is-gone.2226/). On 2026-09-11 Learnerside found the old URL redirects to a general page with no list (https://learnerside.com/training-providers/comptia-authorized/). Only a Japan list is public. So **no seller can be "verified authorized" from a CompTIA source today.**

## Seller status
| Seller | Status | Evidence |
|---|---|---|
| CompTIA Store / Pearson VUE | Verified official (named in the terms) | Terms text above |
| Dion Training | Claims authorized ("Platinum partners to CompTIA"), unverified | https://www.diontraining.com/collections/vouchers |
| GetCertified4Less | Claims authorized ("CompTIA Authorized Platinum Partner", also a Pearson VUE test centre), unverified | https://getcertified4less.com/pages/about-us |
| Crucial Exams | Claims authorized ("now a CompTIA Authorized Partner", Mar 2024), unverified | https://crucialexams.com/posts/blog/crucial-exams-is-now-a-comptia-authorized-partner |
| Supreme ICT Academy | Claims to be a "recognised CompTIA Delivery Partner", unverified | https://supremeictacademy.co.za/exam-vouchers-and-services/ |
| Professor Messer | Sells vouchers with CompTIA's T&Cs, but I found no explicit partner claim. No evidence of status (widely used; parent should treat as unconfirmed) | https://www.professormesser.com/vouchers/ |
| Jumping Bean | No evidence found | none |
| SuperVoucher | No evidence; flagged. A CIN instructor wrote that it is not on CompTIA's partner list despite its claims, and questioned its global, different-expiry vouchers | https://cin.comptia.org/threads/seemingly-unauthorized-resellers-how-do-they-do-it.1635/ |

## Proposal
**(a) Keep:** CompTIA Store (add it as the official baseline at $274 list; ZA price to be checked), Dion Training, GetCertified4Less, Crucial Exams (re-verify its price first), and Supreme ICT Academy (ZA). Each labelled "claims CompTIA Authorized Partner; source: their page". **Remove:** SuperVoucher (this also removes the $189.95 "cheapest" callout). **Hold until confirmed:** Professor Messer and Jumping Bean. Email each to ask for proof of partner status (Ali's approval needed before sending), or ask CompTIA support.

**(b) Banner:**
> Only buy CompTIA vouchers from CompTIA, Pearson VUE, or a CompTIA Authorized Partner. Vouchers can't be resold, and codes from unauthorized sellers can be refused or put your certification at risk. We list only sellers that state they are authorized partners, with a link to where they say it. Confirm before you buy.

**(c) Does the idea still work?** Partly. With authorized sellers only, the spread is $246.60–$274 (about 10% off list), against $189.95 before. The "big savings" angle is weaker, and since CompTIA has no public directory, "authorized" can only be shown as each seller's claim. The site could still work as a "safe voucher + retake/region guide", but its differentiation and the affiliate math (about 10% of roughly $250) are thin. It's also risky on Reddit, since voucher posts trigger exactly this removal.

**Fallback pivot (recommended to consider): A+ Practice Test Ranker.** A database of 220-1201/1202 practice tests (Dion, Messer, CertMaster, ExamCompass, Crucial Exams, BurningIceTech, IBM) with price, PBQs, difficulty and a crowd-sourced "practice score vs real score" table. No compliance issues around voucher resale, it fits r/CompTIA's dominant "Passed!" post format, and it monetizes through the Udemy affiliate program (10%, 7-day cookie) and CertMaster. The existing GitHub Pages site and Beehiiv publication can be reused; vouchers would become a small "official ways to buy" section.
