"""Generate city x industry combination pages."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

CITIES = [
    {"city":"Manchester","slug":"manchester","region":"Greater Manchester"},
    {"city":"Birmingham","slug":"birmingham","region":"West Midlands"},
    {"city":"Leeds","slug":"leeds","region":"West Yorkshire"},
    {"city":"Bristol","slug":"bristol","region":"South West England"},
    {"city":"Glasgow","slug":"glasgow","region":"Scotland"},
    {"city":"Edinburgh","slug":"edinburgh","region":"Scotland"},
    {"city":"Liverpool","slug":"liverpool","region":"Merseyside"},
    {"city":"Sheffield","slug":"sheffield","region":"South Yorkshire"},
    {"city":"Newcastle","slug":"newcastle","region":"Tyne and Wear"},
    {"city":"Nottingham","slug":"nottingham","region":"East Midlands"},
    {"city":"Leicester","slug":"leicester","region":"East Midlands"},
    {"city":"Brighton","slug":"brighton","region":"East Sussex"},
    {"city":"Cardiff","slug":"cardiff","region":"Wales"},
    {"city":"Southampton","slug":"southampton","region":"Hampshire"},
    {"city":"Reading","slug":"reading","region":"Berkshire"},
    {"city":"Coventry","slug":"coventry","region":"West Midlands"},
    {"city":"Oxford","slug":"oxford","region":"Oxfordshire"},
    {"city":"Cambridge","slug":"cambridge","region":"Cambridgeshire"},
    {"city":"London","slug":"london","region":"Greater London"},
    {"city":"Milton Keynes","slug":"milton-keynes","region":"Buckinghamshire"},
]

INDUSTRIES = [
    {"industry":"Restaurants","slug":"restaurants","icon":"fas fa-utensils","desc":"In {city}'s competitive restaurant sector, card payments make up the vast majority of covers — customers expect to pay by card or contactless, and a card machine that's slow, unreliable, or expensive is a direct drag on table turnover and margins.","pain":"Monthly rental fees quietly add up. A zero-rental card machine means your {city} restaurant keeps more of every order."},
    {"industry":"Bars & Pubs","slug":"bars-and-pubs","icon":"fas fa-beer","desc":"{city}'s bar and pub scene runs at high transaction volumes — particularly on weekends when queues at the bar can't afford payment terminal delays. A reliable, fast card machine is as fundamental to a {city} bar as a cold tap.","pain":"For busy {city} bars, slow terminals and monthly rental fees are both problems. Switch to zero-rental and take every payment faster."},
    {"industry":"Hair Salons","slug":"hair-salons","icon":"fas fa-cut","desc":"{city}'s hair salons take card payments for the majority of their clients. A card machine that works reliably, connects via both WiFi and 4G backup, and doesn't come with a monthly rental fee is the obvious choice for any well-run salon.","pain":"Hair salons in {city} often pay £20–£40 a month just to rent their card machine. That's money you can eliminate from your overheads today."},
    {"industry":"Beauty Salons","slug":"beauty-salons","icon":"fas fa-spa","desc":"{city}'s beauty salons serve a clientele that expects seamless, premium service — including at checkout. A card machine that always works, pays out the next day, and carries no monthly rental fee is the professional choice for {city} beauty businesses.","pain":"Monthly rental fees are a fixed overhead that {city}'s beauty salons can do without. A DOJO card machine delivers better service at zero monthly cost."},
    {"industry":"Retail Shops","slug":"retail-shops","icon":"fas fa-shopping-bag","desc":"Retail businesses across {city} have shifted decisively to card-first trading. Whether you run an independent boutique, a specialist shop, or a larger retail outlet, reliable card payment infrastructure is non-negotiable — and unnecessary monthly rental fees are one of the easiest costs to cut.","pain":"For {city} retailers, a monthly rental fee on a card machine is a cost that doesn't need to exist. Zero-rental alternatives deliver the same functionality at lower total cost."},
    {"industry":"Takeaways","slug":"takeaways","icon":"fas fa-hamburger","desc":"{city}'s takeaway and fast food sector processes enormous card payment volumes, particularly during evening peaks. Speed matters — customers at the counter don't wait — and a reliable card machine with dual WiFi and 4G connectivity ensures every order goes through first time.","pain":"Takeaways in {city} are high-volume, margin-sensitive businesses. Cutting monthly card machine rental fees is a straightforward improvement to your bottom line."},
    {"industry":"Cafes","slug":"cafes","icon":"fas fa-coffee","desc":"Independent cafes across {city} live and die by their throughput in the morning rush. A card machine that processes contactless payments instantly, connects via WiFi with 4G backup, and costs nothing to rent every month is the clear choice for {city}'s coffee-first café culture.","pain":"{city} cafes are squeezed on margins. Monthly card machine rental fees are an overhead you can eliminate without compromising on reliability."},
    {"industry":"Tradespeople","slug":"tradespeople","icon":"fas fa-tools","desc":"Plumbers, electricians, builders, and other tradespeople working across {city} need a card machine that goes where they go. Dual WiFi and 4G connectivity means payment works on any site, and zero rental means the card machine pays for itself from the very first transaction.","pain":"Mobile tradespeople in {city} who are still carrying a rented card machine are paying every month for something they could own for free."},
    {"industry":"Barbershops","slug":"barbershops","icon":"fas fa-user-alt","desc":"{city}'s barbershops have embraced card payments — most customers no longer carry cash, and barbershops that only accept cash are limiting their client base. A zero-rental card machine with fast connectivity is the straightforward upgrade for {city} barbershops ready to operate fully cashless.","pain":"Barbershops in {city} paying monthly rental on their card machines are spending money they don't need to. The zero-rental alternative is the same quality at zero fixed overhead."},
    {"industry":"Gyms & Fitness","slug":"gyms-and-fitness","icon":"fas fa-dumbbell","desc":"Gyms and personal training businesses across {city} take card payments for memberships, sessions, and retail — often in multiple locations or on the move. A card machine that works everywhere, pays out the next day, and carries no monthly rental is the obvious choice for {city}'s fitness sector.","pain":"Fitness businesses in {city} paying monthly rental fees on card machines are carrying a cost that a zero-rental DOJO setup eliminates from day one."},
    {"industry":"Market Stalls","slug":"market-stalls","icon":"fas fa-store","desc":"{city}'s markets attract thousands of customers who increasingly prefer to pay by card. Stall holders who can't take card payments are losing sales to the next stall that can. A portable DOJO card machine with built-in 4G means you take payments anywhere on the market, with no monthly rental eating into margins.","pain":"For {city} market traders, monthly card machine rental fees are particularly harmful to already-tight margins. Zero-rental is the standard you should be operating to."},
    {"industry":"Hotels & B&Bs","slug":"hotels-and-bbs","icon":"fas fa-bed","desc":"Hotels and B&Bs in {city} take card payments at check-in, at the bar, and for ancillary services. Reliable payment infrastructure that processes cards quickly, pays out the next day, and costs nothing in monthly rental is a straightforward operational win for {city}'s accommodation sector.","pain":"{city} accommodation businesses paying monthly rental on card machines are carrying a fixed overhead. Switch to zero-rental and redirect that spend back into your property."},
    {"industry":"Mechanics & Garages","slug":"mechanics-and-garages","icon":"fas fa-car","desc":"Vehicle repair businesses across {city} handle high-value transactions — and customers paying for a £400 service expect a professional card payment experience. Dual WiFi and 4G connectivity means the card machine works whether you're at the counter or on the forecourt.","pain":"Mechanics and garages in {city} on monthly rental contracts for their card machines are paying a fixed fee that zero-rental alternatives have made unnecessary."},
    {"industry":"Florists","slug":"florists","icon":"fas fa-leaf","desc":"Florists across {city} process card payments for everyday purchases and the high-value orders — weddings, events, corporate accounts — that make up a significant proportion of revenue. A card machine that works reliably, pays out the next day, and carries no monthly rental fee is essential for {city}'s floral businesses.","pain":"A monthly card machine rental fee is a fixed cost that {city} florists can eliminate without any reduction in payment capability. Zero-rental is simply better value."},
    {"industry":"Cleaning Services","slug":"cleaning-services","icon":"fas fa-broom","desc":"Cleaning businesses operating across {city} — commercial cleaners, domestic cleaners, specialist services — typically take payment at the end of each job. A portable card machine with 4G connectivity means you take payment on-site, and zero monthly rental means every job's margin is clean.","pain":"Cleaning businesses in {city} with monthly card machine rental fees are carrying a cost that's easy to remove. DOJO's zero-rental model is designed for exactly this kind of mobile service business."},
    {"industry":"Tattoo Studios","slug":"tattoo-studios","icon":"fas fa-paint-brush","desc":"Tattoo studios across {city} deal in high-value, single-session transactions where payment reliability is non-negotiable. A card machine that always connects, processes instantly, and pays out the next working day is the standard that {city}'s professional tattoo studios should be operating to.","pain":"Monthly card machine rental fees are an overhead that {city} tattoo studios can eliminate. The zero-rental DOJO model delivers the same professional payment experience without the fixed monthly cost."},
    {"industry":"Vets","slug":"vets","icon":"fas fa-paw","desc":"Veterinary practices across {city} handle significant transaction values — especially for emergency treatments and surgery — where card payment reliability is critical. Next-day payouts and 24/7 UK support mean payment infrastructure never gets in the way of what matters most.","pain":"Vet practices in {city} paying monthly rental on card machines are carrying a cost that a zero-rental DOJO setup removes immediately and permanently."},
    {"industry":"Dentists","slug":"dentists","icon":"fas fa-tooth","desc":"Dental practices across {city} take card payments for both NHS charges and significant private treatment costs. A card machine that processes quickly at reception, pays out the next day, and carries no monthly rental is the obvious operational choice for {city}'s dental sector.","pain":"Monthly card machine rental fees are an unnecessary fixed overhead for {city} dental practices. Zero-rental alternatives deliver identical functionality without the monthly charge."},
    {"industry":"Estate Agents","slug":"estate-agents","icon":"fas fa-home","desc":"Estate agents across {city} take card payments for holding deposits, application fees, and other charges. A zero-rental card machine with next-day payouts and 24/7 UK support is the right infrastructure for a professional services environment where every transaction matters.","pain":"{city} estate agents on monthly rental contracts for their card machines are paying more than they need to. A zero-rental DOJO card machine is the straightforward switch."},
    {"industry":"Off-Licences","slug":"off-licences","icon":"fas fa-wine-bottle","desc":"Off-licences and independent alcohol retailers across {city} process high volumes of card payments throughout the day and into the evening. Fast, reliable contactless payment infrastructure is essential — and monthly rental fees on card machines are a cost that {city}'s independent alcohol retailers are increasingly unwilling to carry.","pain":"Off-licences in {city} pay for every transaction already in their rate. A monthly rental fee on top is a cost that zero-rental eliminates."},
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

STATS_BAR = """<div class="stats-bar">
  <div class="container">
    <div class="d-flex justify-content-center align-items-center flex-wrap gap-0">
      <div class="stats-item reveal reveal-delay-1"><div class="stats-num">0%</div><div class="stats-lbl">Monthly Rental</div></div>
      <div class="stats-divider d-none d-sm-block"></div>
      <div class="stats-item reveal reveal-delay-2"><div class="stats-num">FREE</div><div class="stats-lbl">Card Machine</div></div>
      <div class="stats-divider d-none d-sm-block"></div>
      <div class="stats-item reveal reveal-delay-3"><div class="stats-num">1-Day</div><div class="stats-lbl">Fast Payouts</div></div>
      <div class="stats-divider d-none d-sm-block"></div>
      <div class="stats-item reveal reveal-delay-4"><div class="stats-num">24/7</div><div class="stats-lbl">UK Support</div></div>
    </div>
  </div>
