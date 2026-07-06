"""Generate FAQ/blog content pages."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

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

HEAD_LINKS = """  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">"""

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
const faqItems=document.querySelectorAll('.faq-item');
faqItems.forEach(item=>{{item.querySelector('.faq-question').addEventListener('click',()=>{{const isOpen=item.classList.contains('open');faqItems.forEach(i=>i.classList.remove('open'));if(!isOpen)item.classList.add('open');}});}});
</script>"""

ENQUIRY_FORM = f"""<section id="enquire" style="padding:60px 0;background:var(--light);">
  <div class="container enq-inner">
    <div class="text-center mb-5 reveal">
      <h2 class="enq-heading">Get Your Free Card Machine Today</h2>
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

FAQ_STYLE = """<style>
  .blog-content{max-width:780px;margin:0 auto;padding:40px 0 60px;}
  .blog-content h2{font-size:1.6rem;font-weight:700;color:var(--green);margin:40px 0 16px;}
  .blog-content h3{font-size:1.25rem;font-weight:700;color:var(--green);margin:28px 0 12px;}
  .blog-content p{color:var(--muted);line-height:1.85;margin-bottom:20px;}
  .blog-content ul{color:var(--muted);line-height:1.85;padding-left:20px;margin-bottom:20px;}
  .blog-content ul li{margin-bottom:8px;}
  .blog-content .highlight-box{background:linear-gradient(135deg,#012f27,#024a3e);color:#fff;border-radius:12px;padding:24px 28px;margin:32px 0;}
  .blog-content .highlight-box p{color:rgba(255,255,255,.85);margin:0;}
  .faq-item{border:1px solid var(--border);border-radius:10px;margin-bottom:12px;overflow:hidden;}
  .faq-question{padding:18px 22px;cursor:pointer;font-weight:600;color:var(--green);display:flex;justify-content:space-between;align-items:center;user-select:none;}
  .faq-question::after{content:'\\f107';font-family:'Font Awesome 6 Free';font-weight:900;transition:transform .3s;flex-shrink:0;}
  .faq-item.open .faq-question::after{transform:rotate(180deg);}
  .faq-answer{max-height:0;overflow:hidden;transition:max-height .35s ease,padding .35s ease;padding:0 22px;color:var(--muted);line-height:1.8;}
  .faq-item.open .faq-answer{max-height:400px;padding:0 22px 18px;}
  .article-meta{display:flex;gap:20px;margin-bottom:32px;color:var(--muted);font-size:.85rem;flex-wrap:wrap;}
  .article-meta span{display:flex;align-items:center;gap:6px;}
</style>"""

