"""Generate Payment Card Services location + industry SEO pages — run once then delete."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

# ── CITY PAGES ───────────────────────────────────────────────────────────────

CITIES = [
    {
        "slug": "manchester",
        "city": "Manchester",
        "postcode": "M1",
        "region": "North West England",
        "desc": "Manchester's business community spans hospitality, retail, tech, and the creative industries — all sectors where card payments are essential to daily trading. From the Northern Quarter's independent cafes and bars to Spinningfields' professional services firms, Manchester businesses are moving away from cash at speed. If you're still paying a monthly rental fee on your card machine, you're overpaying.",
        "industries": ["Restaurants & Bars", "Independent Retail", "Hair & Beauty", "Market Traders", "Tradespeople"],
    },
    {
        "slug": "birmingham",
        "city": "Birmingham",
        "postcode": "B1",
        "region": "West Midlands",
        "desc": "Birmingham is the UK's second-largest city and one of its most commercially active. From the Bullring's retail sector to the Jewellery Quarter's specialist businesses and the city's thriving hospitality scene, card payments are fundamental to how Birmingham businesses operate every day. Cutting the cost of accepting those payments is one of the fastest ways to improve your bottom line.",
        "industries": ["Restaurants & Takeaways", "Retail Shops", "Hair & Beauty Salons", "Tradespeople", "Market Stalls"],
    },
    {
        "slug": "leeds",
        "city": "Leeds",
        "postcode": "LS1",
        "region": "West Yorkshire",
        "desc": "Leeds has one of the most vibrant independent business scenes in the North of England. From the Victoria Quarter's boutiques to Headingley's cafes and the city centre's busy restaurant trade, card payments dominate. With consumer cash use falling below 15% nationally, Leeds businesses that still pay a monthly rental fee on their card machine are carrying an unnecessary fixed cost.",
        "industries": ["Restaurants & Cafes", "Independent Retail", "Hair Salons", "Gyms & Fitness Studios", "Tradespeople"],
    },
    {
        "slug": "bristol",
        "city": "Bristol",
        "postcode": "BS1",
        "region": "South West England",
        "desc": "Bristol's independent business culture is second to none. From Clifton's boutiques and wine bars to Stokes Croft's creative businesses and the city's exceptional restaurant scene, Bristol is a city that runs on card payments. The old model of paying a monthly rental for a card machine simply doesn't make sense for Bristol's independent businesses — there's a better way.",
        "industries": ["Restaurants & Bars", "Independent Retail", "Hair & Beauty", "Hospitality", "Creative Services"],
    },
    {
        "slug": "glasgow",
        "city": "Glasgow",
        "postcode": "G1",
        "region": "Scotland",
        "desc": "Glasgow is Scotland's commercial capital — a city with a thriving hospitality sector, strong retail trade, and a business community that demands reliable, cost-effective payment solutions. Whether you run a West End restaurant, a Merchant City bar, or a retail unit on Buchanan Street, eliminating your card machine rental fees is a straightforward way to reduce fixed costs and improve cash flow.",
        "industries": ["Restaurants & Pubs", "Retail", "Hair & Beauty", "Tradespeople", "Market Traders"],
    },
    {
        "slug": "edinburgh",
        "city": "Edinburgh",
        "postcode": "EH1",
        "region": "Scotland",
        "desc": "Edinburgh's economy combines tourism, financial services, and a thriving independent business community — all of which depend on reliable card payment infrastructure. From the Royal Mile's hospitality businesses to Stockbridge's boutiques and the city's busy festival trade, card payments are non-negotiable. What is negotiable is what you pay for them — starting with your monthly rental fee.",
        "industries": ["Hotels & B&Bs", "Restaurants & Cafes", "Retail", "Tradespeople", "Hair & Beauty"],
    },
    {
        "slug": "liverpool",
        "city": "Liverpool",
        "postcode": "L1",
        "region": "North West England",
        "desc": "Liverpool's city centre, Baltic Triangle, and independent business community all run on card payments. The city's hospitality sector is one of the largest outside London, and its retail and market trade is extensive. For Liverpool businesses still paying a monthly rental fee on a card machine, the numbers simply don't add up — especially when a free alternative with better features exists.",
        "industries": ["Bars & Restaurants", "Independent Retail", "Market Traders", "Tradespeople", "Hair & Beauty"],
    },
    {
        "slug": "sheffield",
        "city": "Sheffield",
        "postcode": "S1",
        "region": "South Yorkshire",
        "desc": "Sheffield has built one of the North of England's most distinctive independent business communities — from Kelham Island's bars and restaurants to the city's strong manufacturing and trades sector. Whether you're a Sheffield restaurant owner, a builder, or a hairdresser, you're processing card payments every day. The question is how much those payments are costing you in fixed rental fees.",
        "industries": ["Restaurants & Bars", "Tradespeople", "Retail", "Hair & Beauty", "Market Traders"],
    },
    {
        "slug": "newcastle",
        "city": "Newcastle",
        "postcode": "NE1",
        "region": "North East England",
        "desc": "Newcastle upon Tyne has one of the UK's most active nighttime economies and a growing daytime retail and hospitality sector. From Grainger Street's shops to the Quayside's restaurants and bars, Newcastle businesses process card payments at high volumes. The cost of accepting those payments — particularly fixed monthly rental fees — is something every Newcastle business owner should be reviewing.",
        "industries": ["Bars & Restaurants", "Retail", "Hair & Beauty", "Tradespeople", "Hotels"],
    },
    {
        "slug": "nottingham",
        "city": "Nottingham",
        "postcode": "NG1",
        "region": "East Midlands",
        "desc": "Nottingham's diverse business economy — from its retail core to its hospitality sector and growing independent scene — runs on card payments. With two major universities bringing a young, cashless population into the city, contactless payments are the norm. Businesses in Nottingham still paying monthly rental fees on their card machines are falling behind both on cost and on capability.",
        "industries": ["Restaurants & Cafes", "Retail", "Hair & Beauty", "Tradespeople", "Student-Facing Businesses"],
    },
    {
        "slug": "leicester",
        "city": "Leicester",
        "postcode": "LE1",
        "region": "East Midlands",
        "desc": "Leicester's rich mix of independent retail, hospitality, and trades businesses all rely on card payment infrastructure. The city's diverse business community — from the Golden Mile's restaurants to the city centre's retail and service businesses — has embraced contactless payments. What many haven't yet done is eliminated the unnecessary monthly rental fee that older card machine contracts carry.",
        "industries": ["Restaurants & Takeaways", "Independent Retail", "Hair & Beauty", "Tradespeople", "Market Stalls"],
    },
    {
        "slug": "brighton",
        "city": "Brighton",
        "postcode": "BN1",
        "region": "South East England",
        "desc": "Brighton's independent, creative business culture makes it one of the UK's most distinctive trading environments. From the Lanes' boutiques to Hove's restaurants and the city's vast hospitality sector, card payments dominate. Brighton's business community is also savvy about costs — and an unnecessary monthly rental fee on a card machine is exactly the kind of overhead that good operators cut first.",
        "industries": ["Restaurants & Bars", "Independent Retail", "Hair & Beauty", "Events & Hospitality", "Tradespeople"],
    },
    {
        "slug": "cardiff",
        "city": "Cardiff",
        "postcode": "CF10",
        "region": "Wales",
        "desc": "Cardiff is the fastest-growing capital city in the UK, with a rapidly expanding hospitality sector, a thriving independent retail scene, and a business community that's moving decisively towards cashless trading. Welsh businesses across the capital are processing card payments every day — and too many are still paying monthly rental fees that could easily be eliminated.",
        "industries": ["Restaurants & Bars", "Retail", "Hair & Beauty", "Tradespeople", "Hotels & Guesthouses"],
    },
    {
        "slug": "southampton",
        "city": "Southampton",
        "postcode": "SO14",
        "region": "Hampshire",
        "desc": "Southampton's port economy, retail sector, and growing hospitality scene all demand reliable, cost-effective card payment solutions. From the city centre's retail units to the waterfront's restaurants and the busy trades sector serving Hampshire's housing market, Southampton businesses process significant card volumes daily. A free card machine with no monthly rental is a straightforward upgrade.",
        "industries": ["Restaurants & Cafes", "Retail", "Tradespeople", "Hair & Beauty", "Hospitality"],
    },
    {
        "slug": "reading",
        "city": "Reading",
        "postcode": "RG1",
        "region": "Berkshire",
        "desc": "Reading's tech-sector presence and strong retail core make it one of the South East's most commercially active towns outside London. Businesses across Berkshire — from town centre retailers to the growing hospitality scene and busy trades sector — are processing card payments at scale. For businesses still on monthly rental contracts, switching to a zero-rental model is one of the easiest cost-saving decisions available.",
        "industries": ["Restaurants & Bars", "Retail", "Tech & Professional Services", "Tradespeople", "Hair & Beauty"],
    },
    {
        "slug": "coventry",
        "city": "Coventry",
        "postcode": "CV1",
        "region": "West Midlands",
        "desc": "Coventry's regenerating city centre and growing independent business community are driving increased card payment volumes across the West Midlands. From the city's hospitality sector to its retail businesses and active trades community, card payments are fundamental. A free DOJO card machine with no monthly rental fee means more of every transaction stays in your business.",
        "industries": ["Restaurants & Cafes", "Independent Retail", "Tradespeople", "Hair & Beauty", "Market Traders"],
    },
    {
        "slug": "oxford",
        "city": "Oxford",
        "postcode": "OX1",
        "region": "Oxfordshire",
        "desc": "Oxford's high footfall, internationally-facing hospitality sector, and premium retail environment make it one of the most payment-intensive trading environments in the South East. With a wealthy, cashless customer base spanning students, academics, and tourists, Oxford businesses need payment infrastructure that's reliable, fast, and cost-effective. Eliminating monthly rental fees is the obvious first step.",
        "industries": ["Restaurants & Cafes", "Independent Retail", "Hotels & B&Bs", "Tradespeople", "Hair & Beauty"],
    },
    {
        "slug": "cambridge",
        "city": "Cambridge",
        "postcode": "CB1",
        "region": "Cambridgeshire",
        "desc": "Cambridge's blend of tourism, university spend, and a high-income professional population creates consistent, high-volume card payment demand across its businesses. From the city's independent restaurants and shops to its busy trades sector serving the surrounding Cambridgeshire market, card payments are constant. The businesses that thrive here keep their cost per transaction as low as possible.",
        "industries": ["Restaurants & Cafes", "Independent Retail", "Hotels & B&Bs", "Tradespeople", "Hair & Beauty"],
    },
    {
        "slug": "london",
        "city": "London",
        "postcode": "Various",
        "region": "London",
        "desc": "London is the UK's most payment-intensive trading environment. With cash use in the capital falling below 10% of transactions, card payments are the default across every sector — hospitality, retail, trades, professional services, and beyond. London businesses are also under the greatest cost pressure, making a free card machine with no monthly rental not just attractive but essential for any business serious about margins.",
        "industries": ["Restaurants & Hospitality", "Retail", "Hair & Beauty", "Tradespeople", "Markets & Pop-Ups"],
    },
    {
        "slug": "milton-keynes",
        "city": "Milton Keynes",
        "postcode": "MK9",
        "region": "Buckinghamshire",
        "desc": "Milton Keynes is one of the UK's fastest-growing cities — a planned business hub with high footfall retail centres, a growing hospitality sector, and a large commuter population that shops and eats locally. Businesses across MK process high card payment volumes every day. For those still paying a monthly rental on their card machine, switching to a zero-rental model is a fast, straightforward cost saving.",
        "industries": ["Retail", "Restaurants & Cafes", "Hair & Beauty", "Tradespeople", "Gyms & Leisure"],
    },
]

# ── INDUSTRY PAGES ────────────────────────────────────────────────────────────

INDUSTRIES = [
    {
        "slug": "restaurants",
        "industry": "Restaurants",
        "headline": "Free Card Machines for Restaurants",
        "icon": "fa-utensils",
        "desc": "Restaurants are one of the highest-volume card payment environments in the UK. Between table service, bar tabs, takeaway orders, and event bookings, a busy restaurant can run hundreds of transactions a day. Every one of those transactions costs you money — and if you're paying a monthly rental fee on top of your transaction rate, you're paying more than you need to.",
        "why": "Restaurant owners need speed, reliability, and simplicity from their payment technology. DOJO card machines are built for exactly this — fast transaction times, dual WiFi/4G connectivity so you never go offline during a service, and next-day payouts that keep your cash flow consistent. And with zero monthly rental, the savings are immediate and ongoing.",
        "pain_point": "Are you still paying a monthly rental fee for your restaurant card machine? Most restaurant operators are. It's one of the first costs you can eliminate.",
    },
    {
        "slug": "hair-salons",
        "industry": "Hair Salons",
        "headline": "Free Card Machines for Hair Salons",
        "icon": "fa-scissors",
        "desc": "Hair salons are almost entirely cashless — clients expect to pay by card or contactless wallet, and most never carry cash at all. For salon owners, a reliable card machine is as essential as the chair itself. What shouldn't be essential is the monthly rental fee that most salons are quietly paying on top of their transaction costs.",
        "why": "A DOJO card machine through Payment Card Services gives hair salons a professional, reliable payment solution with no monthly rental charge. Accept all cards, Apple Pay, and Google Pay, track transactions through the DOJO app, and receive payouts the next working day. Tap to Pay on iPhone also gives you a backup payment method if you ever need it.",
        "pain_point": "Most salon owners sign up for a card machine through their bank or a high-street provider and don't realise there's a zero-rental alternative available.",
    },
    {
        "slug": "retail",
        "industry": "Retail",
        "headline": "Free Card Machines for Retail Businesses",
        "icon": "fa-store",
        "desc": "Retail businesses — from independent boutiques to larger multi-unit operators — process card payments all day, every day. Transaction speed, reliability, and cost-per-transaction are the metrics that matter most. An unnecessary monthly rental fee on your card machine is a fixed cost that serves the provider, not your business.",
        "why": "Payment Card Services provides DOJO card machines to UK retailers with no monthly rental charge. Whether you have one till or several, you get fast transaction processing, dual WiFi/4G connectivity to ensure you never miss a sale, and the DOJO app for real-time reporting. Next-day payouts keep your stock buying power consistent.",
        "pain_point": "Many retailers are on legacy merchant service contracts that were set up when they first opened. Those contracts often carry rental fees that were never necessary and have only increased over time.",
    },
    {
        "slug": "tradespeople",
        "industry": "Tradespeople",
        "headline": "Free Card Machines for Tradespeople",
        "icon": "fa-hard-hat",
        "desc": "Plumbers, electricians, builders, decorators, and other tradespeople are collecting larger payments in cash less and less — and clients increasingly expect to pay by card at the end of a job. For sole traders and small trade firms, a card machine needs to be portable, reliable, and cheap to run. A monthly rental fee that adds nothing to your service is the first thing to cut.",
        "why": "DOJO's card machines are ideal for tradespeople — compact, dual-connected via WiFi and 4G SIM so they work anywhere, and simple enough to use between jobs without any hassle. Tap to Pay on iPhone gives you an instant backup. No monthly rental means your payment setup costs you nothing except a small percentage of what you actually take.",
        "pain_point": "Most tradespeople either avoid card machines because of the cost, or pay more than they should through providers who charge monthly fees. There's a better option.",
    },
    {
        "slug": "pubs-and-bars",
        "industry": "Pubs & Bars",
        "headline": "Free Card Machines for Pubs & Bars",
        "icon": "fa-beer",
        "desc": "Pubs and bars are high-volume card payment environments — especially at weekends when the pace is relentless and reliability is everything. A card machine that goes offline during Friday night service isn't just an inconvenience; it's lost revenue and frustrated customers. Payment infrastructure needs to be rock-solid, and the cost of running it needs to be as low as possible.",
        "why": "DOJO card machines offer dual WiFi/4G connectivity — so if your broadband drops mid-service, the machine switches automatically to 4G and keeps taking payments. No monthly rental means your overhead stays low even in quieter periods. Next-day payouts keep your ordering cash flow predictable, and 24/7 UK support means any issues get resolved around the clock.",
        "pain_point": "Many pubs and bars are locked into rental agreements with legacy payment providers. Those agreements predate the zero-rental model — and they're costing licensees money every month.",
    },
]

# ── SHARED HTML FRAGMENTS ─────────────────────────────────────────────────────

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
              <div class="col-12">
                <label class="enq-label" for="enq-name">Full Name *</label>
                <input type="text" class="enq-input" id="enq-name" name="full_name" placeholder="Your full name" required>
              </div>
              <div class="col-sm-6">
                <label class="enq-label" for="enq-email">Email Address *</label>
                <input type="email" class="enq-input" id="enq-email" name="email" placeholder="your@email.com" required>
              </div>
              <div class="col-sm-6">
                <label class="enq-label" for="enq-phone">Phone Number *</label>
                <input type="tel" class="enq-input" id="enq-phone" name="phone" placeholder="+44 7700 000000" required>
              </div>
              <div class="col-12">
                <label class="enq-label" for="enq-type">Enquiry Type</label>
                <select class="enq-select" id="enq-type" name="enquiry_type">
                  <option value="" disabled selected>--- Please Select ---</option>
                  <option>New Card Machine</option>
                  <option>Switching Provider</option>
                  <option>Multiple Machines</option>
                  <option>General Enquiry</option>
                </select>
              </div>
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
        <div class="foot-contact-item">
          <i class="fas fa-map-marker-alt"></i>
          <span>Eubank Consulting Limited,<br>166 College Road, Harrow, England, HA1 1BH</span>
        </div>
        <div class="foot-contact-item">
          <i class="fas fa-envelope"></i>
          <span><a href="mailto:{EMAIL}">{EMAIL}</a></span>
        </div>
        <div class="foot-contact-item mb-3">
          <i class="fas fa-shield-alt"></i>
          <span>Authorised DOJO Consultant</span>
        </div>
        <a href="#enquire" class="foot-cta-btn">Get Free Card Machine</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Payment Card Services. All rights reserved.</span>
      <div class="foot-legal">
        <a href="/">Privacy Policy</a>
        <a href="/">Cookie Policy</a>
      </div>
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

HEAD_LINKS = """  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">"""

