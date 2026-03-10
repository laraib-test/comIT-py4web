# Last time modified: 03/04/26
# Author: y44k0v

html_base = ""
# Read template HTML

with open("garbage.html", "r") as website:
    html_base = website.read()
    
# Page title
page_title = "Modern Apparel"

html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

# daisy UI libraries

daisy_ui ="""

<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<!-- Daisy ui themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

"""

html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

theme = "retro"
html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

#Navbar
nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
  <a class="btn btn-ghost text-xl">Modern Apparel</a>
</div>
"""


html_modified = html_modified.replace('<body>', '<body>\n'+nav_bar)





with open("index.html", "w") as file:
    file.write(html_modified)