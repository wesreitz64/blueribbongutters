import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new hero content
new_hero = """<div class="container hero__content hero-split">
            <div class="hero-text">
                <div class="hero__badge">⭐ Serving Boyertown &amp; Surrounding Areas</div>
                <h1 class="hero__title">Expert Seamless Gutters<br><span class="hero__highlight">installed right the first time.</span></h1>
                
                <div class="hero-review">
                    <div class="hero-review-stars">
                        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
                    </div>
                    <p>“Ed gave us a quote and in less than a week, he had the gutters installed. He takes his time to be sure everything is a precise fit.”</p>
                    <span><strong>- Becca, Google Reviews</strong></span>
                </div>
                
                <p class="hero__sub">Professional seamless gutter installation &amp; repair serving Berks &amp; Montgomery Counties. Family-owned. Free estimates. Licensed &amp; insured.</p>
                
            </div>
            <div class="hero-formbox">
                <div class="formbox-header">
                    <h3>Get a Free Estimate</h3>
                    <p>We typically respond within hours</p>
                </div>
                <form class="contact__form formbox-form" action="https://formspree.io/f/xqeykjan" method="POST">
                    <input type="hidden" name="_next" value="https://blueribbongutters.com/thankyou.html">
                    <input type="hidden" name="_source" value="home2-hero-form">
                    <div class="form-group">
                        <label style="color:#2b2b2b" for="name2">Your Name *</label>
                        <input type="text" id="name2" name="name" required placeholder="John Smith">
                    </div>
                    <div class="form-group">
                        <label style="color:#2b2b2b" for="phone2">Phone Number *</label>
                        <input type="tel" id="phone2" name="phone" required placeholder="(555) 000-0000">
                    </div>
                    <div class="form-group">
                        <label style="color:#2b2b2b" for="service2">Service Needed</label>
                        <select id="service2" name="service">
                            <option>New Seamless Gutters</option>
                            <option>Gutter Guards</option>
                            <option>Gutter Repair / Cleaning</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn--primary btn--full formbox-btn">
                        Get Your Free Quote
                    </button>
                    <p class="formbox-subtext">No pressure, no obligation.</p>
                </form>
            </div>
        </div>"""

css = """
<style>
.hero-split {
    display: flex;
    flex-wrap: wrap;
    gap: 3rem;
    align-items: center;
    justify-content: space-between;
    text-align: left;
}
.hero-text {
    flex: 1 1 450px;
    text-align: left;
}
.hero-text .hero__badge {
    margin: 0 0 1rem 0;
}
.hero-text .hero__title {
    margin-bottom: 1rem;
    font-size: 3.5rem;
}
.hero-review {
    background: rgba(255, 255, 255, 0.1);
    border-left: 4px solid var(--gold);
    padding: 1rem;
    border-radius: 4px;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(5px);
    max-width: 500px;
}
.hero-review-stars {
    color: var(--gold);
    margin-bottom: 0.5rem;
}
.hero-review p {
    font-style: italic;
    font-size: 1rem;
    margin-bottom: 0.5rem;
    color: #fff;
    line-height: 1.4;
}
.hero-review span {
    font-size: 0.85rem;
    color: rgba(255, 255, 255, 0.8);
}
.hero-formbox {
    flex: 0 0 380px;
    background: var(--white);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    animation: slideUpFade 0.8s ease forwards;
}
.formbox-header {
    background: var(--primary);
    color: white;
    padding: 1.5rem;
    text-align: center;
}
.formbox-header h3 {
    margin: 0;
    font-size: 1.4rem;
}
.formbox-header p {
    margin: 0.5rem 0 0;
    font-size: 0.9rem;
    opacity: 0.9;
}
.formbox-form {
    padding: 1.5rem;
}
.formbox-btn {
    font-size: 1.1rem;
    padding: 1rem;
    margin-top: 0.5rem;
}
.formbox-subtext {
    text-align: center;
    font-size: 0.8rem;
    color: var(--gray);
    margin-top: 1rem;
}

@media (max-width: 900px) {
    .hero-split {
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }
    .hero-text {
        text-align: center;
    }
    .hero-text .hero__title {
        font-size: 2.5rem;
    }
    .hero-text .hero__badge {
        margin: 0 auto 1rem;
    }
    .hero-review {
        margin: 1.5rem auto;
        text-align: left;
    }
    .hero-formbox {
        width: 100%;
        flex: 1 1 100%;
        max-width: 450px;
    }
}
</style>
"""

# Replace the hero content
# We will use regex to find <div class="container hero__content"> ... </div> up to </section>

pattern = re.compile(r'<div class="container hero__content">.*?(?=</section>)', re.DOTALL)
new_content = pattern.sub(new_hero + '\n    ', content)

# Inject CSS before </head>
new_content = new_content.replace('</head>', css + '</head>')

# Ensure rel="canonical" points to home2 (or remove it to prevent issues)
new_content = re.sub(r'<link rel="canonical" href="[^"]+">', '<link rel="canonical" href="https://blueribbongutters.com/home2.html">', new_content)

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
