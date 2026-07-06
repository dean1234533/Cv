"""Generate new industry SEO pages for Payment Card Services — run once."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FORMSPREE_ID = "mjgzzowv"
DOMAIN       = "https://www.paymentcardservices.co.uk"
EMAIL        = "lee.eubank@dojo.tech"

NEW_INDUSTRIES = [
    # ── AUTOMOTIVE ──────────────────────────────────────────────────────────────
    {
        "slug": "mechanics-and-car-garages",
        "industry": "Mechanics & Car Garages",
        "headline": "Free Card Machines for Mechanics & Car Garages",
        "icon": "fa-wrench",
        "desc": "Independent mechanics and car garages handle large, irregular payments — a service can run from £100 to well over £1,000 — and customers increasingly expect to pay by card. Whether you're a sole trader working from a unit or a multi-bay garage with a team, the cost of accepting those payments shouldn't eat into your margins. A monthly rental fee on your card machine is a fixed overhead that serves your provider, not your business.",
        "why": "DOJO card machines are a natural fit for garages — robust, portable enough to bring to the customer's car, and reliable with dual WiFi/4G connectivity. Next-day payouts mean that money from a job on Monday is in your account on Tuesday. No monthly rental means you're only ever paying when you're taking money in.",
        "pain_point": "Most garages are paying a monthly rental fee they signed up for years ago and never thought to question. It's one of the easiest costs to cut.",
    },
    {
        "slug": "car-servicing-and-mot-centres",
        "industry": "Car Servicing & MOT Centres",
        "headline": "Free Card Machines for Car Servicing & MOT Centres",
        "icon": "fa-car",
        "desc": "Car servicing and MOT centres process consistent, predictable payments — mostly card. Customers bringing in their car for a service or MOT expect to pay quickly and professionally when they collect. The payment experience reflects on your business, and a reliable card machine is a basic expectation. What shouldn't be expected is paying a monthly rental fee on top of your transaction costs.",
        "why": "DOJO card machines work perfectly at the service desk — fast, clean transactions, all cards and contactless wallets accepted. Next-day payouts give you a predictable cash flow week to week, and 24/7 UK support means any issue gets resolved without downtime. Zero monthly rental means your fixed costs stay low even in quieter months.",
        "pain_point": "MOT centres and service garages often run on tight margins. A monthly card machine rental fee is a small but unnecessary cost that compounds every month.",
    },
    {
        "slug": "vehicle-paint-and-spray-shops",
        "industry": "Vehicle Paint & Spray Shops",
        "headline": "Free Card Machines for Vehicle Paint & Spray Shops",
        "icon": "fa-spray-can",
        "desc": "Vehicle paint and spray shops handle high-value, one-off payments — bodywork repairs and full resprays can run into hundreds or thousands of pounds. Customers collecting their vehicle expect a smooth, professional payment experience. For shops doing consistent work, the cost-per-transaction matters, and any unnecessary fixed cost — like a monthly card machine rental — directly affects what you keep.",
        "why": "DOJO card machines handle high-value transactions reliably and professionally — exactly what a spray shop needs when a customer is paying a large bill. Dual connectivity means no connectivity failures at the checkout. Next-day payouts help with parts purchasing and supplier payments. No rental means your payment setup is as lean as your operation.",
        "pain_point": "Spray shops often process fewer but larger transactions. A monthly rental fee is a fixed cost regardless of how busy you are — with DOJO, you only pay when you take money.",
    },
    {
        "slug": "tyre-shops",
        "industry": "Tyre Shops",
        "headline": "Free Card Machines for Tyre Shops",
        "icon": "fa-circle",
        "desc": "Tyre shops — whether fitting centres, mobile tyre fitters, or tyre retailers — handle a high volume of moderate-sized transactions throughout the day. Speed at the point of sale matters; customers want to pay and get back on the road. Every tyre shop in the UK is paying a transaction rate — the question is whether they're also paying a monthly rental fee on top of it when they don't need to.",
        "why": "DOJO card machines are fast at the point of sale — exactly what a busy tyre fitting bay needs. Dual WiFi/4G connectivity keeps you taking payments even in workshop environments with patchy WiFi. Next-day payouts keep your tyre stock purchasing cash flow consistent. No monthly rental means your cost of taking payments is purely transaction-based.",
        "pain_point": "Most tyre shops are on provider contracts they set up when they opened. Many of those contracts include monthly rental fees that have never been reviewed.",
    },
    {
        "slug": "vehicle-accessories",
        "industry": "Vehicle Accessories Stores",
        "headline": "Free Card Machines for Vehicle Accessories Stores",
        "icon": "fa-car-side",
        "desc": "Vehicle accessories stores — whether standalone retailers or workshop-attached shops selling dash cams, seat covers, matting, or performance parts — handle frequent card transactions throughout the day. Like any retail business, the cost of accepting payments directly affects margins. A monthly card machine rental fee is a fixed cost that adds up over a year without providing anything in return.",
        "why": "DOJO card machines are straightforward retail payment solutions — fast, reliable, and compatible with all cards and contactless wallets. The DOJO app gives you real-time transaction reporting, and next-day payouts keep your stock-buying cash flow healthy. With no monthly rental, your payment setup costs scale with your turnover rather than running as a fixed overhead.",
        "pain_point": "Vehicle accessories retailers are often paying for card machine rental as part of a bundle they didn't fully understand when they signed up. A zero-rental alternative is available.",
    },
    {
        "slug": "car-parts-stores",
        "industry": "Car Parts Stores",
        "headline": "Free Card Machines for Car Parts Stores",
        "icon": "fa-cogs",
        "desc": "Car parts stores serve both trade customers and the public, processing a high volume of transactions at varying price points throughout the day. Trade accounts aside, cash is declining fast among the general public, and mechanics buying parts on behalf of customers increasingly pay by card. A reliable, cost-effective payment setup is non-negotiable — and a monthly rental fee is the first thing to eliminate.",
        "why": "DOJO card machines handle both quick, low-value transactions and larger trade orders efficiently. The dual WiFi/4G connectivity ensures you're never offline when a mechanic needs to pay fast. Next-day payouts keep your supplier payments on track. No monthly rental means your payment costs only run when your till is running.",
        "pain_point": "Car parts stores often have multiple transaction types and busy peaks. Paying a fixed monthly rental on top of transaction fees is an avoidable cost.",
    },
    {
        "slug": "tyre-retailers",
        "industry": "Tyre Retailers",
        "headline": "Free Card Machines for Tyre Retailers",
        "icon": "fa-circle-dot",
        "desc": "Tyre retailers — selling tyres wholesale, retail, or online with in-person collection — process a consistent volume of card payments from both trade and consumer customers. Whether you're a dedicated tyre retailer or a parts distributor with a tyre range, the economics of your payment processing matter. Every month you're paying a rental fee is a month you're subsidising your card machine provider.",
        "why": "DOJO card machines are well-suited to the tyre retail environment — straightforward, reliable, and compatible with all payment types. The DOJO portal gives you full transaction visibility, and next-day payouts mean you're never waiting for your money after a busy day. Zero monthly rental means your payment costs are fully variable — no payment, no fee.",
        "pain_point": "Tyre retailers who set up their payment processing through a bank or high-street provider are almost certainly paying more than they need to.",
    },

    # ── BAKERIES & SPECIALIST FOODS ─────────────────────────────────────────────
    {
        "slug": "bakeries-and-patisseries",
        "industry": "Bakeries & Patisseries",
        "headline": "Free Card Machines for Bakeries & Patisseries",
        "icon": "fa-bread-slice",
        "desc": "Bakeries and patisseries run on high transaction volumes and relatively low average order values — which makes the cost of each transaction, and every fixed fee on top of it, matter more than most. Customers at the counter expect to tap and go; they rarely carry cash. For independent bakers and patisserie owners, a monthly rental fee on a card machine is an unnecessary overhead that comes straight off the bottom line.",
        "why": "DOJO card machines are fast at the counter — critical for bakeries with queue-sensitive morning rushes. Tap-to-pay on all contactless cards and wallets, next-day payouts, and a simple DOJO app for reporting. No monthly rental means your payment setup costs you only when you're actually selling — perfectly aligned with how a bakery operates.",
        "pain_point": "Many bakery owners are paying monthly rental fees they didn't fully realise were in their original contract. It's one of the first costs worth revisiting.",
    },
    {
        "slug": "ice-cream-parlours",
        "industry": "Ice Cream Parlours",
        "headline": "Free Card Machines for Ice Cream Parlours",
        "icon": "fa-ice-cream",
        "desc": "Ice cream parlours and gelaterias depend on footfall, speed at the counter, and a seamless customer experience. Low average transaction values mean every pence of processing cost counts — and a monthly rental fee on your card machine is a fixed overhead that doesn't vary with your seasonal trade. Slower months should cost you less. With a zero-rental card machine, they do.",
        "why": "DOJO card machines handle fast, contactless transactions perfectly — ideal for a busy ice cream counter in summer. No monthly rental means you're not paying a fixed fee during slower winter months. Next-day payouts keep your cash flow consistent, and 24/7 UK support is there if anything goes wrong during a peak trading day.",
        "pain_point": "Ice cream parlours are highly seasonal. Paying a monthly rental fee year-round when your trade is concentrated in a few peak months is a cost that doesn't need to exist.",
    },
    {
        "slug": "dessert-parlours",
        "industry": "Dessert Parlours",
        "headline": "Free Card Machines for Dessert Parlours",
        "icon": "fa-cookie",
        "desc": "Dessert parlours — serving waffles, sundaes, crepes, bubble waffles, and more — attract a young, cashless demographic that almost exclusively pays by card or phone. Transaction volumes are high during evenings and weekends, and speed at the till is critical when queues build. A card machine that's slow, unreliable, or expensive to run works against the experience you're trying to create.",
        "why": "DOJO card machines are built for the pace of an evening dessert service — fast contactless payments, all wallets accepted including Apple Pay and Google Pay, and dual WiFi/4G so you never go offline mid-rush. Next-day payouts and zero monthly rental mean your payment costs are lean and your cash flow stays healthy.",
        "pain_point": "Dessert parlours often attract younger, entirely cashless customers. If your card machine is slow or unreliable, you're losing sales. And if you're paying monthly rental on top of that, you're paying twice.",
    },
    {
        "slug": "cookie-doughnut-and-cake-stores",
        "industry": "Cookie, Doughnut & Cake Stores",
        "headline": "Free Card Machines for Cookie, Doughnut & Cake Stores",
        "icon": "fa-cookie-bite",
        "desc": "Specialist sweet bakeries — cookie shops, doughnut stores, custom cake studios, and pie shops — typically run high volumes of small card transactions throughout the day. Customers at the counter expect a quick, smooth payment experience, and they almost never use cash. For small business owners in this space, cutting unnecessary fixed costs — like monthly card machine rental — is one of the most direct ways to improve profitability.",
        "why": "DOJO card machines handle rapid, low-value transactions efficiently — exactly what a queue at a doughnut counter needs. Tap-to-pay works for every card and contactless wallet, speeding up each transaction. No monthly rental keeps your payment costs proportional to your revenue, and next-day payouts mean you're not waiting on your money.",
        "pain_point": "Cookie and doughnut stores live and die on throughput speed. A slow or costly card machine is a friction point that costs you both in lost sales and unnecessary fees.",
    },
    {
        "slug": "pastry-shops",
        "industry": "Pastry Shops",
        "headline": "Free Card Machines for Pastry Shops",
        "icon": "fa-utensils",
        "desc": "Pastry shops — croissanteries, viennoiserie specialists, and continental-style bake shops — attract customers who expect a premium, frictionless experience from arrival to payment. Cash is rarely expected. For artisan pastry businesses, the card machine is a front-of-house tool that reflects your brand — and the cost of running it reflects on your margin. An unnecessary monthly rental fee doesn't fit either equation.",
        "why": "DOJO card machines are clean, modern payment terminals that present well in a high-quality retail environment. Fast transactions, all payment methods accepted, next-day payouts, and zero monthly rental. The DOJO app gives you real-time visibility of your daily takings — useful for a business where morning sales volumes tell the whole story.",
        "pain_point": "Artisan pastry shops often operate on tight margins. A monthly rental fee on a card machine is a small cost with a big principle: you're paying for something you don't need to pay for.",
    },
    {
        "slug": "cheese-and-dairy-shops",
        "industry": "Cheese & Dairy Shops",
        "headline": "Free Card Machines for Cheese & Dairy Shops",
        "icon": "fa-cheese",
        "desc": "Specialist cheese and dairy retailers — delis, fromageries, and farm shops — typically carry high average order values and a customer base that's entirely comfortable paying by card. Whether you're a market stall, a fixed retail unit, or both, reliable payment processing is essential. And with customers often spending significant amounts on quality products, a smooth card payment experience is part of delivering the premium service they expect.",
        "why": "DOJO card machines work equally well in fixed retail and on market stalls — compact, dual WiFi/4G connected, and portable enough to use anywhere. For farm shops or market traders who sell in locations without reliable broadband, the 4G SIM backup is particularly valuable. Next-day payouts and no monthly rental keep your operating costs lean.",
        "pain_point": "Cheese and dairy specialists — especially those who trade at farmers' markets — often struggle with connectivity. DOJO's dual connection handles this automatically, with no extra cost.",
    },

    # ── HOSPITALITY / ALCOHOL ────────────────────────────────────────────────────
    {
        "slug": "pubs-alehouses-and-taprooms",
        "industry": "Pubs, Ale Houses & Tap Rooms",
        "headline": "Free Card Machines for Pubs, Ale Houses & Tap Rooms",
        "icon": "fa-beer-mug-empty",
        "desc": "Pubs, ale houses, and tap rooms are among the highest-volume card payment environments in the UK. From a quiet Tuesday lunchtime to a packed Friday night, the card machine never stops. For licensees managing tight margins — beer duty, rent, staff costs — a monthly card machine rental fee is a fixed overhead that stacks up fast. It's also one of the most straightforward costs to eliminate.",
        "why": "DOJO card machines are built for the pace and pressure of pub service — fast transactions, dual WiFi/4G so you never drop offline mid-service, and next-day payouts that keep your brewery account funded. Multiple machines can be deployed on the same account. Zero monthly rental means your payment infrastructure doesn't cost you anything in slow trading weeks.",
        "pain_point": "Most licensees are on card machine contracts that date back years, often tied to their bank or their till system supplier. Those contracts almost always include rental fees that no longer need to exist.",
    },
    {
        "slug": "wine-bars",
        "industry": "Wine Bars",
        "headline": "Free Card Machines for Wine Bars",
        "icon": "fa-wine-glass",
        "desc": "Wine bars operate on higher average transaction values and an entirely card-paying clientele. Customers expect a premium, unhurried payment experience — one that matches the environment they've chosen to spend their evening in. A card machine that fails mid-service or slows down a busy Friday evening service is not an option. Neither is paying a monthly rental fee that adds nothing to your operation.",
        "why": "DOJO card machines are a clean, professional payment solution that fits the wine bar environment — fast, reliable, and accepting all cards and contactless wallets. Dual connectivity means service never drops. Next-day payouts keep your supplier account funded. And with zero monthly rental, your payment setup is as refined as your wine list.",
        "pain_point": "Wine bar operators often come from a hospitality background and inherited their payment setup from their fit-out. Many don't know a zero-rental alternative exists.",
    },
    {
        "slug": "cocktail-bars",
        "industry": "Cocktail Bars",
        "headline": "Free Card Machines for Cocktail Bars",
        "icon": "fa-martini-glass",
        "desc": "Cocktail bars run on high transaction volumes, high average spend, and a customer base that never pays in cash. From late-night service to private events and bottomless brunches, the payment infrastructure needs to keep pace. A card machine that goes offline on a Saturday night isn't just an inconvenience — it's lost revenue and a damaged reputation. And a monthly rental fee is money going out of your business every month regardless.",
        "why": "DOJO card machines are built for high-volume evening service — fast contactless transactions, dual WiFi/4G connectivity so you're never reliant on your broadband, and next-day payouts so Monday morning's float is always ready. Multiple machines, one account. No monthly rental means your fixed costs stay low even when you're not trading.",
        "pain_point": "Cocktail bars are a competitive, high-stakes environment. Every cost that isn't earning you something should be cut. A monthly card machine rental fee is exactly that cost.",
    },
    {
        "slug": "nightclubs",
        "industry": "Nightclubs",
        "headline": "Free Card Machines for Nightclubs",
        "icon": "fa-music",
        "desc": "Nightclubs and late-night venues process enormous volumes of card payments — at the bar, at the door, at cloakrooms, and in VIP areas. The entire operation runs on contactless payments, and any point-of-sale failure during peak hours is a serious revenue problem. Payment infrastructure in this environment needs to be bulletproof. And the cost of running it needs to be as low as possible given the margins involved.",
        "why": "DOJO card machines are designed for high-volume environments — fast, durable, and equipped with dual WiFi/4G so that if your venue's WiFi buckles under the load of a packed Saturday night, 4G automatically takes over. Multiple terminals on one account give you full coverage across the venue. Zero monthly rental per machine means deploying more machines doesn't proportionally increase your fixed costs.",
        "pain_point": "Nightclubs often run multiple card machines across different parts of the venue — each with its own rental fee. A zero-rental model changes the economics of running payment infrastructure at scale.",
    },
    {
        "slug": "breweries",
        "industry": "Breweries",
        "headline": "Free Card Machines for Breweries",
        "icon": "fa-barrel",
        "desc": "Breweries with taprooms, on-site shops, or tour operations need card payment infrastructure that works across multiple environments — from a tap room bar to a retail counter to a pop-up at a beer festival. The customer base is cashless and expects professional payment handling. Whether you're a microbrewery selling cans and growlers or a larger operation with a full hospitality offering, your payment costs should be as lean as your operation.",
        "why": "DOJO card machines are portable and dual-connected — perfect for taproom, retail, and event use. For brewery pop-ups and beer festivals where there's no reliable WiFi, the 4G SIM backup ensures you're always taking payments. Next-day payouts help with grain and hop purchasing, and zero monthly rental means your payment setup doesn't cost you anything between taproom events.",
        "pain_point": "Many breweries set up their payment processing as an afterthought. A quick review of what they're paying in rental fees often reveals a straightforward saving.",
    },
    {
        "slug": "off-licences-and-beer-stores",
        "industry": "Off Licences & Beer Stores",
        "headline": "Free Card Machines for Off Licences & Beer Stores",
        "icon": "fa-wine-bottle",
        "desc": "Off licences, beer and wine shops, and specialist alcohol retailers process a constant stream of card transactions throughout their trading hours. Customers expect tap-and-go payments, often on smaller purchases where a slow or unreliable card machine is a genuine barrier. For retailers operating on tight margins — especially independent off licences competing with supermarkets — every unnecessary fixed cost matters.",
        "why": "DOJO card machines are fast at the counter and accept all payment types — critical for a retail environment where transaction speed determines customer experience. Next-day payouts keep your supplier account funded without waiting. And with zero monthly rental, a smaller or quieter off licence isn't paying a fixed fee just to maintain the ability to take payments.",
        "pain_point": "Independent off licences often operate on thin margins. Monthly rental fees on card machines are one of the first costs that can be cut without any impact on service.",
    },

    # ── RETAIL & SPECIALIST STORES ───────────────────────────────────────────────
    {
        "slug": "bicycle-shops",
        "industry": "Bicycle Shops",
        "headline": "Free Card Machines for Bicycle Shops",
        "icon": "fa-bicycle",
        "desc": "Bicycle shops — selling bikes, parts, accessories, and offering repair services — handle a wide range of transaction values, from a few pounds for a tube to hundreds or thousands for a new bike. Customers are largely cashless, and the in-shop experience matters. For independent bike retailers competing with online sellers, keeping costs lean is essential — and a monthly card machine rental fee is a straightforward overhead to eliminate.",
        "why": "DOJO card machines handle both small workshop payments and large bike sales without any fuss. The DOJO app gives you real-time transaction visibility — useful for tracking workshop revenue separately from retail sales. Next-day payouts and zero monthly rental keep your cash flow healthy and your overheads low.",
        "pain_point": "Bike shops often have variable monthly income depending on season and repairs. A monthly rental fee is a fixed cost regardless of your turnover — a zero-rental model is more logical.",
    },
    {
        "slug": "electric-scooter-shops",
        "industry": "Electric Scooter Shops",
        "headline": "Free Card Machines for Electric Scooter Shops",
        "icon": "fa-person-biking",
        "desc": "Electric scooter retailers — selling e-scooters, e-bikes, and accessories — are a fast-growing retail segment handling high-value transactions. Customers purchasing an e-scooter or e-bike are spending significant money and expect a professional payment experience. For newer businesses in this space, keeping fixed costs low while building revenue is critical — and a monthly card machine rental fee is one of the first unnecessary costs to cut.",
        "why": "DOJO card machines are a natural fit for higher-value retail transactions — fast, professional, accepting all payment types. Dual connectivity means you're never offline during a sale. Next-day payouts are useful for a business that needs to replenish stock quickly after sales. Zero monthly rental means your payment infrastructure is lean from day one.",
        "pain_point": "Many electric scooter retailers are newer businesses that set up card payments quickly without shopping around. A zero-rental alternative is almost always available.",
    },
    {
        "slug": "butchers-and-fishmongers",
        "industry": "Butchers & Fishmongers",
        "headline": "Free Card Machines for Butchers & Fishmongers",
        "icon": "fa-drumstick-bite",
        "desc": "Butchers and fishmongers — whether high-street shops, market traders, or farm shop operations — process a high volume of card payments every day. Cash use among their customers has fallen sharply, and younger customers expect contactless as standard. For artisan butchers and fishmongers competing on quality and service, an unnecessary monthly rental fee on a card machine is a cost that cuts into the margin on every sale.",
        "why": "DOJO card machines work well in food retail environments — compact, easy to clean around, and reliable with dual WiFi/4G connectivity. For market-trading butchers or fishmongers where there's no reliable broadband, 4G ensures payments always go through. Next-day payouts and zero monthly rental are standard — no contracts that don't make sense for your business.",
        "pain_point": "Many traditional food retailers like butchers have only recently moved to card payments. Their first contract often included monthly rental fees they didn't know to question.",
    },
    {
        "slug": "frozen-meat-and-seafood-markets",
        "industry": "Frozen Meat & Seafood Markets",
        "headline": "Free Card Machines for Frozen Meat & Seafood Markets",
        "icon": "fa-fish",
        "desc": "Frozen meat and seafood markets — wholesale or retail — handle bulk purchases and high average order values. Customers doing a monthly or weekly shop are spending significant amounts and expecting to pay by card as a matter of course. For retailers in this space, the cost-per-transaction on large orders matters, and a monthly card machine rental fee is a fixed overhead with no justification.",
        "why": "DOJO card machines handle large transaction values smoothly and reliably. For markets in warehouses or industrial units where WiFi can be patchy, dual WiFi/4G connectivity ensures payments always process. Next-day payouts on large orders are particularly valuable for cash flow. Zero monthly rental means your payment setup is proportional to what you earn.",
        "pain_point": "Frozen food markets often deal in large basket sizes. Paying a rental fee on top of a transaction rate on every large order is a compounding cost that quickly adds up.",
    },

    # ── FOOD SERVICE ─────────────────────────────────────────────────────────────
    {
        "slug": "cafes-and-brasseries",
        "industry": "Cafés & Brasseries",
        "headline": "Free Card Machines for Cafés & Brasseries",
        "icon": "fa-mug-hot",
        "desc": "Cafés and brasseries process card payments constantly — from morning coffee runs to leisurely lunches, most customers pay by card or phone. Transaction speed matters during busy periods, and a card machine that slows down service costs you customers and revenue. For independent café owners, the economics of every transaction are tight — a monthly rental fee is a fixed cost that comes out of every cup of coffee you sell.",
        "why": "DOJO card machines are fast at the counter and at the table — critical for cafés where throughput speed matters as much as quality. Tap-to-pay on all cards and wallets, dual connectivity, and next-day payouts mean your payment setup works as hard as you do. And with zero monthly rental, your costs scale with your revenue rather than running as a fixed overhead.",
        "pain_point": "Many café owners set up their card machine through their coffee supplier or their bank and have never reviewed the contract. Monthly rental fees are almost always present — and almost always unnecessary.",
    },
    {
        "slug": "takeaways-and-fast-food",
        "industry": "Takeaways & Fast Food",
        "headline": "Free Card Machines for Takeaways & Fast Food",
        "icon": "fa-burger",
        "desc": "Takeaways and fast food businesses are among the highest card payment volumes per square metre of any retail environment. From lunchtime rushes to late-night service, the card machine is running constantly. Speed, reliability, and cost are the three things that matter most — and a monthly rental fee on top of your transaction rate is the cost that should be cut first.",
        "why": "DOJO card machines are built for fast, high-volume payment environments — contactless transactions in seconds, dual WiFi/4G so you never drop offline during service, and next-day payouts so your cash flow is always current. No monthly rental means that even on a quiet Monday you're not paying a fixed cost just to be able to take payments.",
        "pain_point": "Takeaway owners are often paying transaction rates and monthly fees through a provider tied to their EPOS system. That's two revenue streams for the provider, and one unnecessary cost for you.",
    },
    {
        "slug": "deli-and-sandwich-shops",
        "industry": "Deli & Sandwich Shops",
        "headline": "Free Card Machines for Deli & Sandwich Shops",
        "icon": "fa-sandwich",
        "desc": "Delis and sandwich shops operate on high volumes of lower-value transactions — a lunchtime queue of office workers paying £5–£10 each, several days a week. Speed at the till is everything. Customers expect tap and go, and anything that slows down the queue costs you sales. For deli owners, the cumulative cost of monthly card machine rental across 12 months is a straightforward overhead to eliminate.",
        "why": "DOJO card machines are ideal for the lunchtime rush — fast contactless payments, all wallets accepted, and the counter space to keep service flowing. Dual connectivity means the card machine keeps working even if your broadband has issues. Next-day payouts keep your supply runs funded. Zero monthly rental means your payment costs are purely variable.",
        "pain_point": "Deli and sandwich shops often have very high transaction counts but low margins. A monthly rental fee is a fixed drain on profit regardless of how well or badly you're trading.",
    },
    {
        "slug": "cafeterias-and-diners",
        "industry": "Cafeterias & Diners",
        "headline": "Free Card Machines for Cafeterias & Diners",
        "icon": "fa-utensils",
        "desc": "Cafeterias and diners — from workplace canteens to American-style diners and transport café operations — process high volumes of card payments across long trading hours. Customers at a cafeteria counter expect fast, frictionless payments. Whether it's a £4 breakfast or a £12 lunch, every transaction needs to be processed quickly without error. A monthly rental fee on the card machine is a cost that adds nothing to that experience.",
        "why": "DOJO card machines handle cafeteria-style service efficiently — fast transactions, all payment methods accepted, and dual connectivity for venues in locations where broadband can be unreliable (motorway services, industrial estates, transport hubs). Next-day payouts and zero monthly rental keep your operation lean and your cash flow predictable.",
        "pain_point": "Cafeterias serving a captive audience — whether in a business park, hospital, or transport hub — often have payment setups that haven't been reviewed in years. Those setups almost always include rental fees.",
    },

    # ── CLEANING SERVICES ────────────────────────────────────────────────────────
    {
        "slug": "carpet-and-upholstery-cleaning",
        "industry": "Carpet & Upholstery Cleaning",
        "headline": "Free Card Machines for Carpet & Upholstery Cleaners",
        "icon": "fa-broom",
        "desc": "Carpet and upholstery cleaning businesses — whether sole traders or small teams — collect payment at the end of a job, often in a customer's home. Clients expect to pay by card, and a mobile card machine is as essential as the cleaning equipment itself. For cleaning professionals collecting payments on the road, the portability and connectivity of a card machine matter enormously. So does what it costs to run.",
        "why": "DOJO card machines are compact and dual WiFi/4G connected — ideal for a cleaning professional collecting payment in a residential property. No need for the customer's WiFi; the 4G SIM handles it. Next-day payouts mean that money collected on a job today is in your account tomorrow. Zero monthly rental means your payment setup costs you nothing on days you're not working.",
        "pain_point": "Many carpet cleaners are either avoiding card payments because of the perceived cost, or using a card reader with a monthly fee they don't need to pay. A zero-rental alternative exists.",
    },
    {
        "slug": "carpet-and-flooring-repairs",
        "industry": "Carpet & Flooring Repairs",
        "headline": "Free Card Machines for Carpet & Flooring Repair Businesses",
        "icon": "fa-ruler-combined",
        "desc": "Carpet fitters, flooring installers, and repair specialists typically collect large, one-off payments at the end of a job. Customers want to pay by card when the work is done — increasingly, they won't have the cash. For tradespeople in this space, a mobile card machine is a professional necessity. The question is whether yours comes with a monthly rental fee it doesn't need.",
        "why": "DOJO card machines are portable and work anywhere with 4G coverage — no reliance on a customer's home WiFi to process a payment. Fast, professional card and contactless payments when the job is done, with next-day payouts so your material costs for the next job are funded quickly. Zero monthly rental fits the variable income pattern of project-based trade work.",
        "pain_point": "Flooring fitters who've avoided card machines because of setup costs or monthly fees are missing sales. The cost of getting started with DOJO is exactly zero — and so is the monthly rental.",
    },

    # ── CLOTHING & FASHION ───────────────────────────────────────────────────────
    {
        "slug": "clothing-stores",
        "industry": "Clothing Stores",
        "headline": "Free Card Machines for Clothing Stores",
        "icon": "fa-shirt",
        "desc": "Clothing stores — men's, women's, and family fashion — process constant card payments throughout their trading day. Whether it's a single item or a full outfit, customers pay by card. Cash is increasingly rare in fashion retail, particularly in high streets and shopping centres. For independent clothing retailers competing with national chains and online sellers, every unnecessary fixed cost erodes the margin that keeps you competitive.",
        "why": "DOJO card machines are a clean, professional solution for fashion retail — fast transactions at the till, all cards and contactless wallets accepted, and the DOJO app for daily sales reporting. Next-day payouts keep your stock buying power healthy. Zero monthly rental means your payment setup costs are purely proportional to what you sell.",
        "pain_point": "Many independent clothing retailers are on merchant service contracts that include monthly rental fees alongside their transaction rates. A zero-rental alternative is available — and switching is straightforward.",
    },
    {
        "slug": "fashion-and-accessories",
        "industry": "Fashion & Accessories",
        "headline": "Free Card Machines for Fashion & Accessories Retailers",
        "icon": "fa-gem",
        "desc": "Fashion and accessories retailers — selling bags, jewellery, hats, belts, scarves, and more — handle frequent card transactions at a range of price points. The in-store experience is important, and a smooth payment process is part of it. Customers browsing and buying fashion accessories expect effortless contactless payments. For independent retailers in this space, an unnecessary monthly fee on the card machine is simply money that should be staying in the business.",
        "why": "DOJO card machines present professionally and process payments efficiently — important in a retail environment where the experience matters. All payment methods accepted, next-day payouts, and zero monthly rental. The DOJO app gives you real-time sales data — useful for understanding which products are driving revenue.",
        "pain_point": "Fashion accessories retailers often operate on moderate margins. Monthly card machine rental is one of the smaller but most avoidable costs in their overhead structure.",
    },
    {
        "slug": "boutique-stores",
        "industry": "Boutique Stores",
        "headline": "Free Card Machines for Boutique Stores",
        "icon": "fa-store",
        "desc": "Independent boutiques — selling curated fashion, homeware, gifts, or lifestyle products — attract customers who value the in-store experience. Payment should feel seamless, not transactional. A card machine that's slow or unreliable breaks the experience you've worked to create. And a monthly rental fee on that machine is an overhead that works against the tight margins most boutique owners operate on.",
        "why": "DOJO card machines are compact, professional-looking payment terminals that fit the boutique environment without dominating the counter. Fast transactions, all wallets accepted, next-day payouts. Zero monthly rental means your cost of taking payments scales with your revenue — not with a fixed fee someone else decided to charge you.",
        "pain_point": "Boutique owners often focus on product and experience, and their payment setup is an afterthought. Many are paying rental fees they could immediately eliminate.",
    },
    {
        "slug": "second-hand-and-vintage-stores",
        "industry": "Second-Hand & Vintage Stores",
        "headline": "Free Card Machines for Second-Hand & Vintage Stores",
        "icon": "fa-recycle",
        "desc": "Second-hand and vintage stores — charity shops, thrift stores, vintage fashion retailers, and antique dealers — handle high transaction volumes at varying price points. Card payments now dominate even in this sector; charity shop customers in particular are used to tapping their phone for a £3 purchase. For resale businesses where margins are entirely dependent on buying well and selling efficiently, a monthly card machine rental fee is exactly the kind of cost to cut.",
        "why": "DOJO card machines are cost-effective for high-volume, lower-value retail environments — exactly what second-hand and vintage shops need. Fast contactless payments keep queues moving. Zero monthly rental is critical for shops where average transaction values are low and every cost counts. Next-day payouts and 24/7 UK support are standard.",
        "pain_point": "Many charity shops and vintage retailers still use older card readers with monthly fees. A zero-rental alternative provides the same functionality for less.",
    },
    {
        "slug": "workwear-and-uniforms",
        "industry": "Workwear & Uniforms",
        "headline": "Free Card Machines for Workwear & Uniform Suppliers",
        "icon": "fa-hard-hat",
        "desc": "Workwear and uniform suppliers — serving construction, healthcare, hospitality, and corporate clients — handle bulk orders and walk-in retail purchases. Trade customers often pay on account, but retail customers and smaller trade buyers pay by card at the counter. For workwear retailers, the card machine is a functional necessity. The monthly rental fee attached to it is not.",
        "why": "DOJO card machines handle both retail counter payments and larger trade transactions smoothly. The DOJO app gives you visibility of your daily sales, and next-day payouts keep your garment stock purchases funded. With zero monthly rental, your payment setup doesn't cost you anything in quieter periods between large orders.",
        "pain_point": "Workwear suppliers often run counter sales alongside trade accounts. The card machine for walk-in retail shouldn't carry a monthly fee that eats into each transaction's margin.",
    },
    {
        "slug": "fancy-dress-and-costume-stores",
        "industry": "Fancy Dress & Costume Stores",
        "headline": "Free Card Machines for Fancy Dress & Costume Stores",
        "icon": "fa-mask",
        "desc": "Fancy dress and costume retailers have highly seasonal trade — Halloween, Christmas, and carnival season drive the vast majority of revenue. During peak periods, transaction volumes are high and speed matters. During quieter months, a monthly card machine rental fee is a fixed cost running on minimal turnover. For fancy dress shop owners, a zero-rental card machine simply makes more sense than any fixed-fee alternative.",
        "why": "DOJO card machines are designed for exactly this kind of variable, peaks-and-troughs trading pattern. You pay only when you're taking money — no fixed monthly fee in the quiet weeks between Halloween and New Year. Fast contactless payments during the busy periods, next-day payouts, and 24/7 support if anything goes wrong at peak.",
        "pain_point": "Fancy dress shops are seasonal by nature. A monthly rental fee that runs year-round regardless of trading is particularly hard to justify for a business that earns most of its money in 6–8 weeks.",
    },
    {
        "slug": "clothing-rental",
        "industry": "Clothing Rental",
        "headline": "Free Card Machines for Clothing Rental Businesses",
        "icon": "fa-rotate",
        "desc": "Clothing rental businesses — dress hire, suit hire, costume rental — handle deposits and rental fees that are often significant per transaction. Customers expect smooth, professional payment handling when collecting and returning hired items. For clothing rental operators, a reliable card machine with low running costs is a commercial necessity. A monthly rental fee that runs regardless of how many transactions you process is an avoidable overhead.",
        "why": "DOJO card machines handle deposits and split payments efficiently, with full transaction records available in the DOJO app. For hire businesses where managing deposit returns is important, having a clear transaction history is useful. Next-day payouts and zero monthly rental keep your cost structure proportional to your revenue.",
        "pain_point": "Clothing hire businesses often have variable transaction volumes — busy around weddings and events, quieter at other times. A zero-rental model means your payment costs fall with your revenue rather than running as a fixed overhead.",
    },

    # ── ELECTRONICS & APPLIANCES ─────────────────────────────────────────────────
    {
        "slug": "electrical-and-appliance-stores",
        "industry": "Electrical & Appliance Stores",
        "headline": "Free Card Machines for Electrical & Appliance Stores",
        "icon": "fa-plug",
        "desc": "Electrical and appliance retailers — selling white goods, kitchen appliances, and consumer electronics in-store — handle high-value transactions where payment reliability is critical. A customer paying £400 for a washing machine expects the payment process to be smooth and secure. For independent electrical retailers competing with national chains, keeping every cost lean is essential — starting with an unnecessary monthly card machine rental fee.",
        "why": "DOJO card machines handle high-value transactions reliably and professionally. All payment types accepted, including high-value contactless. Dual connectivity means you're never reliant on a single connection for a large transaction. Next-day payouts keep your stock purchasing power consistent, and zero monthly rental means your payment infrastructure costs are proportional to your sales.",
        "pain_point": "Independent electrical retailers are often on merchant service contracts set up when they first opened. Those contracts frequently include rental fees that were never the only option available.",
    },
    {
        "slug": "electronics-stores",
        "industry": "Electronics Stores",
        "headline": "Free Card Machines for Electronics Stores",
        "icon": "fa-microchip",
        "desc": "Electronics stores — selling phones, computers, tablets, gaming equipment, and tech accessories — process a mix of high-value and everyday transactions. Customers expect professional, fast payments. For independent electronics retailers, the margin on many product categories is tight, making every unnecessary cost worth examining. A monthly card machine rental fee is a fixed overhead that can be eliminated without affecting anything else in the business.",
        "why": "DOJO card machines work well in an electronics retail environment — professional-looking, fast, and accepting all payment types including premium contactless on high-value items. The DOJO app provides real-time sales data. Next-day payouts and zero monthly rental keep your cash flow and cost structure lean.",
        "pain_point": "Electronics retailers often operate on thin margins, especially on hardware. A monthly card machine rental fee compounds with every transaction rate — it's an avoidable cost.",
    },
    {
        "slug": "lighting-and-electrical-parts",
        "industry": "Lighting & Electrical Parts",
        "headline": "Free Card Machines for Lighting & Electrical Parts Suppliers",
        "icon": "fa-lightbulb",
        "desc": "Lighting showrooms, electrical wholesalers, and electrical parts suppliers serve a mix of trade professionals and retail customers, handling everything from small parts purchases to large order values. Trade accounts exist, but walk-in and counter sales are paid by card. For suppliers in this space, a reliable and cost-effective card machine at the counter is a basic commercial requirement — one that doesn't need to include a monthly rental fee.",
        "why": "DOJO card machines handle trade counter payments efficiently — fast, all payment types accepted, and the DOJO app for transaction reporting. For suppliers serving both retail and trade through the same counter, having clear payment records is valuable. Zero monthly rental and next-day payouts keep your cost structure and cash flow working in your favour.",
        "pain_point": "Electrical parts suppliers often set up their payment processing through their trade account or bank. Those setups often carry monthly fees that a direct DOJO setup would eliminate.",
    },

    # ── AGRICULTURE & OUTDOOR ────────────────────────────────────────────────────
    {
        "slug": "farming-and-farm-supplies",
        "industry": "Farming & Farm Supplies",
        "headline": "Free Card Machines for Farming & Farm Supply Businesses",
        "icon": "fa-tractor",
        "desc": "Farm shops, agricultural suppliers, and farm-direct food businesses handle card payments across a variety of environments — fixed shops, market stalls, and on-farm sales points. Connectivity can be challenging in rural locations, which makes the reliability of the payment infrastructure even more important. A monthly rental fee on a card machine that may not even work reliably in your location is a particularly easy cost to cut.",
        "why": "DOJO card machines are built with dual WiFi/4G connectivity — critical for farm shops and agricultural suppliers where broadband can be unreliable. The 4G SIM backup means payments go through regardless of your internet connection. Portable enough for market stalls and pop-up sales, next-day payouts, and zero monthly rental. A practical solution for a practical business.",
        "pain_point": "Rural businesses have historically struggled with card payment infrastructure. DOJO's dual connectivity solves the reliability problem — and the zero-rental model solves the cost problem.",
    },
    {
        "slug": "garden-centres-and-nurseries",
        "industry": "Garden Centres & Nurseries",
        "headline": "Free Card Machines for Garden Centres & Nurseries",
        "icon": "fa-seedling",
        "desc": "Garden centres and nurseries handle high transaction volumes during peak seasons — spring and summer in particular — and much lower volumes in winter. Customers buy everything from a £2 packet of seeds to a £200 mature specimen, and almost everyone pays by card. For garden centre operators, a payment setup that costs a fixed monthly fee regardless of seasonal trading patterns doesn't make commercial sense.",
        "why": "DOJO card machines handle both small plant purchases and large landscaping orders efficiently. For garden centres with outdoor sales areas where WiFi doesn't reach, 4G connectivity ensures you never miss a payment. Zero monthly rental means your payment costs fall in winter with your revenue — you're never paying for the ability to take payments when there's nothing to take.",
        "pain_point": "Garden centres are among the most seasonally variable retail businesses in the UK. A monthly rental fee that runs year-round regardless of trading is one of the clearest candidates for elimination.",
    },
    {
        "slug": "florists",
        "industry": "Florists",
        "headline": "Free Card Machines for Florists",
        "icon": "fa-leaf",
        "desc": "Florists handle regular in-shop card payments and occasional large orders — weddings, corporate events, funerals — where payment reliability really matters. Customers walk in with their phone in their hand expecting to tap and go. For independent florists competing with supermarket flower sections and online services, every cost needs to be lean. A monthly card machine rental fee is one of the simplest things to cut.",
        "why": "DOJO card machines are compact and professional — fitting naturally behind a florist's counter. Fast contactless payments, all wallets accepted, and next-day payouts mean that a big wedding order payment on Thursday is in your account on Friday. Zero monthly rental means your payment setup doesn't cost you anything during quieter weeks.",
        "pain_point": "Many florists are on card machine contracts they've never revisited since they opened. A quick check of their monthly statement usually reveals a rental fee they don't need to pay.",
    },
    {
        "slug": "landscape-gardening",
        "industry": "Landscape Gardening",
        "headline": "Free Card Machines for Landscape Gardeners",
        "icon": "fa-tree",
        "desc": "Landscape gardeners collect large, project-based payments from clients — often at the client's property at the end of a job. Customers expect to pay by card, and a mobile card machine is an essential professional tool. For landscape gardeners building a business, keeping overhead costs low while delivering high-quality work is the constant challenge. A monthly rental fee on a card machine is an obvious overhead to eliminate.",
        "why": "DOJO card machines are compact and fully mobile — working anywhere with 4G coverage, which means at a client's home, garden, or commercial site. No reliance on the customer's WiFi. Fast professional payments, next-day payouts to fund materials for the next project, and zero monthly rental. The payment solution that makes sense for a mobile, project-based business.",
        "pain_point": "Landscape gardeners who've been collecting cash or doing bank transfers are losing professional credibility and sometimes losing jobs over it. DOJO makes card payments easy, mobile, and free to set up.",
    },
    {
        "slug": "tree-surgeons",
        "industry": "Tree Surgeons",
        "headline": "Free Card Machines for Tree Surgeons",
        "icon": "fa-tree",
        "desc": "Tree surgeons collect payment on-site at the end of a job — often a significant sum for a full tree removal or large crown reduction. Customers increasingly expect card payment rather than bank transfer or cash. For arborists and tree surgery businesses, a reliable mobile card machine is a professional necessity. The monthly rental fee attached to it is not.",
        "why": "DOJO card machines are fully mobile and work anywhere with 4G — ideal for a tree surgeon collecting payment in a residential garden or rural property. No need for the customer's WiFi. Next-day payouts fund your equipment maintenance and chipper hire without waiting for bank transfers to clear. Zero monthly rental means your payment setup costs nothing on days you're not on a job.",
        "pain_point": "Many tree surgeons have avoided card machines because of the perceived setup cost and monthly fees. DOJO costs nothing to set up and nothing per month — just a transaction rate when you take a payment.",
    },

    # ── PETS & ANIMAL SERVICES ───────────────────────────────────────────────────
    {
        "slug": "veterinary-services",
        "industry": "Veterinary Services",
        "headline": "Free Card Machines for Veterinary Practices",
        "icon": "fa-paw",
        "desc": "Veterinary practices handle card payments for everything from a routine annual check-up to an emergency surgical procedure running into thousands of pounds. Clients are paying significant amounts and expect a smooth, professional payment experience at an often already stressful moment. For vet practices, the economics of payment processing matter — and a monthly rental fee on the card machine is a cost worth eliminating.",
        "why": "DOJO card machines handle the full range of veterinary payment values — from a £30 vaccination to a £3,000 emergency procedure. Professional, reliable, and accepting all payment types. Next-day payouts ensure your supplier and drug company payments are always funded. Zero monthly rental means your payment overhead is purely proportional to your transaction volume.",
        "pain_point": "Many vet practices are on payment setups tied to their practice management software. Those setups often include monthly rental or service fees on the terminal that a direct DOJO arrangement would eliminate.",
    },

    # ── GROCERY & CONVENIENCE ────────────────────────────────────────────────────
    {
        "slug": "supermarkets-and-grocery-stores",
        "industry": "Supermarkets & Grocery Stores",
        "headline": "Free Card Machines for Grocery Stores & Supermarkets",
        "icon": "fa-shopping-basket",
        "desc": "Independent supermarkets and grocery stores process among the highest card payment volumes of any retail category — multiple transactions per minute during peak hours, all day, every day. For independent grocery operators competing with multiples on price and service, the cost-per-transaction and the fixed overhead of a monthly card machine rental are both worth scrutinising. A zero-rental card machine is a simple, immediate improvement.",
        "why": "DOJO card machines are fast at the checkout — contactless transactions in under a second, all cards and wallets accepted. Dual connectivity ensures you're never offline during peak hours. Multiple machines on a single account for multi-till operations. Next-day payouts keep your supplier payments on schedule. Zero monthly rental per machine is a significant saving for high-volume grocery operations.",
        "pain_point": "Independent grocery stores often have multiple tills, each with its own rental fee. Switching to a zero-rental model across all terminals can represent a meaningful monthly saving.",
    },
    {
        "slug": "corner-shops-and-newsagents",
        "industry": "Corner Shops & Newsagents",
        "headline": "Free Card Machines for Corner Shops & Newsagents",
        "icon": "fa-newspaper",
        "desc": "Corner shops and newsagents handle a constant flow of low-value card transactions — newspapers, drinks, snacks, tobacco, lottery tickets — from early morning to late evening. Cash use has declined significantly even for small purchases, and customers expect tap-and-go on transactions of any size. For corner shop owners managing tight margins across long trading hours, a monthly card machine rental fee is a fixed cost that eats into what's already a thin operation.",
        "why": "DOJO card machines are fast for low-value transactions — essential for a corner shop where the queue can't afford to slow down. All contactless payment types accepted, next-day payouts, and zero monthly rental. For newsagents open from 6am to 10pm, a payment setup that only costs when you're taking money is simply more logical than any fixed-fee alternative.",
        "pain_point": "Corner shops often have some of the highest card payment volumes and lowest average transaction values in retail. Monthly rental fees are a fixed cost regardless of that margin reality — they should be the first thing cut.",
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

HEAD_LINKS = """  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;1,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">"""

SCROLL_BTN = """<button id="scrollBtn" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Scroll to top">
  <i class="fas fa-chevron-up"></i>
</button>"""


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


def build_industry_page(ind):
    slug     = ind["slug"]
    industry = ind["industry"]
    headline = ind["headline"]
    icon     = ind["icon"]
    desc     = ind["desc"]
    why      = ind["why"]
    pain     = ind["pain_point"]
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


def main():
    count = 0
    slugs = []
    for ind in NEW_INDUSTRIES:
        filename = f"card-machine-for-{ind['slug']}.html"
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(build_industry_page(ind))
        print(f"  Created: {filename}")
        slugs.append(ind["slug"])
        count += 1
    print(f"\nDone — {count} pages generated.")
    print("\nSitemap entries:")
    for s in slugs:
        print(f'  <url><loc>https://www.paymentcardservices.co.uk/card-machine-for-{s}</loc><lastmod>2026-07-06</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>')


if __name__ == "__main__":
    main()
