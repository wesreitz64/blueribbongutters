import os

base_file = r'c:\Users\wesre\source\repos\BlueRibbonGutters\pottstown.html'
with open(base_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Generate limerick.html first by replacing Pottstown stuff
limerick_content = content.replace('Pottstown', 'Limerick')
limerick_content = limerick_content.replace('19464 &amp; 19465', '19468')
limerick_content = limerick_content.replace('19464 & 19465', '19468')
limerick_content = limerick_content.replace('19464, 19465', '19468')
limerick_content = limerick_content.replace('pottstown', 'limerick')

with open(r'c:\Users\wesre\source\repos\BlueRibbonGutters\limerick.html', 'w', encoding='utf-8') as f:
    f.write(limerick_content)

# 2. Function to generate special pages
def generate_special(town_name, town_slug, zip_code):
    pages = [
        {
            'filename': f'downspouts-{town_slug}.html',
            'title': f'Downspout Installation & Repair in {town_name}, PA | Blue Ribbon Seamless Gutter',
            'desc': f'Expert downspout installation, repair, and drainage solutions in {town_name}, PA. Serving {zip_code} zip codes. Free estimates. Call (610) 322-7069.',
            'canonical': f'https://blueribbongutters.com/downspouts-{town_slug}',
            'h1_main': 'Expert Downspout Installation',
            'h1_sub': f'& Repair in {town_name}',
            'hero_sub': f'Protect your home\'s foundation with proper downspout placement and premium materials. Trusted by your neighbors. Serving {zip_code}.'
        },
        {
            'filename': f'gutter-guards-{town_slug}.html',
            'title': f'Gutter Guards & Leaf Protection in {town_name}, PA | Blue Ribbon Seamless Gutter',
            'desc': f'Premium micro-mesh gutter guards and leaf protection in {town_name}, PA. Keep your gutters clog-free. Serving {zip_code} zip codes. Free estimates.',
            'canonical': f'https://blueribbongutters.com/gutter-guards-{town_slug}',
            'h1_main': 'Premium Gutter Guards',
            'h1_sub': f'& Leaf Protection in {town_name}',
            'hero_sub': 'End ladder climbing forever with micro-mesh gutter guards. 99.9% effective against leaves, pine needles, and debris. Built for PA weather.'
        },
        {
            'filename': f'award-winning-gutters-{town_slug}.html',
            'title': f'Award-Winning Gutter Services in {town_name}, PA | Blue Ribbon Seamless Gutter',
            'desc': f'Top-rated, award-winning seamless gutter installation in {town_name}, PA. Trusted by the community with 5-star reviews. Free estimates. Call (610) 322-7069.',
            'canonical': f'https://blueribbongutters.com/award-winning-gutters-{town_slug}',
            'h1_main': 'Award-Winning Gutter',
            'h1_sub': f'Services in {town_name}',
            'hero_sub': f'Award-winning quality, 5-star customer service, and absolute reliability. Join hundreds of satisfied {town_name} homeowners who trust Blue Ribbon.'
        }
    ]

    base_town_file = os.path.join(r'c:\Users\wesre\source\repos\BlueRibbonGutters', f'{town_slug}.html')
    with open(base_town_file, 'r', encoding='utf-8') as f:
        town_content = f.read()

    for p in pages:
        new_content = town_content
        # We need to replace the <title>, description, canonical, H1, etc.
        # This is a bit brute force but works for the current template structure
        import re
        new_content = re.sub(r'<title>.*?</title>', f'<title>{p["title"]}</title>', new_content)
        new_content = re.sub(r'<meta name="description"\s*content=".*?">', f'<meta name="description"\n        content="{p["desc"]}">', new_content, flags=re.DOTALL)
        new_content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{p["canonical"]}">', new_content)
        
        # Replace H1
        new_content = re.sub(r'<h1 class="hero__title">.*?<br><span class="hero__highlight">.*?</span></h1>', f'<h1 class="hero__title">{p["h1_main"]}<br><span class="hero__highlight">{p["h1_sub"]}</span></h1>', new_content)
        
        # Replace hero sub
        new_content = re.sub(r'<p class="hero__sub">.*?</p>', f'<p class="hero__sub">{p["hero_sub"]}</p>', new_content, flags=re.DOTALL)
        
        with open(os.path.join(r'c:\Users\wesre\source\repos\BlueRibbonGutters', p['filename']), 'w', encoding='utf-8') as f:
            f.write(new_content)

generate_special('Royersford', 'royersford', '19468')
generate_special('Limerick', 'limerick', '19468')

print("Generated Limerick.html and all special pages for Royersford and Limerick.")
