import glob

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="/blog.html"' not in content:
        # replace desktop nav
        content = content.replace('</nav>', '    <a href="/blog.html">Blog</a>\n            </nav>', 1)
        # replace mobile nav
        content = content.replace('</nav>', '    <a href="/blog.html">Blog</a>\n        </nav>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added blog link to {file}")
    else:
        print(f"Blog link already in {file}")
