from bs4 import BeautifulSoup
#import lxml
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article = soup.find_all(class_="storylink")
article_texts = []
article_links = []

for article_tag in article:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

highest_vote = max(article_upvote)
article_text = article_texts[article_upvote.index(highest_vote)]
article_link = article_links[article_upvote.index(highest_vote)]
print(article_text)
print(article_link)

 # with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# all_anchor_tags = soup.find_all("a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", id="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)