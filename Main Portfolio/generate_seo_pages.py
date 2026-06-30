"""Generate Dean Burt portfolio location SEO pages — run once then delete."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOCATIONS = [
    {
        "slug": "london",
        "city": "London",
        "region": "UK",
        "desc": "London is the UK's most competitive market for digital talent — and the best businesses know that a strong web presence is the foundation of growth. Whether you're a startup in Shoreditch, a law firm in the City, or a retailer in Notting Hill, your website is your most important business asset.",
        "why": "Working with a freelance developer in London means faster communication, the ability to meet in person, and someone who understands the pace and expectations of the London market. Dean works with London businesses who need professional, high-performance websites built quickly and without agency markups.",
    },
    {
        "slug": "manchester",
        "city": "Manchester",
        "region": "North West England",
        "desc": "Manchester's digital economy is booming — from MediaCity's creative sector to the Northern Quarter's independent business community. Businesses across Manchester are investing in web presence to compete locally and nationally, and the demand for skilled freelance developers has never been higher.",
        "why": "Dean builds websites and web apps for Manchester businesses remotely, delivering the same quality as a city-centre agency at a fraction of the cost. Fast turnarounds, clear communication, and results-focused development.",
    },
    {
        "slug": "birmingham",
        "city": "Birmingham",
        "region": "West Midlands",
        "desc": "Birmingham is the UK's second-largest city and its economy is growing fast. With one of the youngest populations in Europe and a thriving SME sector, demand for web development services across the West Midlands is consistent and growing. Businesses in Digbeth, Jewellery Quarter, and beyond are increasingly investing in professional digital presence.",
        "why": "Dean partners with Birmingham businesses to build fast, mobile-first websites and web applications — delivered remotely with the responsiveness and communication you'd expect from a local developer.",
    },
    {
        "slug": "leeds",
        "city": "Leeds",
        "region": "West Yorkshire",
        "desc": "Leeds has built one of the most impressive digital and creative sectors outside London. The city's tech community, independent retail culture, and growing financial services sector all drive consistent demand for skilled web development. From LS1 startups to established South Yorkshire firms, the appetite for quality web work is strong.",
        "why": "Dean works with Leeds businesses who want websites and applications built properly — clean code, mobile performance, and an outcome-focused approach rather than agency process.",
    },
    {
        "slug": "bristol",
        "city": "Bristol",
        "region": "South West England",
        "desc": "Bristol's creative and tech economy is thriving. The city has developed a well-earned reputation for innovation — from its independent retail sector to its growing number of tech companies and startups. Clifton, Stokes Croft, and the wider Bristol area are full of businesses that take their digital presence seriously.",
        "why": "Dean delivers remote web development for Bristol businesses who need high-quality, well-built websites and web apps — without the wait times or overhead costs of a large agency.",
    },
    {
        "slug": "edinburgh",
        "city": "Edinburgh",
        "region": "Scotland",
        "desc": "Edinburgh's economy spans tourism, financial services, tech, and the creative industries. The city hosts thousands of ambitious businesses — from Festival Fringe hospitality to financial firms on Charlotte Square — all of which depend on a polished web presence to compete. The Scottish capital is a strong market for skilled web development.",
        "why": "Dean builds websites and web applications for Edinburgh businesses remotely, offering the quality of a specialist developer without the cost of a city-centre agency. Clear deliverables, fast turnaround, professional results.",
    },
    {
        "slug": "glasgow",
        "city": "Glasgow",
        "region": "Scotland",
        "desc": "Glasgow is Scotland's commercial heart — a city with serious business ambition and a creative culture that punches above its weight. From the Merchant City's hospitality sector to the West End's independent businesses and the city's growing tech community, demand for professional web development in Glasgow is robust and growing.",
        "why": "Dean works with Glasgow businesses who are serious about their online presence and want development done right the first time — built for performance, mobile users, and long-term growth.",
    },
    {
        "slug": "brighton",
        "city": "Brighton",
        "region": "South East England",
        "desc": "Brighton is one of the UK's most digitally-savvy cities — home to a thriving creative tech community, a strong independent business culture, and clients who have high expectations of what a website should look and feel like. The Brighton and Hove market rewards quality and penalises anything that looks generic.",
        "why": "Dean builds websites and apps for Brighton businesses that match the quality the city demands — distinctive, performance-driven, and built around conversion rather than just aesthetics.",
    },
    {
        "slug": "cambridge",
        "city": "Cambridge",
        "region": "East England",
        "desc": "Cambridge's economy is built on knowledge — from the University's research commercialisation to the Silicon Fen tech cluster. Businesses and startups operating in Cambridge have some of the most discerning clients in the country, and their websites need to match. A well-built web presence is table stakes in Cambridge's competitive professional market.",
        "why": "Dean develops clean, technically strong websites and applications for Cambridge businesses and startups — the kind of work that impresses technical founders and professional clients alike.",
    },
    {
        "slug": "oxford",
        "city": "Oxford",
        "region": "South East England",
        "desc": "Oxford is a global brand in its own right — a city of academic excellence, innovation, and high-value professional services. Businesses operating in Oxford, from life sciences firms to independent retailers in the Covered Market, are expected to present themselves to an international standard. A mediocre website is a credibility problem in Oxford.",
        "why": "Dean builds websites for Oxford businesses that reflect the professional standards the city demands — technically sound, well-designed, and built for performance across all devices.",
    },
    {
        "slug": "liverpool",
        "city": "Liverpool",
        "region": "North West England",
        "desc": "Liverpool has reinvented itself as a creative, hospitality, and commercial powerhouse. The city's independent culture, growing startup scene, and tourism economy all demand professional digital presence from businesses that want to compete. Whether it's the Baltic Triangle's tech firms or city-centre retailers, web quality matters in Liverpool.",
        "why": "Dean works with Liverpool businesses remotely, delivering websites and web applications that reflect genuine development skill rather than template-based solutions — at freelance rates rather than agency prices.",
    },
    {
        "slug": "sheffield",
        "city": "Sheffield",
        "region": "South Yorkshire",
        "desc": "Sheffield has quietly built one of the most robust SME economies in the North of England. Its manufacturing heritage has been joined by a growing creative and digital sector, a vibrant independent retail community, and two major universities that generate constant demand for web services. Sheffield businesses that invest in quality web development consistently outperform those that don't.",
        "why": "Dean builds professional websites and web apps for Sheffield businesses — working remotely with clear scope, honest communication, and delivery that actually matches what was agreed.",
    },
    {
        "slug": "newcastle",
        "city": "Newcastle",
        "region": "North East England",
        "desc": "Newcastle upon Tyne is the North East's commercial hub — a city with ambition, a growing tech scene, and a business community that's increasingly serious about digital. From Quayside businesses to the Ouseburn Valley's creative cluster, Newcastle companies are investing in better web presence to compete regionally and nationally.",
        "why": "Dean delivers remote web development for Newcastle businesses who want proper, professionally built websites and applications — not template sites dressed up as bespoke work.",
    },
    {
        "slug": "nottingham",
        "city": "Nottingham",
        "region": "East Midlands",
        "desc": "Nottingham has a diverse and growing business economy — from its retail and hospitality sector to its tech and life sciences community. Two major universities give the city a constant stream of talent and a culture of innovation. Businesses across Nottingham and the East Midlands are investing in web presence to stay competitive both locally and online.",
        "why": "Dean works with Nottingham businesses who want websites built to a professional standard — mobile-first, fast-loading, and designed to convert visitors into enquiries or sales.",
    },
    {
        "slug": "leicester",
        "city": "Leicester",
        "region": "East Midlands",
        "desc": "Leicester is one of the most diverse and commercially active cities in the UK. Its retail and wholesale sector, professional services community, and growing tech industry all depend on strong digital presence. The city's entrepreneurial culture means high demand for quality web development at competitive freelance rates.",
        "why": "Dean builds websites and web applications for Leicester businesses — delivering professional results remotely with the kind of personal attention and responsiveness that agencies rarely provide.",
    },
    {
        "slug": "reading",
        "city": "Reading",
        "region": "Berkshire",
        "desc": "Reading is the UK's most important tech hub outside London — home to major corporate headquarters and a thriving SME sector that spans software, professional services, and retail. Businesses in Reading have direct London-market expectations for their web presence, without always wanting to pay London agency prices.",
        "why": "Dean works with Reading businesses and startups who need websites and applications built to a high technical standard — professionally designed, well-coded, and ready to scale.",
    },
    {
        "slug": "southampton",
        "city": "Southampton",
        "region": "Hampshire",
        "desc": "Southampton is a major commercial port city with a diverse economy spanning maritime, hospitality, retail, and a growing tech sector. The University of Southampton adds a significant research and startup dimension. Businesses across Hampshire are increasingly prioritising web quality as competition for online visibility intensifies.",
        "why": "Dean delivers professional web development for Southampton businesses remotely — building websites and applications that perform well in search, work perfectly on mobile, and represent the business properly.",
    },
    {
        "slug": "coventry",
        "city": "Coventry",
        "region": "West Midlands",
        "desc": "Coventry's City of Culture legacy has accelerated investment in the city's creative and commercial infrastructure. A growing young population, regenerating city centre, and expanding business community make it one of the UK's most interesting cities for digital development. Businesses in Coventry are increasingly aware that web quality directly affects growth.",
        "why": "Dean builds websites and web apps for Coventry businesses who want proper development rather than off-the-shelf templates — built for their specific goals, delivered on time, and maintained with honest support.",
    },
    {
        "slug": "milton-keynes",
        "city": "Milton Keynes",
        "region": "Buckinghamshire",
        "desc": "Milton Keynes is one of the UK's fastest-growing cities — a planned business hub with excellent transport links, a growing corporate presence, and a young, digitally-literate population. Businesses across MK and Buckinghamshire are investing in web presence to compete nationally, and the demand for skilled freelance web developers is strong.",
        "why": "Dean works with Milton Keynes businesses remotely, delivering professional websites and web applications that match the city's fast-moving, commercially-focused business environment.",
    },
    {
        "slug": "east-london",
        "city": "East London",
        "region": "London",
        "desc": "East London is one of the most dynamic business environments in the UK. From Shoreditch's startup ecosystem to Stratford's post-Olympic regeneration, Canary Wharf's financial sector, and the thriving independent businesses of Hackney and Bethnal Green — East London demands and rewards digital excellence. It's where Dean is based, and the market he knows best.",
        "why": "As an East London-based developer, Dean brings genuine local knowledge and the option for in-person meetings alongside remote work. He's built websites for businesses across E1 to E20 and understands the mix of tech-savvy clients and community-focused businesses that make East London unique.",
    },
]

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./index.css">"""

