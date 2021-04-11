cd build
pandoc --css epub.css -o data-visualization-guide.epub data-visualization-guide.md

# (<(?:h1|h2|h3|p|img|ul|ol|li|pre)>)\s* -- \n$1
# \s+< -- <
# <p>(<img.+alt="([^"]+)"[^>]*>)</p> -- <figure>$1<figcaption>$2</figcaption></figure>
