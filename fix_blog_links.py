import glob

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the duplicate desktop links
    while '                <a href="/blog.html">Blog</a>\n                <a href="/blog.html">Blog</a>' in content:
        content = content.replace('                <a href="/blog.html">Blog</a>\n                <a href="/blog.html">Blog</a>', '                <a href="/blog.html">Blog</a>')
        
    # Fix the duplicate mobile links
    while '            <a href="/blog.html">Blog</a>\n            <a href="/blog.html">Blog</a>' in content:
        content = content.replace('            <a href="/blog.html">Blog</a>\n            <a href="/blog.html">Blog</a>', '            <a href="/blog.html">Blog</a>')

    if file == 'blog.html':
        # Remove the link to itself completely on the blog page
        content = content.replace('\n                <a href="/blog.html">Blog</a>', '')
        content = content.replace('\n            <a href="/blog.html">Blog</a>', '')
        
        # Also catch footer if any
        content = content.replace('\n                <a href="/blog.html">Blog</a>', '')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed blog links.")
