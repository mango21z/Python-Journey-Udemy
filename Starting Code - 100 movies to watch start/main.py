import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movie_title = soup.find_all(name="h3",class_="title")
movie_list = [movie.getText() for movie in movie_title]
movie_list.reverse()
# print(movie_list)

with open('movie_list.txt', 'w', encoding="UTF-8") as f:
    for movie in movie_list:
        f.write(f"{movie}\n")