SCROLL_BTN = """<button id="scrollBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Scroll to top">
  <i class="fas fa-chevron-up"></i>
</button>"""


# ── CITY PAGE BUILDER ─────────────────────────────────────────────────────────

def build_city_page(loc):
    city      = loc["city"]
    slug      = loc["slug"]
    postcode  = loc["postcode"]
    region    = loc["region"]
    desc      = loc["desc"]
    industries = loc["industries"]

    industries_html = "".join(
        f'<span class="area-pill-teal"><i class="fas fa-check-circle me-1"></i>{ind}</span>'
        for ind in industries
    )

    schema_area = json_city(city, postcode)
    keywords = f"free card machine {city}, card machine {city}, DOJO card machine {city}, no rental card machine {city}, merchant services {city}, contactless payments {city}, point of sale {city}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Free Card Machine {city} | No Monthly Rental | Payment Card Services</title>
  <meta name="description" content="Get a FREE DOJO card machine for your {city} business — no monthly rental, just a simple transaction rate. Next-day payouts, 24/7 UK support. Claim yours today.">
  <meta name="keywords" content="{keywords}">
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
  <meta property="og:description" content="Free DOJO card machine for {city} businesses — no monthly rental. Next-day payouts, dual connectivity, 24/7 UK support. Get yours today.">
  <meta property="og:url" content="{DOMAIN}/free-card-machine-{slug}">
  <meta property="og:image" content="{DOMAIN}/images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FinancialService",
    "name": "Payment Card Services — {city}",
    "description": "Free DOJO card machines for businesses in {city} with no monthly rental charges. Next-day payouts, dual connectivity, and 24/7 UK support.",
    "url": "{DOMAIN}/free-card-machine-{slug}",
    "email": "{EMAIL}",
    "areaServed": {schema_area},
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "166 College Road",
      "addressLocality": "Harrow",
      "addressRegion": "England",
      "postalCode": "HA1 1BH",
      "addressCountry": "GB"
    }}
  }}
  </script>
  <style>
    .area-pill-teal {{
      display: inline-block;
      background: #e6f9f4;
      border: 1px solid #2fcfae;
      color: #012f27;
      border-radius: 50px;
      padding: 6px 16px;
      font-size: .85rem;
      font-weight: 600;
      margin: 4px;
    }}
    .industries-block {{ margin: 24px 0; }}
    .local-intro {{ max-width: 860px; margin: 0 auto; padding: 60px 20px 0; }}
    .local-intro .sec-badge {{ margin-bottom: 16px; }}
  </style>
{HEAD_LINKS}
</head>
<body>

