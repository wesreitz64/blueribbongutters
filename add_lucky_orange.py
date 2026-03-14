import os
import glob

lo_tag = '<script async defer src="https://tools.luckyorange.com/core/lo.js?site-id=5162d7f3"></script>'

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "tools.luckyorange.com/core/lo.js" not in content:
        # insert right before </head>
        content = content.replace('</head>', f'    {lo_tag}\n</head>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added lucky orange to {file}")
    else:
        print(f"Already has lucky orange {file}")