PAGES = [
    {
        "slug": "how-much-does-a-card-machine-cost",
        "title": "How Much Does a Card Machine Cost in the UK? (2026 Guide)",
        "meta": "Everything UK business owners need to know about card machine costs in 2026 — rental fees, transaction rates, hidden charges, and how to get a card machine for free.",
        "h1": "How Much Does a Card Machine Cost in the UK?",
        "sub": "A straightforward guide to card machine pricing — rental fees, transaction rates, and how to get one for free.",
        "date": "July 2026",
        "body": """
<div class="article-meta">
  <span><i class="fas fa-calendar"></i>July 2026</span>
  <span><i class="fas fa-clock"></i>5 minute read</span>
  <span><i class="fas fa-tag"></i>Card Machine Costs</span>
</div>
<p>One of the most common questions UK business owners ask when looking at card payments is: how much does a card machine actually cost? The answer depends on which provider you choose — and there's a significant range between the best and worst value options in the market.</p>

<h2>The Two Main Cost Models</h2>
<p>Card machine costs in the UK typically fall into two categories:</p>
<ul>
  <li><strong>Monthly rental + transaction fees</strong> — You pay a fixed monthly fee (typically £15–£30+) plus a percentage on every transaction. This is the traditional model used by banks and older payment providers.</li>
  <li><strong>Zero rental + transaction fees</strong> — You pay no monthly fee and only a small percentage per transaction. This is the model that DOJO and similar modern providers use.</li>
</ul>

<h2>The Hidden Cost of Monthly Rental</h2>
<p>Monthly rental fees sound small — £20 a month doesn't sound like much. But over the course of a year, that's £240. Over three years (a typical contract), that's £720+ that goes to the payment provider before a single transaction is processed. For a small business with thin margins, that's real money.</p>

<div class="highlight-box">
  <p><strong style="color:#2fcfae;">Key fact:</strong> A zero-rental card machine through Payment Card Services costs nothing per month. You pay only when you take a payment — a small, competitive transaction rate with no hidden charges.</p>
</div>

<h2>Transaction Rate Breakdown</h2>
<p>Whether you're on a rental or no-rental model, you'll pay a transaction fee on every card payment. Typical rates for UK businesses in 2026:</p>
<ul>
  <li><strong>DOJO (via Payment Card Services):</strong> Competitive per-transaction rate, no monthly fee</li>
  <li><strong>SumUp:</strong> 1.69% standard rate</li>
  <li><strong>Square:</strong> 1.75% standard rate</li>
  <li><strong>Zettle by PayPal:</strong> 1.75% standard rate</li>
  <li><strong>Traditional bank card machines:</strong> 1.5–2%+ plus monthly rental</li>
</ul>

<h2>What About Setup Costs?</h2>
<p>With Payment Card Services, there are no setup costs. The DOJO card machine is provided free of charge, there's no installation fee, and the onboarding process is handled by our UK-based team. With some other providers, you'll pay £20–£100+ for the card reader hardware.</p>

<h2>What Are the Real Costs to Compare?</h2>
<p>When comparing card machine providers, look at the full picture:</p>
<ul>
  <li>Monthly rental fee (£0 vs. £15–£30+)</li>
  <li>Per-transaction rate (look for rates under 1.75%)</li>
  <li>Hardware cost (free vs. £20–£100)</li>
  <li>Payout speed (next day vs. 1–3 business days)</li>
  <li>Support availability (24/7 UK vs. online only)</li>
</ul>

<h2>The Bottom Line</h2>
<p>For most UK small and medium businesses, a zero-rental card machine with a competitive transaction rate is the best value option. There's no reason to pay a monthly rental fee when alternatives that deliver the same — or better — functionality are available at no monthly cost.</p>
<p>If you're currently paying monthly rental on a card machine, switching to a zero-rental DOJO machine is one of the fastest ways to reduce your fixed operating costs.</p>
"""
    },
    {
        "slug": "best-card-machine-for-small-business",
        "title": "Best Card Machine for Small Business UK 2026 | Honest Comparison",
        "meta": "Looking for the best card machine for your small business in the UK? We compare DOJO, SumUp, Square, Zettle and more on cost, speed, support, and features.",
        "h1": "Best Card Machine for Small Business UK (2026)",
        "sub": "An honest comparison of the top card machines for UK small businesses — based on cost, reliability, and what actually matters day-to-day.",
        "date": "July 2026",
        "body": """
<div class="article-meta">
  <span><i class="fas fa-calendar"></i>July 2026</span>
  <span><i class="fas fa-clock"></i>6 minute read</span>
  <span><i class="fas fa-tag"></i>Card Machine Comparison</span>
</div>
<p>With a growing number of card machine providers in the UK, choosing the right one for your small business takes a bit of research. This guide cuts through the marketing and focuses on what actually matters: total cost, payout speed, connectivity, and support quality.</p>

<h2>What Small Businesses Actually Need From a Card Machine</h2>
<ul>
  <li><strong>Reliability</strong> — It needs to work, every time, without WiFi issues mid-transaction</li>
  <li><strong>Fast payouts</strong> — Getting your money the next day makes a real difference to cash flow</li>
  <li><strong>Low cost</strong> — No monthly rental fees eating into margins</li>
  <li><strong>Real support</strong> — 24/7 UK-based help when something goes wrong</li>
</ul>

<h2>Our Top Pick: DOJO via Payment Card Services</h2>
<p>For UK small businesses that take card payments as a core part of their operation — restaurants, retailers, tradespeople, salons, cafes — DOJO is our top recommendation. Here's why:</p>
<ul>
  <li><strong>Zero monthly rental</strong> — no fixed overhead, ever</li>
  <li><strong>Dual connectivity</strong> — WiFi with automatic 4G SIM backup, so payments go through even when WiFi drops</li>
  <li><strong>Next-day payouts</strong> — money in your account the next working day</li>
  <li><strong>24/7 UK support</strong> — a real team based in the UK, available around the clock</li>
  <li><strong>Free hardware</strong> — the card machine is provided at no cost</li>
</ul>

<div class="highlight-box">
  <p><strong style="color:#2fcfae;">Why dual connectivity matters:</strong> Most card machines only connect via WiFi. When the WiFi drops (and it does), you're unable to take payments. DOJO automatically switches to its built-in 4G SIM backup — payments never stop.</p>
</div>

<h2>How Other Providers Compare</h2>
<h3>SumUp</h3>
<p>Good for very small, low-volume operations. Transaction rate of 1.69%, no monthly fee on the basic plan, but payouts take 1–3 business days and support is primarily online. No built-in 4G backup connectivity.</p>

<h3>Square</h3>
<p>Strong POS software and a good ecosystem, particularly for retail. Transaction rate of 1.75%. No monthly fee but hardware has a purchase cost. Payouts 1–2 business days. US-designed support structure. No automatic 4G backup.</p>

<h3>Zettle by PayPal</h3>
<p>Good PayPal integration and simple setup. 1.75% transaction rate, hardware purchase required. Business hours support only. No automatic 4G backup connectivity.</p>

<h3>Traditional Bank Card Machines</h3>
<p>Typically £15–£30+ per month in rental fees plus transaction rates of 1.5–2%+. Often on long contracts. Payouts 1–3 business days. The most expensive option for most small businesses.</p>

<h2>The Verdict</h2>
<p>If you're a UK small business taking card payments regularly — especially in hospitality, retail, or mobile services — DOJO via Payment Card Services is the strongest all-round option. Zero rental, best-in-class connectivity, next-day payouts, and real 24/7 UK support make it the most operationally sound choice for businesses that rely on payments every day.</p>
"""
    },
    {
        "slug": "do-i-need-a-card-machine",
        "title": "Do I Need a Card Machine for My Business? (UK Guide 2026)",
        "meta": "Wondering whether your UK business needs a card machine? This guide covers when card payments are essential, what you're losing by going cash-only, and how to get started for free.",
        "h1": "Do I Need a Card Machine for My Business?",
        "sub": "If you're still cash-only in 2026, here's what it's probably costing you — and how to fix it for free.",
        "date": "July 2026",
        "body": """
<div class="article-meta">
  <span><i class="fas fa-calendar"></i>July 2026</span>
  <span><i class="fas fa-clock"></i>4 minute read</span>
  <span><i class="fas fa-tag"></i>Getting Started</span>
</div>
<p>Card and contactless payments now account for the vast majority of UK consumer transactions. If your business is still cash-only, you're not just missing out on convenience — you're actively losing customers every day.</p>

<h2>The State of Cash in the UK</h2>
<p>UK Finance data consistently shows that card payments make up over 80% of retail transactions in the UK. Contactless payments alone account for more than half of all face-to-face transactions. In London and other major cities, the figure is even higher.</p>
<p>The shift isn't gradual anymore — it's complete. Most consumers under 40 regularly leave the house without cash. If your business can't accept their card, they'll go to the business that can.</p>

<h2>What Cash-Only Businesses Lose</h2>
<ul>
  <li><strong>Lost impulse purchases</strong> — Customers who didn't plan to spend but would if they could pay by card</li>
  <li><strong>Higher-value transactions</strong> — People spend more when paying by card</li>
  <li><strong>Repeat customers</strong> — A customer who can't pay their way won't come back</li>
  <li><strong>Credibility</strong> — Cash-only signals to customers that a business is informal or behind the times</li>
</ul>

<div class="highlight-box">
  <p><strong style="color:#2fcfae;">Research shows</strong> that businesses that add card payments typically see revenue increase by 15–30% in the first year — not because they charge more, but because they stop turning away customers who only carry cards.</p>
</div>

<h2>Do I Need a Card Machine or Can I Use Something Else?</h2>
<p>For most businesses with a physical presence — a shop, a salon, a stall, a van — a card machine is the right tool. It lets customers pay instantly at the point of service without delays or friction.</p>
<p>Alternatives like payment links (sending a customer a link to pay online) work for some service businesses but create unnecessary steps for in-person transactions. A card machine keeps checkout fast, professional, and seamless.</p>

<h2>The Cost Question: Can I Afford a Card Machine?</h2>
<p>Through Payment Card Services, a DOJO card machine costs nothing to rent. There's no monthly fee. The hardware is free. You pay only a small percentage per transaction — meaning you only pay when you earn.</p>
<p>The practical question isn't whether you can afford a card machine. It's whether you can afford not to have one.</p>

<h2>Which Businesses Need a Card Machine?</h2>
<p>Almost every business with customer-facing transactions benefits from accepting card payments:</p>
<ul>
  <li>Restaurants, cafes, and bars</li>
  <li>Retail shops and market stalls</li>
  <li>Hair salons, barbershops, and beauty businesses</li>
  <li>Tradespeople and mobile service businesses</li>
  <li>Hotels, B&Bs, and guesthouses</li>
  <li>Gyms, fitness studios, and personal trainers</li>
  <li>Vets, dentists, and healthcare providers</li>
  <li>Any business where customers come to you or you go to customers</li>
</ul>

<h2>How to Get Started</h2>
<p>Getting a free DOJO card machine through Payment Card Services takes minutes. Fill in the enquiry form below and our UK-based team will be in touch to set everything up — no monthly rental, no hidden fees, and no long-term contract lock-in.</p>
"""
    },
    {
        "slug": "card-machine-transaction-fees-explained",
        "title": "Card Machine Transaction Fees Explained | UK Small Business Guide 2026",
        "meta": "Everything UK small businesses need to know about card machine transaction fees — what you pay, why, and how to make sure you're getting a fair rate in 2026.",
        "h1": "Card Machine Transaction Fees Explained",
        "sub": "What you pay per transaction, why it varies, and how to make sure you're not overpaying.",
        "date": "July 2026",
        "body": """
<div class="article-meta">
  <span><i class="fas fa-calendar"></i>July 2026</span>
  <span><i class="fas fa-clock"></i>5 minute read</span>
  <span><i class="fas fa-tag"></i>Card Machine Fees</span>
</div>
<p>Every time a customer pays by card, the business pays a small fee — a percentage of the transaction value. These fees fund the payment infrastructure: the card networks (Visa and Mastercard), the issuing bank (the customer's bank), and the payment processor (your card machine provider).</p>
<p>Understanding how these fees work helps you choose the right provider and avoid overpaying.</p>

<h2>What is a Transaction Fee?</h2>
<p>A transaction fee is a percentage of each card payment that goes to your payment processor. For most UK small businesses using modern providers, this is between 1.69% and 1.75% of the transaction value.</p>
<p>Example: A customer pays £50. At 1.75%, you pay 87.5p to the payment processor. You receive £49.13.</p>

<h2>What Drives the Transaction Rate?</h2>
<p>Transaction rates are made up of several components:</p>
<ul>
  <li><strong>Interchange fee</strong> — paid to the customer's issuing bank (regulated in the UK at 0.2% for debit, 0.3% for credit)</li>
  <li><strong>Scheme fee</strong> — paid to Visa or Mastercard for use of their network</li>
  <li><strong>Processor margin</strong> — the payment provider's cut for providing the hardware, software, and support</li>
</ul>
<p>The published rate you see (e.g. 1.75%) covers all three. Providers with lower rates are typically taking a smaller margin, or have better interchange agreements due to higher processing volume.</p>

<h2>Flat Rate vs. Interchange Plus Pricing</h2>
<p>Most small business card machine providers use a flat rate — one percentage for all card types. This is simple and predictable: you always know exactly what you'll pay.</p>
<p>Some larger-volume businesses use interchange plus pricing, where the exact fee varies depending on the card type used. This can be cheaper for businesses processing over £500k per year, but it adds complexity for smaller operators.</p>

<div class="highlight-box">
  <p><strong style="color:#2fcfae;">For most UK small businesses:</strong> a flat rate from a zero-rental provider is the simplest and most cost-effective option. The rate is predictable, the hardware is free, and there are no monthly fees to absorb.</p>
</div>

<h2>Hidden Fees to Watch Out For</h2>
<p>Some card machine providers advertise a headline transaction rate but add charges that increase your real cost:</p>
<ul>
  <li><strong>Monthly minimum charges</strong> — if you don't hit a volume threshold, you pay a top-up fee</li>
  <li><strong>Statement fees</strong> — some providers charge for monthly statements</li>
  <li><strong>Authorisation fees</strong> — a small fixed fee per transaction on top of the percentage</li>
  <li><strong>Payout fees</strong> — some providers charge to transfer your money to your bank account</li>
  <li><strong>Chargeback fees</strong> — fees for disputed transactions</li>
</ul>
<p>With DOJO via Payment Card Services, the transaction rate is the transaction rate. There are no monthly minimums, no statement fees, and no hidden charges sitting beneath the headline number.</p>

<h2>How to Compare Transaction Rates Fairly</h2>
<p>When comparing providers, calculate your total cost per month under each option:</p>
<ol>
  <li>Take your average monthly card turnover</li>
  <li>Multiply by the transaction rate (as a decimal)</li>
  <li>Add any monthly rental fee</li>
  <li>Add any other fixed charges</li>
</ol>
<p>This gives you the true monthly cost of each option, allowing a like-for-like comparison rather than one based on headline rates alone.</p>

<h2>The Bottom Line</h2>
<p>For UK small businesses, the best card machine pricing combines a competitive transaction rate with zero monthly rental. DOJO, accessed through Payment Card Services, delivers exactly this — and adds next-day payouts and 24/7 UK support to make it the complete package for businesses that depend on card payments every day.</p>
"""
    },
]

