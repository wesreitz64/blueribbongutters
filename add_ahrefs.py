import os
import glob

ahrefs_tag = """<!-- Ahrefs Analytics -->
<script src="https://analytics.ahrefs.com/analytics.js" data-key="m3HTzeCMSRGKXeT2mQI3qQ" async></script>"""

# Find all HTML files in current directory and in _layouts
html_files = glob.glob("*.html") + glob.glob("_layouts/*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "https://analytics.ahrefs.com/analytics.js" not in content:
        # insert right before </head>
        if "</head>" in content:
            content = content.replace('</head>', f'{ahrefs_tag}\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Ahrefs to {file}")
        else:
            print(f"Could not find head tag in {file}")
    else:
        print(f"Already has Ahrefs {file}")
