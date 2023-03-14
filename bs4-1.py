# utilisation de bs4
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# la base pour scraper
soup = BeautifulSoup(html_doc, 'html.parser')

# on récupère la balise title + son contenu
print( soup.title )

# on récupère le contenu uniquement de la balise title
print( soup.title.string )

# on récupère tous les liens
links = soup.find_all("a") 

# on parcours tous les liens
for link in links:
    # on affiche le lien complet
    print( link )
    # on affiche le texte du lien
    print( "texte : ", link.string )
    # on affiche le href
    print( "href : ", link["href"] )

