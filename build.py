import os

LOGO = "https://burnshomes247.github.io/listings/burnshomes-logo.png"
GTAG = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-359RJ8YZZY"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-359RJ8YZZY');
</script>"""

NAV_ITEMS = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("seller-services.html", "Seller Services"),
    ("buyer-services.html", "Buyer Services"),
    ("broker-information.html", "Broker Info"),
    ("contact.html", "Contact"),
]

def nav(active):
    links = "\n".join(
        f'<a href="{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV_ITEMS
    )
    return f"""<header class="site-nav">
<div class="nav-inner">
<a class="nav-logo" href="index.html"><img src="{LOGO}" alt="BURNSHOMES"><span>BURNSHOMES</span></a>
<nav class="nav-links">
{links}
</nav>
</div>
</header>"""

def footer():
    links = "\n".join(f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS[1:])
    return f"""<footer class="site-footer">
<img class="footer-logo" src="{LOGO}" alt="BURNSHOMES">
<div class="agent">Mike Burns, Realtor</div>
<div class="agent-sub">RE/MAX Allegiance</div>
<div class="footer-links">
{links}
</div>
<div class="copyright">&copy; 2026 BURNSHOMES. All rights reserved. &middot; (703) 403-2022 &middot; mike@burnshomes.com</div>
</footer>"""

def page(title, description, active, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{GTAG}
<link rel="stylesheet" href="style.css">
</head>
<body>
{nav(active)}
{body}
{footer()}
</body>
</html>"""

os.makedirs("/home/claude/burnshomes-site", exist_ok=True)
OUT = "/home/claude/burnshomes-site"

# ---------------- HOME ----------------
home_body = f"""
<div class="hero">
<div class="hero-eyebrow">Virginia &middot; Maryland &middot; Washington DC</div>
<h1>Expert &amp; Personalized Real Estate Services</h1>
<p>Advising sellers and buyers across the DMV for nearly three decades.</p>
<div class="hero-actions">
<a href="seller-services.html" class="btn btn-filled">Seller Services</a>
<a href="buyer-services.html" class="btn">Buyer Services</a>
</div>
</div>

<section class="section-tight">
<div class="container">
<div class="stat-strip">
<div class="stat"><div class="num">29+</div><div class="label">Years Experience</div></div>
<div class="stat"><div class="num">$500M+</div><div class="label">Closed Transactions</div></div>
<div class="stat"><div class="num">VA &middot; MD &middot; DC</div><div class="label">Licensed In</div></div>
</div>
</div>
</section>

<section>
<div class="container">
<div class="section-title">How Can I Help?</div>
<div class="grid-2">
<div class="card">
<h3>Sellers</h3>
<p>Successfully selling real estate demands a keen understanding of price, condition, location, and presentation. I put 29 years of experience to work maximizing your outcome.</p>
<p style="margin-top:16px;"><a href="seller-services.html">Learn more &rarr;</a></p>
</div>
<div class="card">
<h3>Buyers</h3>
<p>Every home-buying journey is complex and unique. I offer Essential and Premium buyer programs, customized to meet your specific needs.</p>
<p style="margin-top:16px;"><a href="buyer-services.html">Learn more &rarr;</a></p>
</div>
</div>
</div>
</section>

<section class="testimonials">
<div class="container" style="padding:60px 20px;">
<div class="section-title" style="margin-bottom:10px;">What Clients Say</div>
</div>
<div class="testimonial-grid">
<div class="testimonial"><p>&ldquo;Mike is hands-down the best realtor I've worked with in the past 30 years! He's knowledgeable, patient, thorough, empathic, tenacious, and he listens.&rdquo;</p><div class="name">Aaron A.</div></div>
<div class="testimonial"><p>&ldquo;With Mike's expertise our home sold after the first open house above our asking price. He was wonderful in keeping the transaction moving forward.&rdquo;</p><div class="name">Alpa P.</div></div>
</div>
</section>

<div class="cta-band">
<h2>Let's Talk</h2>
<p>Call, text, or email &mdash; I respond quickly and I'm happy to help.</p>
<a href="contact.html" class="btn btn-filled">Contact Me</a>
</div>
"""

