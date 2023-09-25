import requests
from bs4 import BeautifulSoup


# Scrape
def scrape_summery(url):
    response = requests.get(url)
    title, author, summery = ("", "", "")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.title.string
        meta_description = soup.find("meta", attrs={"name": "description"})
        author_tag = soup.find("meta", attrs={"name": "author"})
        if meta_description:
            summery = meta_description.get("content")
        if title_tag:
            title = title_tag
        if author_tag:
            author = author_tag.get("content")
    return {"title": title, "summery": summery, "author": author}
