import os
import glob
import re

# 1. Generate missing town pages from boyertown.html
base_file = 'boyertown.html'
with open(base_file, 'r', encoding='utf-8') as f:
    base_content = f.read()

missing_towns = [
    ('Amity Township', 'amity-township'),
    ('Birdsboro', 'birdsboro'),
    ('Exeter Township', 'exeter-township'),
    ('Bechtelsville', 'bechtelsville')
]

for town_name, town_slug in missing_towns:
    # We replace Boyertown with the new town name
    new_content = base_content.replace('Boyertown', town_name)
    new_content = new_content.replace('boyertown', town_slug)
    # The zip code in Boyertown is 19512. Let's just blindly replace it if needed, or leave it.
    if town_name == 'Birdsboro': new_content = new_content.replace('19512', '19508')
    elif town_name == 'Bechtelsville': new_content = new_content.replace('19512', '19505')
    elif town_name == 'Exeter Township': new_content = new_content.replace('19512', '19606')
    elif town_name == 'Amity Township': new_content = new_content.replace('19512', '19518')

    with open(f'{town_slug}.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Generated {town_slug}.html")

# 2. Add Gallery and replace Area Towns links on ALL html files
gallery_html = """
    <!-- WORK GALLERY -->
    <section class="gallery section">
        <div class="container">
            <div class="section__header">
                <h2>Our Work</h2>
                <p>Real jobs, real results — all by Ed and his crew</p>
            </div>
            <div class="gallery__grid">
                <img src="work-2.jpg" alt="Seamless gutter installation" class="gallery__img">
                <img src="work-3.png" alt="Gutter guard installation" class="gallery__img">
                <img src="work-4.png" alt="Ed installing gutter guards" class="gallery__img">
                <img src="split-level.png" alt="Split level home gutter work" class="gallery__img">
                <img src="downspouts-done-right.png" alt="Professional downspout installation" class="gallery__img">
            </div>
        </div>
    </section>
"""

area_towns_replacement = """<div class="area__towns">
                <a href="/boyertown.html" class="town-link">Boyertown</a>
                <a href="/pottstown.html" class="town-link">Pottstown</a>
                <a href="/douglassville.html" class="town-link">Douglassville</a>
                <a href="/gilbertsville.html" class="town-link">Gilbertsville</a>
                <a href="/bechtelsville.html" class="town-link">Bechtelsville</a>
                <a href="/royersford.html" class="town-link">Royersford</a>
                <a href="/limerick.html" class="town-link">Limerick</a>
                <a href="/amity-township.html" class="town-link">Amity Township</a>
                <a href="/birdsboro.html" class="town-link">Birdsboro</a>
                <a href="/exeter-township.html" class="town-link">Exeter Township</a>
                <span>Pennsburg</span><span>East Greenville</span><span>Red Hill</span><span>Barto</span><span>Sassamansville</span><span>Colebrookdale</span><span>New Hanover</span>
            </div>"""

html_files = glob.glob("*.html")
for file in html_files:
    if file == 'blog.html': continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add gallery if missing (check for "gallery__grid")
    if 'gallery__grid' not in content and '<!-- SERVICE AREA MAP -->' in content:
        content = content.replace('<!-- SERVICE AREA MAP -->', gallery_html + '\n    <!-- SERVICE AREA MAP -->')

    # Replace area__towns block
    # Regex to find <div class="area__towns"> ... </div>
    pattern = re.compile(r'<div class="area__towns">.*?</div>', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(area_towns_replacement, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