</div>"""

WHY_CARDS = """<section id="why" style="padding:60px 0;">
  <div class="container">
    <div class="text-center mb-5 reveal">
      <span class="sec-badge">WHY CHOOSE US</span>
      <h2 class="sec-title sec-grad">Smart Payments.<br>Built For Growth.</h2>
      <div class="teal-bar"></div>
    </div>
    <div class="row g-4">
      <div class="col-sm-6 col-lg-3 reveal reveal-delay-1">
        <div class="why-card"><div class="why-icon"><i class="fas fa-tag"></i></div><h5>No Rental, No Risk</h5><p>Zero fixed monthly fees — you pay only a small percentage per transaction.</p></div>
      </div>
      <div class="col-sm-6 col-lg-3 reveal reveal-delay-2">
        <div class="why-card"><div class="why-icon"><i class="fas fa-bolt"></i></div><h5>Next Day Payouts</h5><p>Get your money the next working day, including weekends — no waiting.</p></div>
      </div>
      <div class="col-sm-6 col-lg-3 reveal reveal-delay-3">
        <div class="why-card"><div class="why-icon"><i class="fas fa-wifi"></i></div><h5>Always Connected</h5><p>WiFi with automatic 4G SIM backup so you never miss a payment.</p></div>
      </div>
      <div class="col-sm-6 col-lg-3 reveal reveal-delay-4">
        <div class="why-card"><div class="why-icon"><i class="fas fa-headset"></i></div><h5>24/7 UK Support</h5><p>Real UK support teams available around the clock, day or night.</p></div>
      </div>
    </div>
  </div>
