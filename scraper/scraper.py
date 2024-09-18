import requests
from bs4 import BeautifulSoup


def fetch_random_article_titles(num_articles):
    url = "https://en.wikipedia.org/wiki/Special:Random"
    titles = []

    for _ in range(num_articles):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1', {'id': 'firstHeading'}).text
            titles.append(title)
            print(f"Fetched title: {title}")  # Debug: Print title to console
        else:
            print(f"Failed to fetch article. Status code: {response.status_code}")

    return titles


def save_titles_to_file(titles, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Use 'w' mode to overwrite
            for title in titles:
                file.write(f"{title}\n")
        print(f"Saved titles to {filename}")  # Debug: Confirm file saving
    except Exception as e:
        print(f"Failed to write to file: {e}")

def main():
    num_articles = 5
    titles = fetch_random_article_titles(num_articles)
    save_titles_to_file(titles, 'random_wiki_articles.txt')
    print(f"Completed fetching and saving {num_articles} articles.")


if __name__ == "__main__":
    main()
