import os
import glob

ahrefs_meta_tag = '<meta name="ahrefs-site-verification" content="46d9a2cbd4cf38a79b3cad164afe78627d9d4572cd5337ba5ee19731a94d3dbb">'

# Find all HTML files in current directory and in _layouts
html_files = glob.glob("*.html") + glob.glob("_layouts/*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "ahrefs-site-verification" not in content:
        # insert right before </head>
        if "</head>" in content:
            content = content.replace('</head>', f'    {ahrefs_meta_tag}\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Ahrefs meta tag to {file}")
        else:
            print(f"Could not find head tag in {file}")
    else:
        print(f"Already has Ahrefs meta tag {file}")