STYLES_EXTRA = """
  <style>
    .seo-hero { padding: calc(var(--nav-h) + 5rem) clamp(1.5rem,6vw,5rem) 5rem; max-width: 860px; }
    .seo-hero .eyebrow { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent); margin-bottom: 1.2rem; }
    .seo-hero h1 { font-family: var(--font-display); font-size: clamp(3rem, 10vw, 7rem); line-height: 0.95; letter-spacing: 0.02em; margin-bottom: 1.5rem; }
    .seo-hero h1 span { color: var(--accent); }
    .seo-hero .tagline { font-size: clamp(1rem, 2.5vw, 1.2rem); color: var(--muted); max-width: 560px; margin-bottom: 2.5rem; font-weight: 300; }
    .seo-ctas { display: flex; gap: 1rem; flex-wrap: wrap; }
    .seo-section { max-width: 860px; margin: 0 auto; padding: 4rem clamp(1.5rem,6vw,5rem); border-top: 1px solid var(--border); }
    .seo-section .label { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--accent); margin-bottom: 1rem; }
    .seo-section h2 { font-family: var(--font-display); font-size: clamp(2rem, 6vw, 3.5rem); line-height: 1; margin-bottom: 1.5rem; }
    .seo-section p { color: var(--muted); font-weight: 300; max-width: 680px; margin-bottom: 1.2rem; font-size: 1.05rem; }
    .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1px; border: 1px solid var(--border); margin: 2.5rem 0; }
    .service-cell { background: var(--surface); padding: 2rem 1.75rem; border-right: 1px solid var(--border); }
    .service-cell:last-child { border-right: none; }
    .service-num { font-family: var(--font-mono); font-size: 0.65rem; color: var(--accent); letter-spacing: 0.15em; margin-bottom: 0.75rem; }
    .service-cell h3 { font-family: var(--font-display); font-size: 1.4rem; margin-bottom: 0.6rem; }
    .service-cell p { font-size: 0.9rem; color: var(--muted); margin: 0; font-weight: 300; }
    .tech-row { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.5rem; }
    .tech-chip { background: var(--surface2); border: 1px solid var(--border); border-radius: var(--radius); padding: 0.35rem 0.8rem; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.06em; color: var(--muted); }
    .cta-block { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid var(--accent); padding: 3rem clamp(1.5rem,5vw,4rem); margin: 3rem 0; }
    .cta-block h2 { font-family: var(--font-display); font-size: clamp(2rem,5vw,3rem); margin-bottom: 1rem; }
    .cta-block p { color: var(--muted); font-weight: 300; margin-bottom: 2rem; max-width: 500px; }
    .back-link { display: inline-block; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); text-decoration: none; margin: 2rem clamp(1.5rem,6vw,5rem); transition: color 0.2s; }
    .back-link:hover { color: var(--accent); }
    @media (max-width: 600px) { .seo-section { padding: 3rem 1.5rem; } .services-grid { grid-template-columns: 1fr; } .service-cell { border-right: none; border-bottom: 1px solid var(--border); } }
  </style>"""

