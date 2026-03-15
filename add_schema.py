import os
import glob

schema_tag = """<!-- JSON-LD LocalBusiness Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Blue Ribbon Seamless Gutter",
  "image": "https://blueribbongutters.com/logo.png",
  "@id": "https://blueribbongutters.com/",
  "url": "https://blueribbongutters.com/",
  "telephone": "+16103227069",
  "priceRange": "$$",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "",
    "addressLocality": "Boyertown",
    "addressRegion": "PA",
    "postalCode": "19512",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 40.334000,
    "longitude": -75.637500
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday"
    ],
    "opens": "07:00",
    "closes": "18:00"
  }
}
</script>"""

# Find all HTML files in current directory and in _layouts
html_files = glob.glob("*.html") + glob.glob("_layouts/*.html")
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "application/ld+json" not in content:
        # insert right before </head>
        if "</head>" in content:
            content = content.replace('</head>', f'{schema_tag}\n</head>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added schema to {file}")
        else:
            print(f"Could not find head tag in {file}")
    else:
        print(f"Already has schema {file}")
