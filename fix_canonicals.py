import glob
import re

html_files = glob.glob("*.html")
for file in html_files:
    if file == 'index.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find canonical links: <link rel="canonical" href="https://blueribbongutters.com/town">
    # and change them to https://blueribbongutters.com/town.html
    # but only if they don't already have .html (and are not the homepage)
    
    def repl(m):
        url = m.group(1)
        if url.endswith('.html') or url == '/':
            return m.group(0) # no change
        # If it doesn't end with .html, add it
        return f'<link rel="canonical" href="{url}.html">'
        
    new_content = re.sub(r'<link rel="canonical" href="([^"]+)">', repl, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated canonical in {file}")

