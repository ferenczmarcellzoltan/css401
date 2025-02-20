import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def soup():
    """Parse the HTML file and return a BeautifulSoup object."""
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    return BeautifulSoup(content, "html.parser")

def test_body_background_color(soup):
    style = soup.find("style").string
    assert "background-color: #8b0000;" in style, "The body background color should be dark red (#8b0000)."

def test_container_width(soup):
    style = soup.find("style").string
    assert ".container {\n            width: 50%;" in style, "The container width should be 50%."

def test_box_styles(soup):
    style = soup.find("style").string
    assert "width: 100px;" in style, "The box width should be 100px."
    assert "height: 100px;" in style, "The box height should be 100px."
    assert "background-color: orange;" in style, "The box background color should be orange."

def test_text_alignment(soup):
    text_div = soup.find("div", class_="text")
    assert text_div is not None, "A text div should exist."
    assert "Lorem ipsum" in text_div.text, "The text content should include Lorem ipsum."

def test_flexbox_layout(soup):
    style = soup.find("style").string
    assert "display: flex;" in style, "The layout should use flexbox."
    assert "gap: 20px;" in style, "There should be a gap of 20px between the box and the text."