# ---------------- ABOUT ----------------
about_body = f"""
<div class="page-header">
<h1>About Mike</h1>
</div>
<section>
<div class="container prose">
<p>Mike Burns has called the DMV home since his family relocated from Upstate New York when he was 12 years old. Growing up in Ocean City, Mike worked various jobs during his middle and high school years &mdash; from caddying at Ocean Pines Golf Course and delivering fudge to the Candy Kitchens, to serving breakfast at The General's Kitchen and cleaning glasses behind the bar at The Bonfire. One summer, he even delivered furniture at Resort Furnishings, where his mother was the manager &mdash; though three months of moving furniture was enough to convince him to pursue other career paths.</p>
<p>After graduating from the University of Maryland, Mike knew he wanted a career focused on helping people plan for their future. He began his professional journey at Transamerica Financial, providing financial services, then transitioned to First Atlantic Mortgage, where he gained valuable insight into the mortgage process. That experience became an essential foundation for his work with real estate clients, starting at Long &amp; Foster and now with RE/MAX Allegiance.</p>
<p>Mike has lived in various parts of the DMV, including Rockville, Bethesda, Falls Church, Arlington, Dupont Circle, Logan Circle, Reston, and Herndon &mdash; giving him a deep understanding of the region and the unique qualities of each area's real estate market.</p>
<p>Mike comes from a large family with five siblings. He is married to his wife, Alicia, a Certified Residential Appraiser with over 35 years of DC-metro experience, and together they have a son named Mack.</p>
</div>
</section>
<div class="cta-band">
<h2>29 Years. $500M+ Closed.</h2>
<p>Local knowledge, honest advice, and a tech-forward approach to every transaction.</p>
<a href="contact.html" class="btn btn-filled">Get In Touch</a>
</div>
"""

# ---------------- SELLER SERVICES ----------------
seller_body = f"""
<div class="page-header">
<h1>Seller Services</h1>
<p>Successfully selling real estate demands a keen understanding of four critical factors: price, condition, location, and presentation. A seasoned advisor expertly leverages these elements to maximize your opportunity for a sale on the best possible terms.</p>
</div>

<section>
<div class="container">
<div class="grid-2">

<div class="card">
<div class="influence">Maximum Influence</div>
<h3>Asking Price</h3>
<p>There is a high and low range for every property sold. The initial asking price matters and should be carefully considered &mdash; not just against recent sales, but also:</p>
<ul>
<li>Active listings</li>
<li>Coming-soon properties</li>
<li>Withdrawn listings</li>
<li>Recent sales just outside the neighborhood</li>
<li>Current &amp; trending economic conditions</li>
<li>Time of year</li>
</ul>
</div>

<div class="card">
<div class="influence">Minimal Influence</div>
<h3>Property Location</h3>
<p>Location refers not just to the address, but the neighborhood, the street, and the surrounding lots:</p>
<ul>
<li>Is the neighborhood desirable?</li>
<li>Are schools close by?</li>
<li>Walkable to shops &amp; dining?</li>
<li>Proximity to parks &amp; transit</li>
</ul>
</div>

<div class="card">
<div class="influence">Medium Influence</div>
<h3>Property Condition</h3>
<p>The quality and condition of updates and features within the home:</p>
<ul>
<li>Updated or original?</li>
<li>Bedroom &amp; bathroom count</li>
<li>Curb appeal &amp; exterior space</li>
<li>Garage, driveway, or street parking</li>
<li>Layout &amp; square footage</li>
</ul>
</div>

<div class="card">
<div class="influence">Maximum Influence</div>
<h3>Listing Presentation</h3>
<p>Expertly assessing price, condition, and location, then executing a superior marketing plan with proper timing and presentation, maximizes your probability of reaching your selling goals.</p>
<p style="margin-top:14px;">After 29 years and $500,000,000 in real estate sales, I can do the job. <a href="tel:7034032022">Call me</a> for a free evaluation.</p>
</div>

</div>
</div>
</section>

<section class="testimonials">
<div class="testimonial-grid">
<div class="testimonial"><p>&ldquo;Mike identified reputable contractors, conducted showings, and was accessible throughout the sales process. I could not have been happier with the decision I made.&rdquo;</p><div class="name">Mark F.</div></div>
<div class="testimonial"><p>&ldquo;With Mike's expertise our home sold after the first open house above our asking price. Mike is an amazing realtor and we are very fortunate to have worked with him.&rdquo;</p><div class="name">Alpa P.</div></div>
<div class="testimonial"><p>&ldquo;His attention to detail is second to none and he will work tirelessly to make his clients happy. He's my first call for my next move.&rdquo;</p><div class="name">Aaron A.</div></div>
<div class="testimonial"><p>&ldquo;He consistently gave us sound advice based upon his past experience and history, which allowed us to make the best decisions for us.&rdquo;</p><div class="name">Sasha T.</div></div>
</div>
</section>

<div class="cta-band">
<h2>Thinking Of Selling?</h2>
<p>Call for a free evaluation and a four-page guide covering all the factors that affect your sale.</p>
<a href="tel:7034032022" class="btn btn-filled">(703) 403-2022</a>
</div>
"""