{NAV}

<!-- HERO -->
<section id="hero">
  <div class="container hero-inner">
    <div class="row align-items-center g-5">
      <div class="col-lg-7">
        <div class="reveal from-left">
          <p style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#2fcfae;margin-bottom:12px;">FREE CARD MACHINE · {city.upper()}</p>
          <h1 class="hero-title">Free Card Machine<br>for {city}<span class="grad"> Businesses</span></h1>
          <div class="hero-img-mobile d-lg-none">
            <img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine {city}">
          </div>
          <p class="hero-sub">No monthly rental. No long contracts. Just a free DOJO card machine and a simple per-transaction rate — helping {city} businesses keep more of every sale.</p>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Zero Monthly Rental Fee</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Next-Day Payouts</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Dual WiFi + 4G Connectivity</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>24/7 UK Support</div>
          <div class="mt-4">
            <a href="#enquire" class="btn-solid">Claim Your FREE Card Machine <i class="fas fa-arrow-right"></i></a>
          </div>
        </div>
      </div>
      <div class="col-lg-5 d-none d-lg-block">
        <div class="hero-img-card reveal from-right">
          <img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {city} businesses">
        </div>
      </div>
    </div>
  </div>
</section>

{STATS_BAR}

<!-- LOCAL INTRO -->
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
          <div class="industries-block">{industries_html}</div>
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


