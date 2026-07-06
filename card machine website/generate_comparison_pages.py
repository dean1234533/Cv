"""Generate DOJO vs competitor comparison pages."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

COMPARISONS = [
    {
        "slug": "dojo-vs-sumup",
        "competitor": "SumUp",
        "title": "DOJO vs SumUp — Which Card Machine is Right for Your Business?",
        "meta": "Comparing DOJO vs SumUp card machines: fees, features, payout speed, and support. Find out which is the better choice for UK businesses in 2026.",
        "intro": "SumUp is one of the most recognisable names in small business card payments. But recognisable doesn't mean best value. If you're choosing between a DOJO and a SumUp card machine for your UK business, there are some important differences that will affect your day-to-day operations and your monthly costs.",
        "verdict": "DOJO",
        "verdict_reason": "DOJO delivers faster payouts, stronger connectivity with automatic 4G backup, and 24/7 UK-based support. For businesses that rely on card payments to run, these aren't nice-to-haves — they're operational fundamentals.",
        "rows": [
            ("Monthly Rental", "£0 — Zero rental forever", "From £0 (some plans have costs)", "DOJO"),
            ("Transaction Fees", "Competitive low rate", "1.69%+ depending on plan", "DOJO"),
            ("Payout Speed", "Next working day", "1–3 business days", "DOJO"),
            ("Connectivity", "WiFi + automatic 4G backup", "WiFi only on most models", "DOJO"),
            ("UK Phone Support", "24/7 UK-based support team", "Online help / limited phone", "DOJO"),
            ("Card Types", "Visa, Mastercard, Amex + all contactless", "Visa & Mastercard primarily", "DOJO"),
            ("Hardware", "Professional countertop terminal", "Compact dongle/standalone", "Tie"),
            ("Contract", "No long-term lock-in", "No contract", "Tie"),
            ("DOJO App", "Full analytics and reporting portal", "SumUp app and dashboard", "Tie"),
            ("Suitable For", "All UK business sizes, especially hospitality, retail, trades", "Micro-businesses and sole traders", "Depends"),
        ],
    },
    {
        "slug": "dojo-vs-square",
        "competitor": "Square",
        "title": "DOJO vs Square — Which Card Machine is Right for Your Business?",
        "meta": "Comparing DOJO vs Square card machines: fees, payout speed, connectivity, and UK support. Which is the better choice for UK businesses in 2026?",
        "intro": "Square is popular globally, especially among US businesses, and has gained traction in the UK. But UK businesses have specific needs — particularly around payout speed and support availability — where DOJO has a clear advantage. Here's how they compare.",
        "verdict": "DOJO",
        "verdict_reason": "For UK-based businesses, DOJO's next-day payouts and 24/7 UK support make it the more reliable operational choice. Square's ecosystem is strong, but its payout delays and US-oriented support structure can create friction for day-to-day UK operations.",
        "rows": [
            ("Monthly Rental", "£0 — Zero rental forever", "£0 (hardware purchase required)", "Tie"),
            ("Transaction Fees", "Competitive low rate", "1.75% standard", "DOJO"),
            ("Payout Speed", "Next working day", "1–2 business days (UK)", "DOJO"),
            ("Connectivity", "WiFi + automatic 4G backup", "WiFi / Bluetooth", "DOJO"),
            ("UK Phone Support", "24/7 UK-based support team", "Mon–Fri business hours", "DOJO"),
            ("Card Types", "Visa, Mastercard, Amex + all contactless", "Visa, Mastercard, Amex", "Tie"),
            ("Hardware Cost", "FREE card machine", "Reader from £19 upwards", "DOJO"),
            ("POS Software", "DOJO App + portal", "Square POS — very feature-rich", "Square"),
            ("Inventory Management", "Basic", "Built-in and strong", "Square"),
            ("Suitable For", "UK hospitality, retail, service businesses", "Retail with complex inventory needs", "Depends"),
        ],
    },
    {
        "slug": "dojo-vs-zettle",
        "competitor": "Zettle by PayPal",
        "title": "DOJO vs Zettle — Which Card Machine is Right for Your Business?",
        "meta": "Comparing DOJO vs Zettle (by PayPal) card machines: fees, payout speed, support, and features for UK businesses in 2026.",
        "intro": "Zettle (owned by PayPal) is a well-established card payment option in the UK with a recognisable brand behind it. But for day-to-day business operations, what matters is payout speed, connectivity, and the quality of support when things go wrong. Here's how DOJO and Zettle compare on what actually matters.",
        "verdict": "DOJO",
        "verdict_reason": "DOJO's dual connectivity (WiFi + automatic 4G backup), next-day payouts, and 24/7 UK support give it a practical edge for businesses that depend on card payments throughout their trading day. Zettle's PayPal integration may suit businesses already deep in that ecosystem, but for most UK operators DOJO is the stronger everyday choice.",
        "rows": [
            ("Monthly Rental", "£0 — Zero rental forever", "£0 (reader purchase required)", "Tie"),
            ("Transaction Fees", "Competitive low rate", "1.75% standard", "DOJO"),
            ("Payout Speed", "Next working day", "1–2 business days", "DOJO"),
            ("Connectivity", "WiFi + automatic 4G backup", "WiFi / Bluetooth", "DOJO"),
            ("UK Phone Support", "24/7 UK-based support team", "Mon–Fri business hours", "DOJO"),
            ("Card Types", "Visa, Mastercard, Amex + all contactless", "Visa, Mastercard, Amex", "Tie"),
            ("Hardware Cost", "FREE card machine", "Reader from £29", "DOJO"),
            ("PayPal Integration", "Not available", "Full PayPal ecosystem", "Zettle"),
            ("Reporting & Analytics", "DOJO portal — business insights", "Zettle app dashboard", "Tie"),
            ("Suitable For", "UK hospitality, retail, trades, service businesses", "Businesses in the PayPal ecosystem", "Depends"),
        ],
    },
]

NAV = """<nav class="navbar navbar-expand-lg site-nav" id="top">
  <div class="container">
    <a class="navbar-brand nav-brand" href="/">Payment Card Services</a>
    <button class="navbar-toggler nav-burger" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
    <div class="collapse navbar-collapse" id="navMenu">
      <ul class="navbar-nav ms-auto align-items-lg-center gap-1">
        <li class="nav-item"><a class="nav-link" href="/#why">Why Choose Us</a></li>
        <li class="nav-item"><a class="nav-link" href="/#services">Our Services</a></li>
        <li class="nav-item"><a class="nav-link" href="/#about">About Us</a></li>
        <li class="nav-item"><a class="nav-link" href="/#how">How It Works</a></li>
        <li class="nav-item ms-lg-3 mt-3 mt-lg-0">
          <a href="#enquire" class="btn-nav">Get Free Card Machine</a>
        </li>
      </ul>
    </div>
  </div>
