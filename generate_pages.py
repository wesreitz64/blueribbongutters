import os

base_file = r'c:\Users\wesre\source\repos\BlueRibbonGutters\pottstown.html'
with open(base_file, 'r', encoding='utf-8') as f:
    content = f.read()

pages = [
    {
        'filename': 'downspouts-pottstown.html',
        'title': 'Downspout Installation & Repair in Pottstown, PA | Blue Ribbon Seamless Gutter',
        'desc': 'Expert downspout installation, repair, and drainage solutions in Pottstown, PA. Serving 19464 & 19465 zip codes. Free estimates. Call (610) 322-7069.',
        'canonical': 'https://blueribbongutters.com/downspouts-pottstown',
        'h1_main': 'Expert Downspout Installation',
        'h1_sub': '& Repair in Pottstown',
        'hero_sub': 'Protect your home\'s foundation with proper downspout placement and premium materials. Trusted by your neighbors in Montgomery County. Serving 19464 & 19465.'
    },
    {
        'filename': 'gutter-guards-pottstown.html',
        'title': 'Gutter Guards & Leaf Protection in Pottstown, PA | Blue Ribbon Seamless Gutter',
        'desc': 'Premium micro-mesh gutter guards and leaf protection in Pottstown, PA. Keep your gutters clog-free. Serving 19464 & 19465 zip codes. Free estimates.',
        'canonical': 'https://blueribbongutters.com/gutter-guards-pottstown',
        'h1_main': 'Premium Gutter Guards',
        'h1_sub': '& Leaf Protection in Pottstown',
        'hero_sub': 'End ladder climbing forever with micro-mesh gutter guards. 99.9% effective against leaves, pine needles, and debris. Built for PA weather.'
    },
    {
        'filename': 'award-winning-gutters-pottstown.html',
        'title': 'Award-Winning Gutter Services in Pottstown, PA | Blue Ribbon Seamless Gutter',
        'desc': 'Top-rated, award-winning seamless gutter installation in Pottstown, PA. Trusted by the community with 5-star reviews. Free estimates. Call (610) 322-7069.',
        'canonical': 'https://blueribbongutters.com/award-winning-gutters-pottstown',
        'h1_main': 'Award-Winning Gutter',
        'h1_sub': 'Services in Pottstown',
        'hero_sub': 'Award-winning quality, 5-star customer service, and absolute reliability. Join hundreds of satisfied Pottstown homeowners who trust Blue Ribbon.'
    }
]

for p in pages:
    new_content = content
    new_content = new_content.replace('<title>Gutter Installation & Repair in Pottstown, PA | Blue Ribbon Seamless Gutter</title>', f'<title>{p["title"]}</title>')
    new_content = new_content.replace('content="Expert seamless gutter installation, repair, and leaf protection in Pottstown, PA. Serving 19464 & 19465 zip codes. Free estimates. Call (610) 322-7069.">', f'content="{p["desc"]}">')
    new_content = new_content.replace('href="https://blueribbongutters.com/pottstown"', f'href="{p["canonical"]}"')
    
    new_content = new_content.replace('Expert Gutter Installation', p['h1_main'])
    new_content = new_content.replace('& Repair in Pottstown', p['h1_sub'])
    new_content = new_content.replace('Trusted by your neighbors in Montgomery County. High-quality seamless gutters and leaf\n                protection built to withstand Pennsylvania winters. Serving 19464 &amp; 19465.', p['hero_sub'])
    
    with open(os.path.join(r'c:\Users\wesre\source\repos\BlueRibbonGutters', p['filename']), 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Generated all 3 pages.")