def build_page(page):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="{page['meta']}">
  <meta name="author" content="Payment Card Services">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#012f27">
  <link rel="canonical" href="{DOMAIN}/{page['slug']}">
  <link rel="icon" type="image/png" href="images/24b8eaefbbf9eb3ecfac877604e424f339285460%20(1).png">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Payment Card Services">
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['meta']}">
  <meta property="og:url" content="{DOMAIN}/{page['slug']}">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{page['h1']}","description":"{page['meta']}","url":"{DOMAIN}/{page['slug']}","datePublished":"2026-07-06","publisher":{{"@type":"Organization","name":"Payment Card Services","url":"{DOMAIN}"}}}}
  </script>
{FAQ_STYLE}
{HEAD_LINKS}
</head>
<body>
{NAV}
<section style="padding:80px 0 20px;background:var(--light);">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8 text-center reveal">
        <span class="sec-badge">GUIDE</span>
        <h1 class="sec-title" style="margin-top:16px;">{page['h1']}</h1>
        <p style="color:var(--muted);font-size:1.1rem;margin-top:12px;max-width:620px;margin-left:auto;margin-right:auto;">{page['sub']}</p>
      </div>
    </div>
  </div>
</section>
<section style="padding:20px 0;">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <div class="blog-content reveal">
          {page['body']}
          <div class="mt-5 p-4" style="background:var(--light);border-radius:12px;border:1px solid var(--border);">
            <h4 style="font-weight:700;color:var(--green);margin-bottom:12px;">Ready to get your free card machine?</h4>
            <p style="color:var(--muted);margin-bottom:16px;">Zero monthly rental. Next-day payouts. 24/7 UK support. It takes minutes to get started.</p>
            <a href="#enquire" class="btn-solid">Claim Your Free Card Machine <i class="fas fa-arrow-right"></i></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
{ENQUIRY_FORM}
{FOOTER}
{SCROLL_BTN}
{JS}
</body>
</html>"""

def main():
    count = 0
    for page in PAGES:
        fname = f"{page['slug']}.html"
        with open(os.path.join(BASE_DIR, fname), "w", encoding="utf-8") as f:
            f.write(build_page(page))
        print(f"  Created: {fname}"); count += 1
    print(f"\nDone — {count} blog/FAQ pages generated.")
    print("\nSitemap entries:")
    for page in PAGES:
        print(f'  <url><loc>{DOMAIN}/{page["slug"]}</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>0.80</priority></url>')

if __name__ == "__main__":
    main()