</nav>"""

HEAD_LINKS = """  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">"""

SCROLL_BTN = """<button id="scrollBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Scroll to top">
  <i class="fas fa-chevron-up"></i>
</button>"""

FOOTER = f"""<footer>
  <div class="container">
    <div class="row g-5 foot-top">
      <div class="col-lg-4">
        <div class="foot-logo">Payment Card<span> Services</span></div>
        <p class="foot-tagline">The smarter way to accept card payments — zero rental, next-day payouts, 24/7 UK support.</p>
      </div>
      <div class="col-sm-6 col-lg-2">
        <p class="foot-col-title">Quick Links</p>
        <ul class="foot-links">
          <li><a href="/">Home</a></li>
          <li><a href="/#why">Why Choose Us</a></li>
          <li><a href="/#services">Our Services</a></li>
          <li><a href="/#about">About Us</a></li>
          <li><a href="/#enquire">Get Started</a></li>
        </ul>
      </div>
      <div class="col-sm-6 col-lg-3">
        <p class="foot-col-title">Our Services</p>
        <ul class="foot-links">
          <li><a href="/#services">Card Machine — Point of Sale</a></li>
          <li><a href="/#services">Tap to Pay on iPhone</a></li>
          <li><a href="/#services">Dual Connectivity</a></li>
          <li><a href="/#services">DOJO App &amp; Portal</a></li>
          <li><a href="/#services">Payment Links</a></li>
        </ul>
      </div>
      <div class="col-sm-6 col-lg-3">
        <p class="foot-col-title">Contact</p>
        <div class="foot-contact-item"><i class="fas fa-map-marker-alt"></i><span>Eubank Consulting Limited,<br>166 College Road, Harrow, England, HA1 1BH</span></div>
        <div class="foot-contact-item"><i class="fas fa-envelope"></i><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></div>
        <div class="foot-contact-item mb-3"><i class="fas fa-shield-alt"></i><span>Authorised DOJO Consultant</span></div>
        <a href="#enquire" class="foot-cta-btn">Get Free Card Machine</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Payment Card Services. All rights reserved.</span>
      <div class="foot-legal"><a href="/">Privacy Policy</a><a href="/">Cookie Policy</a></div>
    </div>
  </div>
</footer>"""