NAV_HTML = """  <nav id="mainNav">
    <a class="nav-logo" href="/">Dean<span>.</span></a>
    <ul class="nav-links">
      <li><a href="/#projects">Work</a></li>
      <li><a href="/#about">About</a></li>
      <li><a href="/#skills">Skills</a></li>
      <li><a href="/#contact">Contact</a></li>
    </ul>
    <button class="burger" id="burger" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </nav>"""

FOOTER_HTML = """  <footer>
    <p>© 2026 Dean Burt. All rights reserved.</p>
    <a href="/">Back to portfolio ↑</a>
  </footer>"""


def build_page(loc):
    city = loc["city"]
    slug = loc["slug"]
    region = loc["region"]
    desc = loc["desc"]
    why = loc["why"]

    keywords = ", ".join([
        f"freelance web developer {city}",
        f"website design {city}",
        f"web designer {city}",
        f"frontend developer {city}",
        f"web developer {city}",
        f"hire web developer {city}",
        f"website builder {city}",
        f"React developer {city}",
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Freelance Web Developer {city} | Dean Burt</title>
  <meta name="description" content="Dean Burt is a freelance web developer based in London available for projects in {city}. Websites, React apps, and full-stack builds. Clean code, fast delivery, no agency fees.">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="Dean Burt">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://dean1234533.github.io/freelance-web-developer-{slug}">
  <meta property="og:title" content="Freelance Web Developer {city} | Dean Burt">
  <meta property="og:description" content="Freelance web developer available for {city} projects. Websites, React apps, and full-stack development. No agency fees.">
  <meta property="og:url" content="https://dean1234533.github.io/freelance-web-developer-{slug}">
  <meta property="og:type" content="website">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Dean Burt — Freelance Web Developer",
    "description": "Freelance frontend and full-stack web developer available for projects in {city}. Specialising in React, JavaScript, HTML/CSS, and Firebase.",
    "url": "https://dean1234533.github.io",
    "telephone": "",
    "email": "Deanburt1308@gmail.com",
    "areaServed": {{"@type": "City", "name": "{city}"}},
    "priceRange": "££",
    "sameAs": ["https://www.linkedin.com/in/dbwebdev/", "https://github.com/dean1234533"]
  }}
  </script>
{HEAD_COMMON}{STYLES_EXTRA}
</head>
<body>

