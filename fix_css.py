import re
import urllib.parse

with open('/Users/emilyli/mywebsite/style.css', 'r') as f:
    content = f.read()

def encode_svg(match):
    prefix = match.group(1)
    svg_content = match.group(2)
    suffix = match.group(3)
    
    # URL encode the SVG content
    encoded_svg = urllib.parse.quote(svg_content)
    
    # If it's a mask-image, we want to output both -webkit-mask-image and mask-image
    if '-webkit-mask-image' in prefix:
        return f"-webkit-mask-image: url('data:image/svg+xml;utf8,{encoded_svg}'); mask-image: url('data:image/svg+xml;utf8,{encoded_svg}');"
    else:
        return f"{prefix}url('data:image/svg+xml;utf8,{encoded_svg}'){suffix};"

# Replace all url('data:image/svg+xml;utf8,<svg...>')
pattern = r"(-webkit-mask-image:\s*|background:\s*)url\('data:image/svg\+xml;utf8,(<svg.*?</svg>)'\)(.*?);"
new_content = re.sub(pattern, encode_svg, content)

with open('/Users/emilyli/mywebsite/style.css', 'w') as f:
    f.write(new_content)

print("Done")