# ── INDUSTRY PAGE BUILDER ─────────────────────────────────────────────────────

def build_industry_page(ind):
    slug      = ind["slug"]
    industry  = ind["industry"]
    headline  = ind["headline"]
    icon      = ind["icon"]
    desc      = ind["desc"]
    why       = ind["why"]
    pain      = ind["pain_point"]

    keywords = f"card machine for {industry.lower()}, free card machine {industry.lower()}, DOJO {industry.lower()} card machine, no rental card machine {industry.lower()}, merchant services {industry.lower()}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{headline} | No Monthly Rental | Payment Card Services</title>
  <meta name="description" content="Free DOJO card machine for {industry.lower()} — no monthly rental, just a simple transaction rate. Next-day payouts and 24/7 UK support. Claim yours today.">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="Payment Card Services">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#012f27">
  <link rel="canonical" href="{DOMAIN}/card-machine-for-{slug}">
  <link rel="icon" type="image/png" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <link rel="apple-touch-icon" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Payment Card Services">
  <meta property="og:title" content="{headline} | No Monthly Rental | Payment Card Services">
  <meta property="og:description" content="Free DOJO card machine for {industry.lower()} businesses — no monthly rental. Next-day payouts, 24/7 UK support.">
  <meta property="og:url" content="{DOMAIN}/card-machine-for-{slug}">
  <meta property="og:image" content="{DOMAIN}/images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FinancialService",
    "name": "Payment Card Services — {industry}",
    "description": "Free DOJO card machines for {industry.lower()} businesses in the UK with no monthly rental charges.",
    "url": "{DOMAIN}/card-machine-for-{slug}",
    "email": "{EMAIL}",
    "areaServed": "GB",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "166 College Road",
      "addressLocality": "Harrow",
      "addressRegion": "England",
      "postalCode": "HA1 1BH",
      "addressCountry": "GB"
    }}
  }}
  </script>
  <style>
    .pain-box {{
      background: var(--teal-pale);
      border-left: 4px solid var(--teal);
      border-radius: 0 8px 8px 0;
      padding: 20px 24px;
      margin: 28px 0;
      color: var(--green);
      font-weight: 500;
    }}
  </style>
{HEAD_LINKS}
</head>
<body>