</section>"""

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
      <h2 class="enq-heading">Get Your Free Card Machine Today</h2>
      <p class="enq-para">Fill in your details and we'll be in touch to confirm your free DOJO card machine with no monthly rental.</p>
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
              <div class="col-12"><label class="enq-label" for="enq-type">Enquiry Type</label><select class="enq-select" id="enq-type" name="enquiry_type"><option value="" disabled selected>--- Please Select ---</option><option>New Card Machine</option><option>Switching Provider</option><option>Multiple Machines</option><option>General Enquiry</option></select></div>
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

def build_page(city_data, ind_data):
    city = city_data["city"]; city_slug = city_data["slug"]
    industry = ind_data["industry"]; ind_slug = ind_data["slug"]
    icon = ind_data["icon"]
    desc = ind_data["desc"].replace("{city}", city)
    pain = ind_data["pain"].replace("{city}", city)
    url_slug = f"free-card-machine-for-{ind_slug}-in-{city_slug}"
    title = f"Free Card Machine for {industry} in {city} | No Rental | Payment Card Services"
    meta_desc = f"Free DOJO card machine for {industry.lower()} in {city} — no monthly rental fee, next-day payouts, 24/7 UK support. Claim yours today."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="card machine {industry.lower()} {city}, free card machine {city}, DOJO {industry.lower()} {city}, merchant services {industry.lower()} {city}, contactless payments {city}">
  <meta name="author" content="Payment Card Services">
  <meta name="robots" content="index, follow">
  <meta name="geo.region" content="GB">
  <meta name="geo.placename" content="{city}">
  <meta name="theme-color" content="#012f27">
  <link rel="canonical" href="{DOMAIN}/{url_slug}">
  <link rel="icon" type="image/png" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Payment Card Services">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{DOMAIN}/{url_slug}">
  <meta property="og:image" content="{DOMAIN}/images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FinancialService","name":"Payment Card Services — {industry} in {city}","description":"Free DOJO card machines for {industry.lower()} in {city} with no monthly rental charges.","url":"{DOMAIN}/{url_slug}","email":"{EMAIL}","areaServed":{{"@type":"City","name":"{city}","addressCountry":"GB"}},"address":{{"@type":"PostalAddress","streetAddress":"166 College Road","addressLocality":"Harrow","addressRegion":"England","postalCode":"HA1 1BH","addressCountry":"GB"}}}}
  </script>
{HEAD_LINKS}
</head>
<body>
{NAV}
<section id="hero">
  <div class="container hero-inner">
    <div class="row align-items-center g-5">
      <div class="col-lg-7">
        <div class="reveal from-left">
          <p style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#2fcfae;margin-bottom:12px;">{industry.upper()} · {city.upper()}</p>
          <h1 class="hero-title">Free Card Machine for<br><span class="grad">{industry} in {city}</span></h1>
          <div class="hero-img-mobile d-lg-none"><img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {industry} in {city}"></div>
          <p class="hero-sub">No monthly rental. No long contracts. Just a free DOJO card machine and a simple per-transaction rate — helping {city}'s {industry.lower()} businesses keep more of every sale.</p>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Zero Monthly Rental Fee</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Next-Day Payouts</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Dual WiFi + 4G Connectivity</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>24/7 UK Support</div>
          <div class="mt-4"><a href="#enquire" class="btn-solid">Get Your FREE Card Machine <i class="fas fa-arrow-right"></i></a></div>
        </div>
      </div>
      <div class="col-lg-5 d-none d-lg-block">
        <div class="hero-img-card reveal from-right"><img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {industry} in {city}"></div>
      </div>
    </div>
  </div>
</section>
{STATS_BAR}
<section style="padding:60px 0;background:var(--light);">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-7 reveal from-left">
        <span class="sec-badge"><i class="{icon} me-2"></i>{industry.upper()} IN {city.upper()}</span>
        <h2 class="sec-title" style="margin-top:12px;">{city} {industry}:<br><span class="sec-grad">The Smart Payment Choice</span></h2>
        <div class="teal-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;line-height:1.8;margin-top:20px;">{desc}</p>
      </div>
      <div class="col-lg-5 reveal from-right">
        <div style="background:#fff;border:2px solid var(--teal);border-radius:12px;padding:28px;">
          <div style="font-size:2rem;color:var(--teal);margin-bottom:12px;"><i class="{icon}"></i></div>
          <h5 style="font-weight:700;color:var(--green);margin-bottom:12px;">The Bottom Line</h5>
          <p style="color:var(--muted);line-height:1.7;font-size:.95rem;">{pain}</p>
          <a href="#enquire" class="btn-solid mt-3" style="width:100%;justify-content:center;">Claim Free Card Machine <i class="fas fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>
{WHY_CARDS}
{enquiry_form()}
{FOOTER}
{SCROLL_BTN}
{JS}
</body>
</html>"""

def main():
    count = 0; slugs = []
    for city_data in CITIES:
        for ind_data in INDUSTRIES:
            fname = f"free-card-machine-for-{ind_data['slug']}-in-{city_data['slug']}.html"
            with open(os.path.join(BASE_DIR, fname), "w", encoding="utf-8") as f:
                f.write(build_page(city_data, ind_data))
            slugs.append((city_data["slug"], ind_data["slug"])); count += 1
    print(f"Done — {count} combo pages generated.")
    print("\nSitemap entries:")
    for (c, i) in slugs:
        print(f'  <url><loc>{DOMAIN}/free-card-machine-for-{i}-in-{c}</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>')

if __name__ == "__main__":
    main()
