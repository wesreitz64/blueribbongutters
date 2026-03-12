import os
import glob

# Find all HTML files
html_files = glob.glob("*.html")

for file in html_files:
    if file == "thankyou.html":
        continue
    
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if the formspree action is in the file
    if 'action="https://formspree.io/f/xqeykjan"' in content:
        # Check if the redirect is already there
        if 'name="_next"' not in content:
            # We want to insert the hidden input right under the form opening tag
            target_str = '<form class="contact__form" action="https://formspree.io/f/xqeykjan" method="POST">'
            replacement_str = target_str + '\n                    <input type="hidden" name="_next" value="https://blueribbongutters.com/thankyou.html">'
            content = content.replace(target_str, replacement_str)
            
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {file}")
        else:
            print(f"Already updated {file}")