{NAV_HTML}

  <div class="seo-hero">
    <p class="eyebrow">Freelance Web Developer &middot; {city}</p>
    <h1>Web Dev<br><span>{city}</span></h1>
    <p class="tagline">Professional websites and web applications for {city} businesses — built clean, fast, and without agency overhead.</p>
    <div class="seo-ctas">
      <a class="btn-primary" href="/#contact">Start a Project</a>
      <a class="btn-outline" href="/#projects">View My Work</a>
    </div>
  </div>

  <section class="seo-section">
    <p class="label">The Market</p>
    <h2>Web Development<br>in {city}</h2>
    <p>{desc}</p>
  </section>

  <section class="seo-section">
    <p class="label">Services</p>
    <h2>What I Build</h2>
    <div class="services-grid">
      <div class="service-cell">
        <p class="service-num">01</p>
        <h3>Websites</h3>
        <p>Fast, mobile-first websites built for real-world performance — designed to represent your business properly and convert visitors.</p>
      </div>
      <div class="service-cell">
        <p class="service-num">02</p>
        <h3>React Apps</h3>
        <p>Interactive web applications built with React — dashboards, booking systems, client portals, and custom tools.</p>
      </div>
      <div class="service-cell">
        <p class="service-num">03</p>
        <h3>Full-Stack</h3>
        <p>End-to-end development with Firebase, Supabase, or custom backends — auth, databases, APIs, and deployment included.</p>
      </div>
    </div>
    <div class="tech-row">
      <span class="tech-chip">HTML5</span>
      <span class="tech-chip">CSS3</span>
      <span class="tech-chip">JavaScript</span>
      <span class="tech-chip">React</span>
      <span class="tech-chip">Firebase</span>
      <span class="tech-chip">Supabase</span>
      <span class="tech-chip">Vercel</span>
      <span class="tech-chip">Cloudflare</span>
    </div>
  </section>

  <section class="seo-section">
    <p class="label">Why Dean</p>
    <h2>Working With<br>{city} Businesses</h2>
    <p>{why}</p>
    <p>Every project starts with a clear brief and ends with a working product — no scope creep, no endless revisions, no disappearing after handoff. Just professional web development delivered by someone who takes pride in the work.</p>
  </section>

  <section class="seo-section">
    <div class="cta-block">
      <h2>Ready to Build<br>Something?</h2>
      <p>Get in touch to discuss your project. I work with {city} businesses remotely and respond within 24 hours.</p>
      <a class="btn-primary" href="mailto:Deanburt1308@gmail.com">Deanburt1308@gmail.com</a>
    </div>
  </section>

  <a class="back-link" href="/">← Back to portfolio</a>

{FOOTER_HTML}

  <script src="./index.js"></script>
</body>
</html>"""


def main():
    for loc in LOCATIONS:
        filename = f"freelance-web-developer-{loc['slug']}.html"
        filepath = os.path.join(BASE_DIR, filename)
        html = build_page(loc)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  Created: {filename}")
    print(f"\nDone — {len(LOCATIONS)} pages generated.")


if __name__ == "__main__":
    main()
