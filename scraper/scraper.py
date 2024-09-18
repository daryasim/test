import requests
from bs4 import BeautifulSoup
import random


def fetch_random_article_titles(num_articles):
    # Wikipedia's Random page URL
    url = "https://en.wikipedia.org/wiki/Special:Random"
    titles = []

    for _ in range(num_articles):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1', {'id': 'firstHeading'}).text
            titles.append(title)
        else:
            print(f"Failed to fetch article. Status code: {response.status_code}")

    return titles


def save_titles_to_file(titles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(f"{title}\n")


def main():
    num_articles = 5
    titles = fetch_random_article_titles(num_articles)
    save_titles_to_file(titles, 'random_wiki_articles.txt')
    print(f"Saved {num_articles} random Wikipedia article titles to 'random_wiki_articles.txt'.")


if __name__ == "__main__":
    main()