{NAV}

<!-- HERO -->
<section id="hero">
  <div class="container hero-inner">
    <div class="row align-items-center g-5">
      <div class="col-lg-7">
        <div class="reveal from-left">
          <p style="font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:#2fcfae;margin-bottom:12px;">FREE CARD MACHINE · {industry.upper()}</p>
          <h1 class="hero-title">{headline}<span class="grad"> — No Monthly Rental</span></h1>
          <div class="hero-img-mobile d-lg-none">
            <img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {industry}">
          </div>
          <p class="hero-sub">Payment Card Services provides DOJO card machines to UK {industry.lower()} businesses with no monthly rental charge — just a simple per-transaction rate. Next-day payouts and 24/7 UK support included.</p>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Zero Monthly Rental Fee</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Next-Day Payouts</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>Tap to Pay on iPhone</div>
          <div class="hero-chk"><i class="fas fa-circle-check"></i>24/7 UK Support</div>
          <div class="mt-4">
            <a href="#enquire" class="btn-solid">Get Your FREE Card Machine <i class="fas fa-arrow-right"></i></a>
          </div>
        </div>
      </div>
      <div class="col-lg-5 d-none d-lg-block">
        <div class="hero-img-card reveal from-right">
          <img src="images/24b8eaefbbf9eb3ecfac877604e424f339285460 (1).png" alt="DOJO Card Machine for {industry}">
        </div>
      </div>
    </div>
  </div>