JS = f"""<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script>
const FORMSPREE_ID = '{FORMSPREE_ID}';
document.getElementById('enquiryForm').addEventListener('submit', async function(e) {{
  e.preventDefault();
  const form=e.target, btn=document.getElementById('submitBtn'),
        btnText=document.getElementById('btnText'), spinner=document.getElementById('btnSpinner'),
        success=document.getElementById('enqSuccess'), error=document.getElementById('enqError');
  if (!form.checkValidity()) {{ form.reportValidity(); return; }}
  btn.disabled=true; btnText.style.display='none'; spinner.style.display='inline';
  success.style.display='none'; error.style.display='none';
  const name=form.querySelector('[name="full_name"]').value;
  try {{
    const res=await fetch('https://formspree.io/f/'+FORMSPREE_ID,{{
      method:'POST', headers:{{'Content-Type':'application/json',Accept:'application/json'}},
      body:JSON.stringify({{'Full Name':name,'Email':form.querySelector('[name="email"]').value,
        'Phone':form.querySelector('[name="phone"]').value,
        'Enquiry Type':form.querySelector('[name="enquiry_type"]').value||'Not specified',
        _replyto:form.querySelector('[name="email"]').value,
        _subject:'New card machine enquiry from '+name}})
    }});
    if(res.ok){{success.style.display='block';form.reset();}}
    else throw new Error();
  }} catch {{ error.style.display='block'; }}
  finally {{ btn.disabled=false; btnText.style.display='inline'; spinner.style.display='none'; }}
}});
const revealEls=document.querySelectorAll('.reveal');
const observer=new IntersectionObserver((entries)=>{{entries.forEach(entry=>{{if(entry.isIntersecting){{entry.target.classList.add('visible');observer.unobserve(entry.target);}}}});}},{{threshold:0.12}});
revealEls.forEach(el=>observer.observe(el));
const nav=document.querySelector('.site-nav');
window.addEventListener('scroll',()=>{{nav.classList.toggle('scrolled',window.scrollY>20);document.getElementById('scrollBtn').classList.toggle('show',window.scrollY>400);}});
document.querySelectorAll('a[href^="#"]').forEach(a=>{{a.addEventListener('click',function(e){{const t=document.querySelector(this.getAttribute('href'));if(t){{e.preventDefault();t.scrollIntoView({{behavior:'smooth',block:'start'}});}}}});}});
</script>"""

def enquiry_form():
    return f"""<section id="enquire" style="padding:60px 0;">
  <div class="container enq-inner">
    <div class="text-center mb-5 reveal">
      <h2 class="enq-heading">Get Your Free DOJO Card Machine</h2>
      <p class="enq-para">Zero monthly rental. Next-day payouts. 24/7 UK support. Fill in your details and we'll be in touch.</p>
    </div>
    <div class="row justify-content-center">
      <div class="col-lg-6 col-md-8 reveal">
        <div class="enq-card">
          <div id="enqSuccess" style="display:none;background:#e6f9f4;color:#012f27;padding:16px;border-radius:8px;margin-bottom:16px;font-weight:600;"><i class="fas fa-circle-check me-2"></i>Thank you! We'll be in touch very soon.</div>
          <div id="enqError" style="display:none;background:#fff0f0;color:#c00;padding:16px;border-radius:8px;margin-bottom:16px;font-weight:600;"><i class="fas fa-circle-exclamation me-2"></i>Something went wrong. Please try again.</div>
          <form id="enquiryForm" novalidate>
            <div class="row g-3">
              <div class="col-12"><label class="enq-label" for="enq-name">Full Name *</label><input type="text" class="enq-input" id="enq-name" name="full_name" placeholder="Your full name" required></div>
              <div class="col-sm-6"><label class="enq-label" for="enq-email">Email Address *</label><input type="email" class="enq-input" id="enq-email" name="email" placeholder="your@email.com" required></div>
              <div class="col-sm-6"><label class="enq-label" for="enq-phone">Phone Number *</label><input type="tel" class="enq-input" id="enq-phone" name="phone" placeholder="+44 7700 000000" required></div>
              <div class="col-12"><label class="enq-label" for="enq-type">Enquiry Type</label><select class="enq-select" id="enq-type" name="enquiry_type"><option value="" disabled selected>--- Please Select ---</option><option>Switching from SumUp</option><option>Switching from Square</option><option>Switching from Zettle</option><option>New Card Machine</option><option>General Enquiry</option></select></div>
            </div>
            <p class="enq-consent">By submitting this form, you agree that Payment Card Services will contact you by phone, SMS, and email about your enquiry. You can opt out at any time.</p>
            <button type="submit" class="btn-solid w-100" id="submitBtn">
              <span id="btnText"><i class="fas fa-paper-plane"></i> Get My Free Card Machine</span>
              <span id="btnSpinner" style="display:none"><i class="fas fa-spinner fa-spin me-2"></i>Sending…</span>
            </button>
            <p class="enq-privacy"><i class="fas fa-lock"></i>100% Privacy Guaranteed. No spam, ever.</p>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>"""

