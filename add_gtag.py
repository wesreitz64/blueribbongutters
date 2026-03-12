import os
import glob

gtag = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-11121961747"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-11121961747');
</script>"""

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "AW-11121961747" not in content:
        # insert right after <head>
        content = content.replace('<head>', f'<head>\n    {gtag}\n')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added gtag to {file}")
    else:
        print(f"Already has gtag {file}")