</section>

{STATS_BAR}

<!-- INDUSTRY CONTENT -->
<section style="padding:60px 0;background:var(--light);">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-6 reveal from-left">
        <span class="sec-badge"><i class="fas {icon} me-1"></i> {industry.upper()}</span>
        <h2 class="sec-title" style="margin-top:12px;">Card Payments for<br><span class="sec-grad">{industry}</span></h2>
        <div class="teal-bar"></div>
        <p style="color:var(--muted);font-size:1.05rem;line-height:1.8;margin-top:20px;">{desc}</p>
        <div class="pain-box"><i class="fas fa-lightbulb me-2" style="color:var(--teal-dark);"></i>{pain}</div>
      </div>
      <div class="col-lg-6 reveal from-right">
        <h3 style="font-weight:700;margin-bottom:16px;">Why DOJO Works for {industry}</h3>
        <p style="color:var(--muted);line-height:1.8;">{why}</p>
        <a href="#enquire" class="btn-solid mt-4">Claim Your Free Machine <i class="fas fa-arrow-right"></i></a>
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


def json_city(city, postcode):
    return f'{{"@type":"City","name":"{city}","postalCode":"{postcode}","addressCountry":"GB"}}'


def main():
    count = 0
    for loc in CITIES:
        filename = f"free-card-machine-{loc['slug']}.html"
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(build_city_page(loc))
        print(f"  Created: {filename}")
        count += 1

    for ind in INDUSTRIES:
        filename = f"card-machine-for-{ind['slug']}.html"
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(build_industry_page(ind))
        print(f"  Created: {filename}")
        count += 1

    print(f"\nDone — {count} pages generated.")


if __name__ == "__main__":
    main()