# ---------------- BUYER SERVICES ----------------
buyer_body = f"""
<div class="page-header">
<h1>Buyer Services</h1>
<p>Each home-buying journey is complex and unique. I offer two programs &mdash; Essential and Premium &mdash; customized to meet each client's specific needs.</p>
</div>

<section>
<div class="container prose">
<p>Through 29 years and $500 million in closed transactions, I have developed a deep understanding of the entire purchasing process &mdash; from the simple (scheduling inspections, delivering notices) to the complex (anticipating seller responses, identifying bluffs). All of my clients benefit from that experience.</p>
</div>
</section>

<section class="section-tight">
<div class="container">
<div class="grid-2">
<div class="card">
<h3>Essential Buyer Services</h3>
<p>Everything you would expect when working with a veteran real estate advocate: professional guidance, negotiating strategy, market analysis, access to a vetted vendor network, and expert contract knowledge.</p>
<p style="margin-top:14px;">This also includes accuracy checks across current listing data, past &amp; non-public listing data, and tax records &mdash; ensuring wise pricing decisions that save you time and money.</p>
</div>
<div class="card">
<h3>Premium Buyer Services</h3>
<p>Everything in Essential, plus additional personalized features &mdash; including targeted mailings within a specific neighborhood to locate off-market sellers.</p>
<p style="margin-top:14px;"><a href="tel:7034032022">Call me</a> to discuss which program is right for you.</p>
</div>
</div>
</div>
</section>

<section class="testimonials">
<div class="testimonial-grid">
<div class="testimonial"><p>&ldquo;Mike guided me through each step of the process with patience and expertise, always making sure I felt confident and informed. Mike is the best in the business!&rdquo;</p><div class="name">Jen D.</div></div>
<div class="testimonial"><p>&ldquo;Mike was an incredible guide for us as we navigated buying a house in DC while returning from abroad. Knowledgeable, anticipatory, frank, and super responsive.&rdquo;</p><div class="name">Chris H.</div></div>
<div class="testimonial"><p>&ldquo;He went over and beyond what would be reasonably expected, in almost every way imaginable. We cannot recommend him highly enough.&rdquo;</p><div class="name">Scott H.</div></div>
</div>
</section>

<div class="cta-band">
<h2>Ready To Start Looking?</h2>
<p>Let's talk about which program fits your search.</p>
<a href="tel:7034032022" class="btn btn-filled">(703) 403-2022</a>
</div>
"""

# ---------------- BROKER INFORMATION ----------------
broker_body = f"""
<div class="page-header">
<h1>Broker Information</h1>
</div>
<section>
<div class="container" style="max-width:720px;">

<div class="license-block">
<h3>Virginia License</h3>
<p>Michael Timothy Burns Jr<br>
Agent License 0225 064462<br>
Broker License 0226 010271</p>
<p style="margin-top:14px;">RE/MAX Allegiance<br>
4157 Chain Bridge Road, Fairfax, Virginia 22030<br>
(703) 563-2200</p>
</div>

<div class="license-block">
<h3>Maryland License</h3>
<p>Michael T Burns Jr<br>
Agent License 529946<br>
Broker License 31417</p>
<p style="margin-top:14px;">RE/MAX Allegiance<br>
701 E Street SE, Washington, DC 20003<br>
(202) 547-5600</p>
</div>

<div class="license-block">
<h3>District of Columbia License</h3>
<p>Michael T Burns Jr<br>
Agent License SP102631<br>
Broker License LL98363268</p>
<p style="margin-top:14px;">RE/MAX Allegiance<br>
701 E Street SE, Washington, DC 20003<br>
(202) 547-5600</p>
</div>

<p style="text-align:center; font-size:12px; letter-spacing:1px; color:#888; margin-top:20px;">Equal Housing Opportunity</p>

</div>
</section>
"""

# ---------------- CONTACT ----------------
contact_body = f"""
<div class="page-header">
<h1>Contact Me</h1>
</div>
<section>
<div class="container">
<div class="contact-block">
<div class="name">Mike Burns, Realtor</div>
<div class="brokerage">RE/MAX Allegiance</div>
<div class="details">
<p><a href="tel:7034032022">(703) 403-2022</a></p>
<p><a href="mailto:mike@burnshomes.com">mike@burnshomes.com</a></p>
</div>
</div>
</div>
</section>
"""

pages = [
    ("index.html", "BURNSHOMES | Mike Burns, Realtor &mdash; Virginia, Maryland &amp; DC", "Expert, personalized real estate services in Virginia, Maryland, and Washington DC. 29 years experience, $500M+ closed.", "index.html", home_body),
    ("about.html", "About Mike | BURNSHOMES", "Meet Mike Burns, a DMV-based realtor with 29 years of experience serving Virginia, Maryland, and DC.", "about.html", about_body),
    ("seller-services.html", "Seller Services | BURNSHOMES", "Expert seller representation across Virginia, Maryland, and DC. Price, condition, location, and presentation.", "seller-services.html", seller_body),
    ("buyer-services.html", "Buyer Services | BURNSHOMES", "Essential and Premium buyer representation programs tailored to your home search in the DMV.", "buyer-services.html", buyer_body),
    ("broker-information.html", "Broker Information | BURNSHOMES", "RE/MAX Allegiance broker and license information for Virginia, Maryland, and DC.", "broker-information.html", broker_body),
    ("contact.html", "Contact | BURNSHOMES", "Contact Mike Burns, Realtor with RE/MAX Allegiance.", "contact.html", contact_body),
]

for fname, title, desc, active, body in pages:
    html = page(title, desc, active, body)
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

print("Built", len(pages), "pages")
