"""Generate 25 new UK town/city location pages."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

NEW_TOWNS = [
    {"slug":"wolverhampton","city":"Wolverhampton","postcode":"WV1","region":"West Midlands","desc":"Wolverhampton's city centre regeneration, strong retail core, and busy hospitality sector all depend on reliable card payment infrastructure. From the Mander Centre's retail units to the city's growing independent restaurant and bar scene, card payments dominate. Businesses across the city that are still paying monthly card machine rental fees are carrying an unnecessary cost — one that directly affects what they keep from every transaction.","industries":["Restaurants & Bars","Independent Retail","Tradespeople","Hair & Beauty","Market Traders"]},
    {"slug":"stoke-on-trent","city":"Stoke-on-Trent","postcode":"ST1","region":"Staffordshire","desc":"Stoke-on-Trent's manufacturing heritage and growing independent business community make it one of the Midlands' most commercially active cities. From Hanley's retail and hospitality sector to the city's strong trades community serving the surrounding area, card payments are the norm. For Stoke businesses still on monthly rental contracts for their card machines, a zero-rental alternative is available and straightforward to switch to.","industries":["Retail","Restaurants & Cafes","Tradespeople","Hair & Beauty","Manufacturing & Trade"]},
    {"slug":"plymouth","city":"Plymouth","postcode":"PL1","region":"Devon","desc":"Plymouth's maritime economy, student population, and growing hospitality sector all run on card payments. From the Barbican's restaurants and bars to the city centre's retail and the busy trades sector serving Devon's housing market, contactless payments are the default. Plymouth businesses paying monthly rental fees on card machines are paying more than they need to — a free alternative with better features exists.","industries":["Restaurants & Bars","Retail","Hair & Beauty","Tradespeople","Hotels & Guesthouses"]},
    {"slug":"derby","city":"Derby","postcode":"DE1","region":"Derbyshire","desc":"Derby's engineering heritage and modern business community span manufacturing, retail, and hospitality — all sectors where card payments are fundamental. From the Cathedral Quarter's independent businesses to the city's busy trades and services sector, Derby businesses process card payments every day. Those still paying monthly rental fees are carrying a cost that a zero-rental DOJO card machine would immediately eliminate.","industries":["Restaurants & Cafes","Retail","Tradespeople","Hair & Beauty","Engineering & Trade"]},
    {"slug":"sunderland","city":"Sunderland","postcode":"SR1","region":"Tyne and Wear","desc":"Sunderland's retail sector, hospitality industry, and active trades community all rely on card payment infrastructure. As the city continues its regeneration, businesses across the centre and surrounding areas are moving decisively towards cashless trading. For Sunderland businesses still paying a monthly rental fee on their card machines, switching to a zero-rental model is one of the most straightforward cost savings available.","industries":["Retail","Restaurants & Bars","Hair & Beauty","Tradespeople","Market Traders"]},
    {"slug":"luton","city":"Luton","postcode":"LU1","region":"Bedfordshire","desc":"Luton's proximity to London, its airport economy, and its diverse and growing business community make it one of the South East's busiest commercial environments outside the capital. From the town centre's retail and hospitality sector to the busy trades and services businesses serving the surrounding area, card payments are constant. Monthly card machine rental fees are a cost that Luton businesses can and should eliminate.","industries":["Restaurants & Takeaways","Retail","Hair & Beauty","Tradespeople","Airport & Travel Services"]},
    {"slug":"huddersfield","city":"Huddersfield","postcode":"HD1","region":"West Yorkshire","desc":"Huddersfield's independent business scene — from the Packhorse Centre's retail to the town's strong hospitality offering and the wider trades sector — processes card payments all day, every day. For Huddersfield businesses, the shift to cashless trading is complete; what hasn't happened for many is a review of the cost of accepting those payments, including the monthly rental fees that are quietly running on their card machines.","industries":["Restaurants & Cafes","Independent Retail","Tradespeople","Hair & Beauty","Market Traders"]},
    {"slug":"doncaster","city":"Doncaster","postcode":"DN1","region":"South Yorkshire","desc":"Doncaster's retail, hospitality, and trades sectors all depend on card payment infrastructure that works reliably and costs as little as possible. From the Frenchgate Shopping Centre's retailers to the town's growing food and drink scene and the busy trades businesses serving South Yorkshire, card payments are non-negotiable. A monthly rental fee on a card machine is a fixed cost that Doncaster business owners can eliminate today.","industries":["Retail","Restaurants & Bars","Tradespeople","Hair & Beauty","Market Traders"]},
    {"slug":"bolton","city":"Bolton","postcode":"BL1","region":"Greater Manchester","desc":"Bolton's retail core, active hospitality sector, and strong trades community all process card payments throughout their trading hours. As Greater Manchester's economy continues to grow outward from the city centre, Bolton businesses are increasingly part of a cashless trading environment. Many are still paying monthly rental fees on card machines set up years ago — switching to zero rental is a fast, straightforward improvement.","industries":["Retail","Restaurants & Cafes","Hair & Beauty","Tradespeople","Market Stalls"]},
    {"slug":"swansea","city":"Swansea","postcode":"SA1","region":"Wales","desc":"Swansea's retail sector, University campus economy, and hospitality industry all depend on reliable card payment infrastructure. From the city centre's shops and restaurants to the growing Marina development and the trades sector serving West Wales, card payments dominate. Welsh businesses in Swansea still paying monthly rental fees on card machines are carrying a cost their counterparts in the rest of the UK are eliminating.","industries":["Restaurants & Bars","Retail","Hair & Beauty","Tradespeople","Student-Facing Businesses"]},
    {"slug":"northampton","city":"Northampton","postcode":"NN1","region":"Northamptonshire","desc":"Northampton's logistics hub, retail sector, and growing hospitality scene make it one of the East Midlands' most commercially active towns. Businesses from the town centre to the surrounding business parks process card payments constantly. For Northampton businesses on monthly rental contracts for their card machines, a zero-rental alternative with next-day payouts and 24/7 UK support is a straightforward step forward.","industries":["Retail","Restaurants & Cafes","Tradespeople","Hair & Beauty","Logistics & Trade"]},
    {"slug":"norwich","city":"Norwich","postcode":"NR1","region":"Norfolk","desc":"Norwich's thriving independent business community — from the Lanes' boutiques and restaurants to the Castle Quarter's shops and the city's strong hospitality scene — is one of the most distinctive in the East of England. Norwich businesses pride themselves on running lean, smart operations, and an unnecessary monthly rental fee on a card machine is exactly the kind of cost that well-run Norwich businesses cut first.","industries":["Independent Retail","Restaurants & Bars","Hair & Beauty","Tradespeople","Hotels & B&Bs"]},
    {"slug":"exeter","city":"Exeter","postcode":"EX1","region":"Devon","desc":"Exeter's university economy, strong tourism sector, and growing independent business community all run on card payments. From the Cathedral Quarter's restaurants and shops to the Quay's hospitality venues and the surrounding Devon trades sector, card payments are the default. Exeter businesses paying monthly rental on card machines are carrying a cost they could eliminate today without any reduction in service or functionality.","industries":["Restaurants & Cafes","Independent Retail","Hotels & B&Bs","Tradespeople","Hair & Beauty"]},
    {"slug":"peterborough","city":"Peterborough","postcode":"PE1","region":"Cambridgeshire","desc":"Peterborough's fast-growing economy — driven by its logistics sector, retail core, and expanding hospitality scene — processes high volumes of card payments every day. As one of the UK's fastest-growing cities, Peterborough businesses are building from scratch in many cases and need payment infrastructure that's cost-effective from day one. A zero-rental DOJO card machine is the obvious choice.","industries":["Retail","Restaurants & Takeaways","Tradespeople","Hair & Beauty","Logistics & Trade"]},
    {"slug":"portsmouth","city":"Portsmouth","postcode":"PO1","region":"Hampshire","desc":"Portsmouth's naval heritage, tourism economy, and vibrant Southsea independent business community all depend on card payments. From Gunwharf Quays' retail and hospitality to the city centre's shops and the busy trades sector serving Hampshire's housing market, card payments are constant. Portsmouth businesses paying monthly rental fees on card machines are paying a cost that doesn't need to exist.","industries":["Restaurants & Bars","Retail","Hair & Beauty","Tradespeople","Hotels & Guesthouses"]},
    {"slug":"swindon","city":"Swindon","postcode":"SN1","region":"Wiltshire","desc":"Swindon's corporate business community, retail sector, and growing independent food and hospitality scene all process card payments throughout the day. As one of the South West's major commercial centres, Swindon businesses are familiar with cutting unnecessary overhead. A monthly card machine rental fee is an avoidable fixed cost — one that a zero-rental DOJO setup eliminates from day one.","industries":["Retail","Restaurants & Cafes","Hair & Beauty","Tradespeople","Corporate Services"]},
    {"slug":"york","city":"York","postcode":"YO1","region":"North Yorkshire","desc":"York is one of the UK's most tourism-intensive cities, with a retail and hospitality sector that runs at extraordinary volume relative to the city's size. From the Shambles' boutiques to Micklegate's bars and the city's outstanding restaurant scene, York businesses process card payments at a relentless pace. Monthly rental fees on card machines are a particularly acute overhead for York's independent operators who need every margin they can protect.","industries":["Restaurants & Bars","Independent Retail","Hotels & B&Bs","Hair & Beauty","Tour & Visitor Services"]},
    {"slug":"hull","city":"Hull","postcode":"HU1","region":"East Yorkshire","desc":"Hull's regeneration, growing independent business community, and strong hospitality and retail sectors all depend on reliable card payment infrastructure. From the Old Town's bars and restaurants to the city centre's shops and the busy trades sector serving the surrounding East Yorkshire area, card payments are fundamental. Hull businesses still paying monthly rental fees on card machines are carrying a cost worth eliminating now.","industries":["Restaurants & Bars","Retail","Hair & Beauty","Tradespeople","Market Traders"]},
    {"slug":"middlesbrough","city":"Middlesbrough","postcode":"TS1","region":"Teesside","desc":"Middlesbrough's retail core, hospitality sector, and strong trades community across Teesside all process card payments throughout the day. As the Tees Valley economy grows, Middlesbrough businesses need payment infrastructure that's reliable and cost-effective. Monthly card machine rental fees are a fixed overhead that zero-rental DOJO machines eliminate — keeping more of every transaction inside your business.","industries":["Retail","Restaurants & Cafes","Hair & Beauty","Tradespeople","Market Traders"]},
    {"slug":"blackpool","city":"Blackpool","postcode":"FY1","region":"Lancashire","desc":"Blackpool's tourism economy runs at extraordinary intensity during peak season — and the hospitality, retail, and entertainment businesses that serve it process enormous card payment volumes. From the Promenade's hotels and restaurants to the town's retail sector and amusement venues, card payments never stop. For Blackpool businesses on monthly rental contracts, cutting that fixed cost with a zero-rental alternative is an immediate improvement to margins.","industries":["Hotels & B&Bs","Restaurants & Takeaways","Retail","Amusements & Entertainment","Hair & Beauty"]},
    {"slug":"ipswich","city":"Ipswich","postcode":"IP1","region":"Suffolk","desc":"Ipswich's waterfront regeneration, growing independent business community, and strong retail and hospitality sectors all run on card payments. From the Waterfront's restaurants and bars to the town centre's retail and the trades sector serving the surrounding Suffolk area, contactless payments are the norm. Ipswich businesses paying monthly rental fees on card machines are paying more than they need to for a service a zero-rental alternative delivers just as well.","industries":["Restaurants & Bars","Independent Retail","Hair & Beauty","Tradespeople","Hotels & B&Bs"]},
    {"slug":"gloucester","city":"Gloucester","postcode":"GL1","region":"Gloucestershire","desc":"Gloucester's historic city centre, growing retail sector, and active hospitality scene all process card payments throughout the day. From the Westgate Street independent retailers to the Docks' restaurants and bars, card payments dominate. Gloucester businesses carrying unnecessary monthly rental fees on card machines are paying a fixed cost that a DOJO zero-rental setup would immediately remove from their overheads.","industries":["Independent Retail","Restaurants & Cafes","Hair & Beauty","Tradespeople","Hotels & B&Bs"]},
    {"slug":"worcester","city":"Worcester","postcode":"WR1","region":"Worcestershire","desc":"Worcester's independent retail and hospitality community — from the High Street's boutiques and restaurants to Friar Street's bars and cafes — runs on card payments. As a cathedral city with strong tourism and a busy student economy, Worcester's businesses serve a cashless customer base year-round. Monthly rental fees on card machines are a fixed overhead that many Worcester businesses are still paying without realising there's a zero-rental alternative.","industries":["Independent Retail","Restaurants & Cafes","Hair & Beauty","Tradespeople","Hotels & B&Bs"]},
    {"slug":"chelmsford","city":"Chelmsford","postcode":"CM1","region":"Essex","desc":"Chelmsford's professional commuter population, active retail sector, and growing food and drink scene make it one of Essex's most commercially active cities. Businesses across the city centre and surrounding areas process high card payment volumes from a cashless, card-first customer base. Monthly rental fees on card machines are a fixed overhead that Chelmsford's business community — known for commercial efficiency — should be the first to eliminate.","industries":["Retail","Restaurants & Bars","Hair & Beauty","Tradespeople","Professional Services"]},
    {"slug":"basildon","city":"Basildon","postcode":"SS14","region":"Essex","desc":"Basildon's retail parks, town centre, and active independent business community process high volumes of card payments every day. From the Festival Leisure Park's hospitality venues to the town centre's retail and the trades sector serving the wider Essex area, card payments are the default. Basildon businesses on monthly rental contracts for their card machines are carrying a cost that a zero-rental DOJO alternative would immediately and permanently reduce.","industries":["Retail","Restaurants & Takeaways","Hair & Beauty","Tradespeople","Market Traders"]},
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

def build_page(loc):
    city = loc["city"]; slug = loc["slug"]; postcode = loc["postcode"]
    region = loc["region"]; desc = loc["desc"]; industries = loc["industries"]
    ind_html = "".join(f'<span class="area-pill-teal"><i class="fas fa-check-circle me-1"></i>{i}</span>' for i in industries)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Card Machine {city} | No Monthly Rental | Payment Card Services</title>
  <meta name="description" content="Get a FREE DOJO card machine for your {city} business — no monthly rental, just a simple transaction rate. Next-day payouts, 24/7 UK support. Claim yours today.">
  <meta name="keywords" content="free card machine {city}, card machine {city}, DOJO card machine {city}, no rental card machine {city}, merchant services {city}, contactless payments {city}">
  <meta name="author" content="Payment Card Services">
  <meta name="robots" content="index, follow">
  <meta name="geo.region" content="GB">
  <meta name="geo.placename" content="{city}">
  <meta name="theme-color" content="#012f27">
  <link rel="canonical" href="{DOMAIN}/free-card-machine-{slug}">
  <link rel="icon" type="image/png" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <link rel="apple-touch-icon" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Payment Card Services">
  <meta property="og:title" content="Free Card Machine {city} | No Monthly Rental | Payment Card Services">
  <meta property="og:description" content="Free DOJO card machine for {city} businesses — no monthly rental. Next-day payouts, dual connectivity, 24/7 UK support.">
  <meta property="og:url" content="{DOMAIN}/free-card-machine-{slug}">
  <meta property="og:image" content="{DOMAIN}/images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FinancialService","name":"Payment Card Services — {city}","description":"Free DOJO card machines for businesses in {city} with no monthly rental charges.","url":"{DOMAIN}/free-card-machine-{slug}","email":"{EMAIL}","areaServed":{{"@type":"City","name":"{city}","postalCode":"{postcode}","addressCountry":"GB"}},"address":{{"@type":"PostalAddress","streetAddress":"166 College Road","addressLocality":"Harrow","addressRegion":"England","postalCode":"HA1 1BH","addressCountry":"GB"}}}}
  </script>
  <style>.area-pill-teal{{display:inline-block;background:#e6f9f4;border:1px solid #2fcfae;color:#012f27;border-radius:50px;padding:6px 16px;font-size:.85rem;font-weight:600;margin:4px;}}.industries-block{{margin:24px 0;}}</style>
{HEAD_LINKS}
</head>
<body>
{NAV}
<section id="hero">
  <div class="container hero-inner">
    <div class="row align-items-center g-5">
      <div class="col-lg-7">
        <div class="reveal from-left">
          <p style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#2fcfae;margin-bottom:12px;">FREE CARD MACHINE · {city.upper()}</p>
          <h1 class="hero-title">Free Card Machine<br>for {city}<span class="grad"> Businesses</span></h1>
          <div class="hero-img-mobile d-lg-none"><img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine {city}"></div>
          <p class="hero-sub">No monthly rental. No long contracts. Just a free DOJO card machine and a simple per-transaction rate — helping {city} businesses keep more of every sale.</p>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Zero Monthly Rental Fee</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Next-Day Payouts</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Dual WiFi + 4G Connectivity</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>24/7 UK Support</div>
          <div class="mt-4"><a href="#enquire" class="btn-solid">Claim Your FREE Card Machine <i class="fas fa-arrow-right"></i></a></div>
        </div>
      </div>
      <div class="col-lg-5 d-none d-lg-block">
        <div class="hero-img-card reveal from-right"><img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {city} businesses"></div>
      </div>
    </div>
  </div>
</section>
{STATS_BAR}
<section style="padding:60px 0;background:var(--light);">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-7 reveal from-left">
        <span class="sec-badge">CARD MACHINES IN {city.upper()}</span>
        <h2 class="sec-title" style="margin-top:12px;">Why {city} Businesses<br><span class="sec-grad">Are Switching</span></h2>
        <div class="teal-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;line-height:1.8;margin-top:20px;">{desc}</p>
      </div>
      <div class="col-lg-5 reveal from-right">
        <div style="background:#fff;border:1px solid var(--border);border-radius:12px;padding:28px;">
          <h5 style="font-weight:700;margin-bottom:16px;color:var(--green);">Industries We Serve in {city}</h5>
          <div class="industries-block">{ind_html}</div>
          <a href="#enquire" class="btn-solid mt-3" style="width:100%;justify-content:center;">Get Your Free Machine <i class="fas fa-arrow-right"></i></a>
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
    for loc in NEW_TOWNS:
        fname = f"free-card-machine-{loc['slug']}.html"
        with open(os.path.join(BASE_DIR, fname), "w", encoding="utf-8") as f:
            f.write(build_page(loc))
        print(f"  Created: {fname}")
        slugs.append(loc["slug"]); count += 1
    print(f"\nDone — {count} town pages generated.")
    print("\nSitemap entries:")
    for s in slugs:
        print(f'  <url><loc>{DOMAIN}/free-card-machine-{s}</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>0.90</priority></url>')

if __name__ == "__main__":
    main()