def row_winner_badge(winner, dojo_name, comp_name):
    if winner == "DOJO":
        return f'<span style="background:#e6f9f4;color:#012f27;padding:3px 10px;border-radius:20px;font-size:.78rem;font-weight:700;white-space:nowrap;">{dojo_name} ✓</span>'
    elif winner == comp_name:
        return f'<span style="background:#f0f4ff;color:#1a1a2e;padding:3px 10px;border-radius:20px;font-size:.78rem;font-weight:700;white-space:nowrap;">{comp_name} ✓</span>'
    else:
        return '<span style="background:#f8f9fa;color:#666;padding:3px 10px;border-radius:20px;font-size:.78rem;font-weight:700;white-space:nowrap;">Tie</span>'

def build_page(comp):
    slug = comp["slug"]; competitor = comp["competitor"]
    rows_html = ""
    for feature, dojo_val, comp_val, winner in comp["rows"]:
        badge = row_winner_badge(winner, "DOJO", competitor)
        dojo_strong = ' style="font-weight:600;color:var(--green);"' if winner == "DOJO" else ""
        rows_html += f"""<tr>
          <td style="font-weight:600;color:var(--green);">{feature}</td>
          <td{dojo_strong}>{dojo_val}</td>
          <td>{comp_val}</td>
          <td class="text-center">{badge}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{comp['title']}</title>
  <meta name="description" content="{comp['meta']}">
  <meta name="author" content="Payment Card Services">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#012f27">
  <link rel="canonical" href="{DOMAIN}/{slug}">
  <link rel="icon" type="image/png" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Payment Card Services">
  <meta property="og:title" content="{comp['title']}">
  <meta property="og:description" content="{comp['meta']}">
  <meta property="og:url" content="{DOMAIN}/{slug}">
  <style>
    .comp-table{{width:100%;border-collapse:collapse;margin-top:32px;}}
    .comp-table th{{background:var(--green);color:#fff;padding:12px 16px;font-size:.85rem;font-weight:600;text-align:left;}}
    .comp-table th:last-child{{text-align:center;}}
    .comp-table td{{padding:12px 16px;border-bottom:1px solid var(--border);font-size:.9rem;vertical-align:middle;}}
    .comp-table tr:last-child td{{border-bottom:none;}}
    .comp-table tr:nth-child(even){{background:var(--light);}}
    .verdict-box{{background:linear-gradient(135deg,#012f27,#024a3e);color:#fff;border-radius:16px;padding:32px;margin-top:40px;}}
    .verdict-box h4{{color:#2fcfae;font-weight:700;margin-bottom:12px;}}
    @media(max-width:768px){{.comp-table{{display:block;overflow-x:auto;white-space:normal;}}}}
  </style>
{HEAD_LINKS}
</head>
<body>
{NAV}
<section id="hero" style="padding:80px 0 40px;">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-9 text-center reveal">
        <span class="sec-badge">COMPARISON</span>
        <h1 class="hero-title" style="margin-top:16px;">DOJO vs {competitor}<br><span class="grad">Side by Side</span></h1>
        <p class="hero-sub" style="max-width:680px;margin:20px auto 0;">{comp['intro']}</p>
      </div>
    </div>
  </div>
</section>
<section style="padding:20px 0 60px;">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-10 reveal">
        <div style="overflow-x:auto;">
          <table class="comp-table">
            <thead>
              <tr>
                <th>Feature</th>
                <th><i class="fas fa-bolt me-1"></i>DOJO (via Payment Card Services)</th>
                <th>{competitor}</th>
                <th style="text-align:center;">Winner</th>
              </tr>
            </thead>
            <tbody>
              {rows_html}
            </tbody>
          </table>
        </div>
        <div class="verdict-box reveal">
          <h4><i class="fas fa-trophy me-2"></i>Our Verdict: {comp['verdict']} Wins</h4>
          <p style="margin:0;line-height:1.7;color:rgba(255,255,255,.85);">{comp['verdict_reason']}</p>
          <div class="mt-4"><a href="#enquire" class="btn-solid">Get Your Free DOJO Card Machine <i class="fas fa-arrow-right"></i></a></div>
        </div>
      </div>
    </div>
  </div>
</section>
{enquiry_form()}
{FOOTER}
{SCROLL_BTN}
{JS}
</body>
</html>"""

def main():
    count = 0
    for comp in COMPARISONS:
        fname = f"{comp['slug']}.html"
        with open(os.path.join(BASE_DIR, fname), "w", encoding="utf-8") as f:
            f.write(build_page(comp))
        print(f"  Created: {fname}"); count += 1
    print(f"\nDone — {count} comparison pages generated.")
    print("\nSitemap entries:")
    for comp in COMPARISONS:
        print(f'  <url><loc>{DOMAIN}/{comp["slug"]}</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>')

if __name__ == "__main__":
    main()
