from collections import deque
import os.path
from bs4 import BeautifulSoup
import httpx


def extract(source):
    doc = BeautifulSoup(source, "html.parser")
    blocks = deque()
    div_elems = doc.find_all("div")
    for div_el in div_elems:
        css_class = div_el["class"][0]
        if css_class == "accordion-title-text":
            blocks = append(blocks, extract_title(div_el))
            blocks = append(blocks, extract_title_text(div_el))
        elif css_class == "accordion-content-image":
            blocks = append(blocks, extract_content_image(div_el, as_local=True))
        elif css_class == "accordion-content-text":
            blocks = append(blocks, extract_content_text(div_el))
        else:
            continue
    return "".join(blocks)


def extract_images(source):
    doc = BeautifulSoup(source, "html.parser")
    images = deque()
    div_elems = doc.find_all("div", class_="accordion-content-image")
    for div_el in div_elems:
        image = extract_content_image(div_el)
        images = append(images, image)
    return "".join(images)


def download_images(source, to):
    doc = BeautifulSoup(source, "html.parser")
    for img_el in doc.find_all("img"):
        url = img_el["src"]
        filename = os.path.basename(url).lower()
        path = os.path.join(to, filename)
        if os.path.exists(path):
            continue
        with open(path, "wb") as file:
            file.write(httpx.get(url).content)


def extract_title(div_el):
    title_el = div_el.find("h2")
    if not title_el:
        return None
    title = "<h2>" + inner_text(title_el) + "</h2>"
    return title


def extract_title_text(div_el):
    paragraph_elems = div_el.find_all("p")
    if not paragraph_elems:
        return None
    paragraphs = [str(el) for el in paragraph_elems]
    return "\n".join(paragraphs)


def extract_content_image(div_el, as_local=False):
    image_el = div_el.find("img")
    if as_local:
        image_path = os.path.join("img", os.path.basename(image_el["src"]).lower())
    else:
        image_path = image_el["src"]
    image = '<img alt="{0}" src="{1}">'.format(image_el["alt"], image_path)
    return image


def extract_content_text(div_el):
    content = inner_html(div_el)
    return content


def inner_html(el):
    return "".join([str(x) for x in el.contents])


def inner_text(el):
    return el.find(text=True, recursive=False).strip()


def append(container, elem):
    if not elem:
        return container
    container.append(elem)
    container.append("\n")
    return container
