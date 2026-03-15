import os
import glob

clarity_tag = """<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "ievv7x1uek");
</script>"""

# Find all HTML files in current directory and in _layouts
html_files = glob.glob("*.html") + glob.glob("_layouts/*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "ievv7x1uek" not in content:
        # insert right after <head> or replace </head> with tag + </head>
        if "<head>" in content:
            content = content.replace('<head>', f'<head>\n    {clarity_tag}\n')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added clarity to {file}")
        elif "</head>" in content:
            content = content.replace('</head>', f'    {clarity_tag}\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added clarity to {file}")
        else:
            print(f"Could not find head tag in {file}")
    else:
        print(f"Already has clarity {file}")
