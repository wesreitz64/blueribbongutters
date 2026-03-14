import os
import glob

favicon_tag = '<link rel="icon" type="image/png" href="icon-192.png">'
apple_tag = '<link rel="apple-touch-icon" href="icon-512.png">'

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "icon-192.png" not in content and apple_tag in content:
        content = content.replace(apple_tag, f'{favicon_tag}\n    {apple_tag}')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added favicon to {file}")
    else:
        print(f"Already has favicon or missing apple tag {file}")
